class Cryptocurrency:
    def __init__(self, name, symbol, market_cap, volume_24h, circulating_supply, total_supply, max_supply, fully_diluted_market_cap):
        self.name = name
        self.symbol = symbol
        self.market_cap = market_cap
        self.volume_24h = volume_24h
        self.circulating_supply = circulating_supply
        self.total_supply = total_supply
        self.max_supply = max_supply
        self.fully_diluted_market_cap = fully_diluted_market_cap

    def __str__(self):
        return f"{self.name} ({self.symbol}): {self.market_cap}"
