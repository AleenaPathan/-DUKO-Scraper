from celery import shared_task
from.coinmarketcap import CoinMarketCap

@shared_task
def start_scraping():
    coinmarketcap = CoinMarketCap('bitcoin')
    data = coinmarketcap.scrape_data()
    # Save data to database
    Coin.objects.create(**data)
    return 'Scraping completed'

@shared_task
def get_scraping_status():
    return 'Scraping in progress'
