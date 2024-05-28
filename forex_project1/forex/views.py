from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CurrencyPair
from django.shortcuts import render

class CurrencyPairView(APIView):
    def get(self, request):
        pairs = CurrencyPair.objects.all().values()
        return Response(pairs)

def index(request):
    return render(request, 'forex/index.html')