from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psycopg2

db_host='localhost'
db_name='biblioteka'
db_user='postgres'
db_password='Pprivatu22'
connection=psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
cursor=connection.cursor()
create_table_querry='''
CREATE TABLE IF NOT EXISTS bibliotekos(
    biblioteka_id serial primary key,
    pavadinimas text,
    autorius text,
    publikavimo_duomenys text
)
'''
cursor.execute(create_table_querry)

webdriver_path = "C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe"
service = Service(webdriver_path)
service.start()
driver = webdriver.Chrome(service=service)
data = []

url= f'https://ibiblioteka.lt/metis/publication?q=y3z3t6av9'
driver.get(url)
def paspausti():
    load_more = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.mat-stroked-button > button:nth-child(1)'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", load_more)
    load_more.click()
    time.sleep(4)

driver.execute_script('window.scrollBy(0, 500);')
time.sleep(4)
for i in range(1, 2):
    paspausti()

soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('table', class_='c-data-table')

if table:
    for row in table.find_all("div", class_='c-result-item__details'):
        cols = row.find_all("p")
        if len(cols) >= 3:
            title = cols[0].text.strip().replace('Pavadinimas:','').replace('[', '').replace(']', '')
            if cols[1].text.strip().startswith('Autorius:'):
                author = cols[1].text.strip().replace('Autorius:', '')
                if cols[2].text.strip().startswith('Laidos duomenys:'):
                    continue
                else:
                    pub_data = cols[2].text.strip().replace('Publikavimo duomenys:', '')
            elif cols[1].text.strip().startswith('Publikavimo duomenys:'):
                continue
            else:
                continue
            insert_querry = '''
            INSERT INTO bibliotekos(pavadinimas, autorius, publikavimo_duomenys)values(%s, %s, %s)
            '''
            cursor.execute(insert_querry,(title, author, pub_data))
            connection.commit()


            # bibl_data = {
            #     'Pavadinimas': title,
            #     'Autorius': author,
            #     'Publikavimo duomenys': pub_data
            # }
            # data.append(bibl_data)

# driver.quit()
# df = pd.DataFrame(data)
# df.to_csv("biblioteka.csv", index = False)