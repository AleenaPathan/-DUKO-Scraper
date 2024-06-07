import requests
from bs4 import BeautifulSoup
from models import DUKO

def scrape_duko():
    url = "https://coinmarketcap.com/currencies/duko/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    duko = DUKO()
    duko.name = soup.find("h1", {"class": "coin-item-symbol"}).text.strip()
    duko.price = soup.find("div", {"class": "priceValue"}).text.strip()
    duko.market_cap = soup.find("div", {"class": "marketCapValue"}).text.strip()
    duko.volume_24h = soup.find("div", {"class": "volumeValue"}).text.strip()
    duko.circulating_supply = soup.find("div", {"class": "circulatingSupplyValue"}).text.strip()
    duko.total_supply = soup.find("div", {"class": "totalSupplyValue"}).text.strip()
    duko.max_supply = soup.find("div", {"class": "maxSupplyValue"}).text.strip()
    duko.fully_diluted_market_cap = soup.find("div", {"class": "fullyDilutedMarketCapValue"}).text.strip()

    return duko
