import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re

webdriver_path = "C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe"
service = Service(webdriver_path)
service.start()
driver = webdriver.Chrome(service=service)
data = []

for i in range(1,5):
    url = f"https://coinmarketcap.com/?page={i}"
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window. scrollBy(0,300);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table')

    if table:
        for row in table.find("tbody").find_all("tr"):
            columns = row.find_all("td")
            if len(columns) >= 9:
                volume_text = columns[8].text.strip()
                volume_match = re.search(r'\$\d{1,3}(,\d{3})*\.?\d*[BMK]?',volume_text)
                volume = volume_match.group(0)[:15] if volume_match else 'N/A'

                market_text = columns[7].text.strip()
                market_match = re.search(r'\$\d{1,3}(,\d{3})*\.?\d*[BMK]?',market_text)
                market = market_match.group(0) if market_match else 'N/A'

                crypto_data = {
                    'Name': columns[2].text.strip(),
                    'Price': columns[3].text.strip(),
                    '1h %': columns[4].text.strip(),
                    '24h %': columns[5].text.strip(),
                    '7d %': columns[6].text.strip(),
                    'Market Cap': market,
                    'Volume(24h)': volume,
                    'Circulating Supply': columns[9].text.strip(),
                }
                data.append(crypto_data)

driver.quit()
df = pd.DataFrame(data)
df.to_csv("crypto.csv", index = False)
