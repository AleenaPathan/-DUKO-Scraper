import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

class CoinMarketCap:
    def __init__(self, coin):
        self.coin = coin
        self.url = f"https://coinmarketcap.com/currencies/{coin}/"

    def scrape_data(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        price = soup.find('div', {'class': 'priceValue'}).text
        price_change = soup.find('span', {'class': 'c-15yy2pl-0'}).text
        market_cap = soup.find('div', {'class': 'tatsValue'}).text
        market_cap_rank = soup.find('span', {'class': 'tatsRank'}).text
        volume = soup.find('div', {'class': 'tatsValue'}).text
        volume_rank = soup.find('span', {'class': 'tatsRank'}).text
        volume_change = soup.find('span', {'class': 'c-15yy2pl-0'}).text
        circulating_supply = soup.find('div', {'class': 'tatsValue'}).text
        total_supply = soup.find('div', {'class': 'tatsValue'}).text
        diluted_market_cap = soup.find('div', {'class': 'tatsValue'}).text

        contracts = []
        contract_elements = soup.find_all('div', {'class': 'c-1q9q90x-0'})
        for element in contract_elements:
            contract_name = element.find('span', {'class': 'c-1q9q90x-1'}).text
            contract_address = element.find('span', {'class': 'c-1q9q90x-2'}).text
            contracts.append({'name': contract_name, 'address': contract_address})

        official_links = []
        official_link_elements = soup.find_all('div', {'class': 'c-1q9q90x-0'})
        for element in official_link_elements:
            link_name = element.find('span', {'class': 'c-1q9q90x-1'}).text
            link_url = element.find('a')['href']
            official_links.append({'name': link_name, 'link': link_url})

        socials = []
        social_elements = soup.find_all('div', {'class': 'c-1q9q90x-0'})
        for element in social_elements:
            social_name = element.find('span', {'class': 'c-1q9q90x-1'}).text
            social_url = element.find('a')['href']
            socials.append({'name': social_name, 'url': social_url})

        data = {
            'price': price,
            'price_change': price_change,
            'arket_cap': market_cap,
            'arket_cap_rank': market_cap_rank,
            'volume': volume,
            'volume_rank': volume_rank,
            'volume_change': volume_change,
            'circulating_supply': circulating_supply,
            'total_supply': total_supply,
            'diluted_market_cap': diluted_market_cap,
            'contracts': contracts,
            'official_links': official_links,
            'ocials': socials
        }

        return data

    def get_json_response(self, data):
        return {'coin': self.coin, 'output': data}
