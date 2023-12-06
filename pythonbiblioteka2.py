import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
import csv

db_host='localhost'
db_name='biblioteka'
db_user='postgres'
db_password='Pprivatu22'
connection=psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
cursor=connection.cursor()
create_table_querry='''
CREATE TABLE IF NOT EXISTS bibliotekos2(
    biblioteka2_id serial primary key,
    pavadinimas text,
    autorius text,
    publikavimo_duomenys text
)
'''
cursor.execute(create_table_querry)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }

data = []
for i in range(1, 10):
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
    insert_querry = '''
                INSERT INTO bibliotekos2(pavadinimas, autorius, publikavimo_duomenys)values(%s, %s, %s)
                '''
    cursor.execute(insert_querry, (title_text, author_text, pub_data_text))
    connection.commit()