import json
import yfinance as yf
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
import asyncio

class CurrencyPairConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.pair = 'EURUSD=X'
        asyncio.create_task(self.send_currency_updates())

    async def disconnect(self, close_code):
        await self.close()

    async def send_currency_updates(self):
        while True:
            data = await self.get_currency_data()
            print(f"Sending data: {data}")  # Log data to console for debugging
            await self.send(text_data=json.dumps(data))
            await asyncio.sleep(60)  # Update every 5 seconds

    async def get_currency_data(self):
        ticker = yf.Ticker(self.pair)
        hist = ticker.history(period='1d', interval='1m')  # 1 month period with 5 minutes interval

        # Log historical data for debugging
        print(hist)

        # Create candlestick data from the historical data
        data = []
        for timestamp, row in hist.iterrows():
            data.append({
                'timestamp': timestamp.isoformat(),
                'open': row['Open'],
                'high': row['High'],
                'low': row['Low'],
                'close': row['Close'],
            })
        return data

    async def get_current_timestamp(self):
        return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
