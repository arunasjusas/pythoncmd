import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

url = "https://www.engelvoelkers.com/en-us/properties/rent-apartment/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find_all('div', class_='ev-teaser-content')
table_data = []
for house in table:
    title = house.find('div', class_='ev-teaser-title').text.strip()[10::]
    location = house.find('div', class_='ev-teaser-subtitle').text.strip()
    price = house.find('div', class_='ev-value').text.strip().replace(' USD', '')
    house_details = house.find_all('span', class_='ev-teaser-attribute-value')
    if len(house_details) >= 4:
        bedrooms = house_details[0].text.strip()
        bathrooms = house_details[1].text.strip()
        surface_area = house_details[2].text.strip().replace(' m²', '')
        property_area = house_details[3].text.strip().replace(' m²', '')
    else:
        continue
    table_data.append({
        'Valstybe': title,
        'Adresas': location,
        'Kaina': price,
        'Miegamieji': bedrooms,
        'Vonios kambariai': bathrooms,
        'Patalpu dydis': surface_area,
        'Visos nuosavybes dydis': property_area
    })

df = pd.DataFrame(table_data)



### ANALIZE:
# Vidutinis plotas pagal vietove:
# df['Patalpu dydis'] = df['Patalpu dydis'].astype(float) # Teksa pavercia i skaiciu reiksme
# avg_area_by_location = df.groupby('Adresas')['Patalpu dydis'].mean()
# print(avg_area_by_location)

# Kainu paskirstymas pagal vietove:
# df['Kaina'] = df['Kaina'].astype(float) # Teksa pavercia i skaiciu reiksme
# sns.boxplot(x='Adresas', y='Kaina', data=df)
# plt.xticks(rotation=45)
# plt.show()

# Bendra ploto ir kainos rysys:
# plt.figure(figsize=(12,6))
# sns.scatterplot(x='Patalpu dydis', y='Kaina', data=df)
# plt.title('Bendra ploto ir kainos rysis')
# plt.show()

# Miegamuju ir vonios kambariu skaicius pasiskirstymas:
# plt.figure(figsize=(12,6))
# plt.subplot(1,2,1)
# sns.displot(df['Miegamieji'], kde=True, bins=5)
# plt.title('Miegamuju skaiciaus paskirstymas')
# plt.subplot(1,2,2)
# sns.displot(df['Vonios kambariai'], kde=True, bins=5)
# plt.title('Vonios kambariu skaiciaus pasiskirstymas')
# plt.show()

# Kainu paskirstymas:
# plt.figure(figsize=(12,6))
# sns.displot(df['Kaina'], bins=20, kde=True)
# plt.title('Kainu pasiskirstymas')
# plt.show()

# 3D Grafikas:
# fig = plt.figure(figsize=(10,8))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(df['Miegamieji'], df['Patalpu dydis'], df['Kaina'], c='blue', marker='o')
# ax.set_xlabel('Miegamieji')
# ax.set_ylabel('Patalpu dydis')
# ax.set_zlabel('Kaina')
# plt.title('Kainos miegamuju sk. ir bendro ploto santykis')
# plt.show()