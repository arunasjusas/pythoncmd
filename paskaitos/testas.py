import requests
from bs4 import BeautifulSoup
import csv


def gauti_svetaines_turini(url):
    atsakymas = requests.get(url)
    return atsakymas.content


def turinio_analize(turinys):
    soup = BeautifulSoup(turinys, 'html.parser')
    objektu_informacija = []

    objektai = soup.find_all('div', class_='project-list-item')
    for objektas in objektai:
        pavadinimas = objektas.find('h2', class_='project-title-full project-title')
        title = pavadinimas.get_text(strip=True) if pavadinimas else None

        if not title:
            continue
        plotas_ir_kaina = objektas.find('h3', class_='project-title-full project-min-values')

        if plotas_ir_kaina:
            h3_tekstas = plotas_ir_kaina.get_text(" ", strip=True)
            h3_dalys = h3_tekstas.split('|')
            plotas = None
            kaina = None

            for tekstas in h3_dalys:
                if 'Plotas' in tekstas:
                    plotas = tekstas.split(':')[1].strip().replace(' ', '')
                elif 'Kaina' in tekstas:
                    kaina = tekstas.split(':')[1].strip()
            plotas = plotas if plotas is not None else "Plotas nerastas"
            kaina = kaina if kaina is not None else "Kaina nerasta"
        else:
            plotas = "Plotas nerastas"
            kaina = "Kaina nerasta"


        objektu_informacija.append({
            'pavadinimas': title,
            'plotas': plotas,
            'kaina': kaina
        })

    return objektu_informacija

def csv_failas(failo_pav, duomenys):

    with open(failo_pav, mode='w', newline='', encoding='utf-8') as failas:
        writer = csv.DictWriter(failas, fieldnames=duomenys[0].keys())
        writer.writeheader()
        for objektas in duomenys:
            writer.writerow(objektas)

def main():
    url = "https://www.aruodas.lt/uzsienio-objektai/"
    turinys = gauti_svetaines_turini(url)

    if turinys:
        duomenys = turinio_analize(turinys)
        if duomenys:
            csv_failas('testas.csv', duomenys)
        else:
            print("Nerasta jokių objektų.")
    else:
        print("Negautas turinys iš svetainės.")


if __name__ == '__main__':
    main()