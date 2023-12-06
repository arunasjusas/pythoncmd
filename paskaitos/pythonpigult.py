import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2


db_host='localhost'
db_name='pythonpigu'
db_user='postgres'
db_password='Pprivatu22'
connection=psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
cursor=connection.cursor()
create_table_querry='''
CREATE TABLE IF NOT EXISTS ratlankiai(
    id serial primary key,
    pavadinimas varchar(255),
    kaina decimal(10,2),
    diametras int
)
'''
cursor.execute(create_table_querry)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

url = "https://pigu.lt/lt/autoprekes/ratlankiai"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

info = soup.find_all('p', class_='product-name')
price = soup.find_all('div', class_='product-price')
rate = soup.find_all('div', class_='product-options__item')[::6]

all_data = []
for info,price,rate in zip(info, price, rate):
    info_text = info.get_text().split()[0]
    price_text = price.get_text().split()[0]
    rate_text = rate.get_text().split()[2]
    insert_querry = '''
    INSERT INTO ratlankiai(pavadinimas, kaina, diametras)values(%s, %s, %s)
    '''
    cursor.execute(insert_querry,(info_text, price_text, rate_text))
    connection.commit()
    # all_data.append({
    #     'Pavadinimas': info_text,
    #     'Kaina': price_text,
    #     'Diametras': rate_text,
    # })

# df = pd.DataFrame(all_data)
# df.to_csv("pythonpigult.csv", index = False)
# print(df)