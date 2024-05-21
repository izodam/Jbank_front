from .models import ExchangeRates
from rest_framework import serializers

class ExchangeRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRates
        fields = '__all__'