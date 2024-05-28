from django.urls import path
from .views import CurrencyPairView
from .views import index, CurrencyPairView

urlpatterns = [
    path('', index, name='index'),
    path('api/currency_pairs/', CurrencyPairView.as_view(), name='currency_pairs'),
]
