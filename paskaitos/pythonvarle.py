import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


info = soup.find_all('div', class_='spec-shortcuts')

price = soup.find_all('div', class_='price-container')

rate = soup.find_all('li', class_='rating')

stock = soup.find_all('li', class_='stock')

all_data = []
for info, price, rate, stock in zip(info, price, rate, stock):
    info_text = info.get_text().replace('Gamintojas', '').split()[0]
    price_text = price.get_text().split()[0]
    rate_text = rate.get_text().split()[0]

    stock_raw_text = stock.get_text()
    stock_match = re.search(r'(\d+\+?)', stock_raw_text)
    stock_text = stock_match.group(1) if stock_match else "Unknown"

    all_data.append({
        'INFO': info_text,
        'KAINA': price_text,
        'REITINGAS': rate_text,
        'LIKUTIS': stock_text
    })

df = pd.DataFrame(all_data)
df.to_csv("pythonvarle.csv", index = False)
print(df)