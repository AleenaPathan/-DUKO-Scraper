from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    price_change = models.DecimalField(max_digits=20, decimal_places=10)
    market_cap = models.DecimalField(max_digits=20, decimal_places=10)
    market_cap_rank = models.IntegerField()
    volume = models.DecimalField(max_digits=20, decimal_places=10)
    volume_rank = models.IntegerField()
    volume_change = models.DecimalField(max_digits=20, decimal_places=10)
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=10)
    total_supply = models.DecimalField(max_digits=20, decimal_places=10)
    diluted_market_cap = models.DecimalField(max_digits=20, decimal_places=10)
    contracts = models.TextField()
    official_links = models.TextField()
    socials = models.TextField()

    def __str__(self):
        return self.name
