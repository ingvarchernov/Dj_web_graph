import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import yfinance as yf
from datetime import datetime, timezone

class CurrencyPairConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_updating = True
        self.data = []  # Зберігатиме всі отримані дані
        asyncio.create_task(self.send_currency_updates())

    async def disconnect(self, close_code):
        self.keep_updating = False

    async def send_currency_updates(self):
        while self.keep_updating:
            # Отримання реальних даних з Yahoo Finance
            new_data = self.get_real_time_data('EURUSD=X')
            self.data.extend(new_data)  # Додати нові дані до загального набору
            serialized_data = self.serialize_data(self.data)
            await self.send(text_data=serialized_data)
            await asyncio.sleep(20)

    def get_real_time_data(self, ticker):
        stock = yf.Ticker(ticker)
        hist = stock.history(period='5d', interval='1h')
        hist = hist.reset_index()
        return hist.to_dict(orient='records')  # Повернути всі дані за день

    def serialize_data(self, data):
        # Конвертуємо Timestamp в ISO 8601 строку з часовою зоною UTC, якщо це об'єкт datetime
        for entry in data:
            if isinstance(entry['Datetime'], datetime):
                entry['Datetime'] = entry['Datetime'].isoformat()
        return json.dumps(data)
