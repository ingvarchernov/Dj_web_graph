from django.db import models

class CurrencyPair(models.Model):
    symbol = models.CharField(max_length=10)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol
