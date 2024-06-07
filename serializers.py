from rest_framework import serializers
from.models import Coin

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['name', 'ymbol', 'price', 'price_change', 'arket_cap', 'arket_cap_rank', 'volume', 'volume_rank', 'volume_change', 'circulating_supply', 'total_supply', 'diluted_market_cap', 'contracts', 'official_links', 'ocials']
      
