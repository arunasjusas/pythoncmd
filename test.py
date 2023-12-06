import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }

data = []
for i in range(1, 50):
    url=f'https://elvislab.lt/leidiniai/{i}'

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', class_='-my-4 text-3xl font-bold')
    if not title:
        continue
    title_text = title.get_text()
    author = soup.find('h2', class_='mb-3 pb-1 text-primary font-bold')
    if not author:
        continue
    author_text = author.get_text()
    if len(soup.find_all('div', class_='md:w-7/12')) <= 9:
        continue
    pub_data = soup.find_all('div', class_='md:w-7/12')[9]
    pub_data_text = pub_data.get_text().replace('|', '').replace('\n', '').replace(
        '                                               ', ' ')
    # print(pub_data_text)
    book_info = {
        'Pavadinimas': title_text,
        'Autorius': author_text,
        'Publikavimo duomenys': pub_data_text
    }
    data.append(book_info)
df = pd.DataFrame(data)
df.to_csv("elvisk.csv", index = False)