import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CurrencyPairConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print('WebSocket connection accepted')

        # Надсилаємо тестове повідомлення одразу після підключення клієнта
        test_data = json.dumps([
            {
                'timestamp': '2024-05-28T21:20:04.728Z',
                'price': 1.2345
            }
        ])
        await self.send(text_data=test_data)
        print('Sent test data:', test_data)

    async def disconnect(self, close_code):
        print('WebSocket connection closed with code:', close_code)

    async def receive(self, text_data):
        print('Message received:', text_data)
        # Тут ви можете обробляти отримані від клієнта повідомлення
