from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/currency_pairs/$', consumers.CurrencyPairConsumer.as_asgi()),
]
