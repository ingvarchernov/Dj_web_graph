"""
ASGI config for forex_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import sys
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path

#from forex_project1.forex.consumers import CurrencyPairConsumer

# Додаємо батьківську директорію до системного шляху
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Встановлюємо змінну оточення для налаштувань Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forex_project.settings')

# Налаштовуємо середовище Django
django.setup()

# Імпортуємо клас консумера WebSocket
from forex.consumers import CurrencyPairConsumer

# Завантажуємо ASGI додаток
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path('ws/currency_pairs/', CurrencyPairConsumer.as_asgi()),
    ]),
})

