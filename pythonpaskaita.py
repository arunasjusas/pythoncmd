# # # import requests
# # # from bs4 import BeautifulSoup
# # # import csv
# # #
# # # headers = {
# # #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
# # # }
# # # # define website url
# # # URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# # # response = requests.get(URL, headers=headers)
# # # # 403 Forbideen - permission denied
# # # # 200 OK - website is alive
# # # # 500 Server error
# # # # if response.status_code == 200:
# # # #     print(f"Svetaine veikia: {response.status_code}")
# # # # else:
# # # #     print(f"Svetaine neveikia: {response.status_code}")
# # # soup = BeautifulSoup(response.content, 'html.parser')
# # # # print(soup)
# # # movies = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-59b6048d-0 cuaJSp cli-parent')
# # # new_movies_list = []
# # #
# # # for movie in movies:
# # #     title = movie.find('h3', class_='ipc-title__text').text.strip()
# # #     years = movie.find('span', class_='sc-479faa3c-8 bNrEFi cli-title-metadata-item').text.strip()
# # #     length = movie.find('div', class_='sc-479faa3c-7 jXgjdT cli-title-metadata').text.strip()[4:10]
# # #     new_movies_list.append((title, years, length))
# # #
# # # # print(new_movies_list)
# # # csv_file = "data.csv"
# # # with open(csv_file, 'w', newline='', encoding='utf-8') as file:
# # #     writer = csv.writer(file)
# # #     writer.writerow(['Title', 'Years', 'Movie Length'])
# # #     writer.writerows(new_movies_list)
# # #
# # # print(f"Data has been written to {csv_file}")
# #
# # # Namų darbai:
# # #
# # # 1. Sukurkite funkciją, kuri patikrina, ar skaičius yra pirminis ir grąžina True arba False. Naudokite funkciją patikrinti skaičiams nuo 1 iki 20.
# # # 2. Sukurkite funkciją lyginiai, kuri priima sąrašą skaičių ir naudoja for ciklą surasti visus lyginius skaičius, grąžindama juos kaip naują sąrašą.
# # # 3. Parašykite funkciją, kuri priima skaičių sąrašą ir grąžina vidurkį. Funkcijos viduje naudokite for ciklą, kad iteruotumėte per sąrašą.
# # # 4. Sukurkite funkciją, kuri priima skaičių sąrašą kaip argumentą ir naudojant for ciklą grąžina didžiausią skaičių.
# # # 5. Sukurkite programą, kuri nuolat prašo vartotoją įvesti skaičių, kol jis įves 0, tada uždaro programą.
# # #
# # # 1.
# # #
# # #
# # # 2.
# # # 2. Sukurkite funkciją lyginiai, kuri priima sąrašą skaičių ir naudoja for ciklą surasti visus lyginius skaičius, grąžindama juos kaip naują sąrašą.
# # def lyginiai(sarasas):
# #     lyginiai_skaiciai = []
# #
# #     for skaicius in sarasas:
# #         if skaicius % 2 == 0:
# #             lyginiai_skaiciai.append(skaicius)
# #     return lyginiai_skaiciai
# #
# # pradinis_sarasas = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# # rezultatas = lyginiai(pradinis_sarasas)
# #
# # print(f"Lyginiai skaiciai: {rezultatas}")
# # #
# # #
# # # 3.
# # #
# # #
# # # 4.
# # #
# # #
# # # 5.
# # Sukurkite programą, kuri nuolat prašo vartotoją įvesti skaičių, kol jis įves 0, tada uždaro programą.
# # meniu = """
# # """
# #
# # pasirinkimas = 1
# # while pasirinkimas != 0:
# #     print(meniu)
# #     try:
# #         pasirinkimas = int(input("Iveskite skaiciu: "))
# #         if pasirinkimas == 0:
# #             print("Programa uzdaryta!")
# #     except ValueError:
# #         print("Ivestis turi buti skaicius")
# #
# # """
# # class KlasesPavadinimas:
# #
# #     def __init__ - konstruktorius(savybes)
# #
# #     // metodai
# #     def atspausdinti_informacija():
# # """
#
#
# # class Automobilis:
# #     def __init__(self, marke, modelis):
# #         self.marke = marke
# #         self.modelis = modelis
# #
# #
# #     def automobilio_info(self):
# #         print(f"Automobilio marke: {self.marke}, modelis: {self.modelis}")
# #
# #
# # audi = Automobilis("Toyota", "Auris")
# # audi.automobilio_info()
# #
# # class Preke:
# #     def __init__(self, prekes_kodas, pavadinimas, kaina):
# #         self.prekes_kodas = prekes_kodas
# #         self.pavadinimas = pavadinimas
# #         self.kaina = kaina
# #
# #     def atspausdinti_kaina_su_pvm(self):
# #         PVM = 0.21
# #         kaina_su_pvm = self.kaina + (self.kaina * PVM)
# #         print(f"{self.pavadinimas}: kaina su PVM: {kaina_su_pvm:.2f} EUR")
# #
# #     def prekes_informacija(self):
# #         print(f"Prekes kodas: {self.prekes_kodas}, pavadinimas: {self.pavadinimas}, kaina be PVM: {self.kaina: .2f} EUR")
# #
# #     def keisti_kaina(self, nauja_kaina):
# #         self.kaina = nauja_kaina
# #         print(f'{self.pavadinimas}: nauja kaina {self.kaina:.2f} EUR')
# #
# #     def pavadinimo_keitimas(self, naujas_pavadinimas):
# #         self.pavadinimas = naujas_pavadinimas
# #         print(f'Prekes.pavadinimas pakeistas i {self.pavadinimas}')
# #
# # preke = Preke("12353123", "Knyga", 13.54)
# # preke.atspausdinti_kaina_su_pvm()
# # preke.prekes_informacija()
# # preke.keisti_kaina(12.99)
# # preke.atspausdinti_kaina_su_pvm()
# # preke.pavadinimo_keitimas("Knyga Python pradmenys")
# # preke.prekes_informacija()
# # # Sukurkite klasę Mokytojas, kuri turėtų atributus vardas ir dalykas.
# # # Pridėkite metodą atspausdinti_info, kuris atspausdintų mokytojo vardą ir dalyką.
# # # Pridėkite metodą sveikintis_su_mokiniais;
# # # Pridėkite metodą pakeisti_dalyka;
# # # Pridėkite metodą pridėti klasę;
# # # Pridėkite metodą visos_klases;
# #
# # class Mokytojas:
# #     def __init__(self, vardas, dalykas):
# #         self.vardas = vardas
# #         self.dalykas = dalykas
# #         self.klases = []
# #
# #     def atspausdinti_info(self):
# #         print(f"Mokytojo vardas: {self.vardas}, Dalykas: {self.dalykas}")
# #
# #     def sveikintis_su_mokiniais(self):
# #         print(f"Mokytojas {self.vardas} sveikinasi su mokiniais!")
# #
# #     def pakeisti_dalyka(self, naujas_dalykas):
# #         self.dalykas = naujas_dalykas
# #         print(f"Mokytojo {self.vardas} dalykas, pakeistas i {naujas_dalykas}")
# #
# #     def pakeisti_varda(self, naujas_vardas):
# #         self.vardas = naujas_vardas
# #         print(f"Mokytojas keiciamas i naujaji mokytoja vardu {naujas_vardas}")
# #
# #     def prideti_klase(self, klases_pavadinimas):
# #         self.klases.append(klases_pavadinimas)
# #         print(f"{self.vardas} pridejo nauja klase: {klases_pavadinimas}")
# #
# #     def visos_klases(self):
# #         if self.klases:
# #             print(f"{self.vardas} desto siose klasese: {','.join(self.klases)}")
# #         else:
# #             print(f"{self.vardas} siuo metu nedesto jokiose klasese")
# #
# # mokytojas = Mokytojas("Petras", "Fizika")
# # mokytojas.atspausdinti_info()
# # mokytojas.sveikintis_su_mokiniais()
# # mokytojas.pakeisti_dalyka("Informatika")
# # mokytojas.pakeisti_varda("Antanas")
# # mokytojas.prideti_klase("5b")
# # mokytojas.visos_klases()
#
# # Sukurkite paprasta bibliotekos valdymo sistema, naudojant objektinį programavimą (OOP) su Python:
# #
# # Klasė Book: Atspindi knygą bibliotekoje.
# # Turi pagrindines savybes: title (pavadinimas), author (autorius),
# # isbn (tarptautinis standartinis knygos numeris) ir checked_out (pažymėjimas, ar knyga išduota).
# # Taip pat turi metodus check_out (išduoti knygą) ir check_in (grąžinti knygą).
# #
# # Klasė Member: Atspindi bibliotekos narį. Turi savybes name (vardas), member_id (nario ID)
# # ir books_checked_out (išduotų knygų sąrašas). Metodai borrow_book (pasiskolinti knygą)
# # ir return_book (grąžinti knygą) leidžia nariui atitinkamai pasiskolinti ar grąžinti knygas.
# #
# # Klasė Library: Atspindi pačia biblioteką. Laiko knygų (books) ir narių (members) sąrašus,
# # turi metodus add_book (pridėti knygą), add_member (pridėti narį)
# # ir display_available_books (rodyti prieinamas knygas),
# # kurie leidžia valdyti bibliotekos turimų knygų ir narių sąrašus bei rodyti,
# # kurios knygos šiuo metu yra nepaimtos.
# #
# # class Book:
# #     def __init__(self, title, author, isbn):
# #         self.title = title
# #         self.author = author
# #         self.isbn = isbn
# #         self.checked_out = False
# #
# #     def check_out(self, member):
# #         if not self.checked_out:
# #             self.checked_out = True
# #             print(f"{self.title} knyga buvo isduota {member.name}")
# #         else:
# #             print(f"{self.title} knyga jau isduota")
# #
# #     def check_in(self):
# #         self.checked_out = False
# #         print(f"{self.title} knyga buvo grazinta")
# #
# # class Member:
# #     def __init__(self, name, member_id):
# #         self.name = name
# #         self.member_id = member_id
# #         self.books_checked_out = []
# #
# #     def borrow_book(self, book):
# #         if not book.checked_out:
# #             book.check_out(self)
# #             self.books_checked_out.append(book)
# #         else:
# #             print(f"{book.title} knyga yra neprieinama")
# #
# #     def return_book(self, book):
# #         book.check_in()
# #         self.books_checked_out.remove(book)
# #
# # class Library:
# #     def __init__(self):
# #         self.books = []
# #         self.members = []
# #
# #     def add_book(self, book):
# #         self.books.append(book)
# #
# #     def add_member(self, member):
# #         self.members.append(member)
# #
# #     def display_available_books(self):
# #         available_books = [book for book in self.books if not book.checked_out]
# #         for book in available_books:
# #             print(f"{book.title} by book author {book.author}")
# #
# # library = Library()
# # book1 = Book("Harry Potter", "Antanas", 152)
# # book2 = Book("Menulis", "Tadas", 634)
# # book3 = Book("Blinda", "Kestas", 81)
# # library.add_book(book1)
# # library.add_book(book2)
# # library.add_book(book3)
# # member1 = Member("Vilius", 877)
# # member2 = Member("Tomas", 878)
# # member3 = Member("Rokas", 879)
# # library.add_member(member1)
# # library.add_member(member2)
# # library.add_member(member3)
# # Sukurkite paprasta ligoninės valdymo sistemą:
# #
# # Klasės ir Metodai:
# #
# # Ligoninė (Hospital): Ši klasė atspindi ligoninę.
# # Ji turi metodą prideti_skyriu, kuris prideda naują skyrių ligoninėje,
# # ir rodyti_skyrius, kuris atspausdina visų ligoninės skyrių sąrašą.
# #
# # Skyrius (Department): Atspindi ligoninės skyrių. Skyriuje yra medikai ir pacientai.
# # Yra metodai prideti_medika ir prideti_pacienta.
# #
# # Medikas (MedicalStaff): Atspindi mediką. Medikai turi vardą, specialybę ir ID.
# # Metodas atspausdinti_informacija rodo mediko informaciją.
# #
# # Pacientas (Patient): Atspindi pacientą. Pacientai turi vardą, asmens kodą ir būklę.
# # Metodas atspausdinti_informacija rodo paciento informaciją.
# #
# # class Skyrius:
# #     def __init__(self, pavadinimas):
# #         self.pavadinimas = pavadinimas
# #         self.medikai = []
# #         self.pacientai = []
# #
# #     def prideti_medika(self, medikas):
# #         self.medikai.append(medikas)
# #
# #     def prideti_pacienta(self, pacientas):
# #         self.pacientai.append(pacientas)
# #
# #     def skyriaus_informacija(self):
# #         print(f"{self.pavadinimas} skyrius: Medikai: {len(self.medikai)}, Pacientai: {len(self.pacientai)}")
# #
# # class Medikas:
# #     def __init__(self, mediko_vardas, specialybe, mediko_id):
# #         self.mediko_vardas = mediko_vardas
# #         self.specialybe = specialybe
# #         self.mediko_id = mediko_id
# #
# #     def atspausdinti_minformacija(self):
# #         print(f" Mediko ID: {self.mediko_id}, Mediko vardas: {self.mediko_vardas}, Specialybe: {self.specialybe}")
# #
# # class Pacientas:
# #     def __init__(self, paciento_vardas, asmens_kodas, busena):
# #         self.paciento_vardas = paciento_vardas
# #         self.asmens_kodas = asmens_kodas
# #         self.busena = busena
# #
# #     def atspausdinti_pinformacija(self):
# #         print(f"Paciento vardas: {self.paciento_vardas}, Asm. Kodas: {self.asmens_kodas}, Busena: {self.busena}")
# #
# # class Ligonine:
# #     def __init__(self):
# #         self.skyriu_sarasas = []
# #
# #     def prideti_skyriu(self, skyriaus_pavadinimas):
# #         skyrius = Skyrius(skyriaus_pavadinimas)
# #         self.skyriu_sarasas.append(skyrius)
# #
# #     def rodyti_skyrius(self):
# #         for skyrius in self.skyriu_sarasas:
# #             skyrius.skyriaus_informacija()
# #
# # ligonine = Ligonine()
# # kardiologijos_skyrius = Skyrius("Kardiologija")
# # chirurgijos_skyrius = Skyrius("Chirurgija")
# #
# # ligonine.prideti_skyriu("kardiologijos_skyrius")
# # ligonine.prideti_skyriu("chirurgijos_skyrius")
# #
# # medikas_jonas = Medikas("Jonas", "Kardiologas", 2)
# # medikas_petras = Medikas("Petras", "Chirurgas", 3)
# # pacientas_antanas = Pacientas("Antanas", "3543156", "Sergantis")
# #
# # chirurgijos_skyrius.prideti_medika(medikas_petras)
# # kardiologijos_skyrius.prideti_medika(medikas_jonas)
# # kardiologijos_skyrius.prideti_pacienta(pacientas_antanas)
# #
# # ligonine.rodyti_skyrius()
#
# class Department:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.medikai = []
#         self.pacientai = []
#
#     def prideti_medika(self, medikas):
#         self.medikai.append(medikas)
#
#     def prideti_pacienta(self, pacientas):
#         self.pacientai.append(pacientas)
#
#     def atspausdinti_informacija(self):
#         print(f"{self.pavadinimas} skyrius: Medikai: {len(self.medikai)}, Pacientai: {len(self.pacientai)}")
#
# class MedicalStaff:
#     def __init__(self, vardas, specialybe, id):
#         self.vardas = vardas
#         self.specialybe = specialybe
#         self.id = id
#
#     def atspausdinti_informacija(self):
#         print(f"Medikas: {self.vardas}, Specialybė: {self.specialybe}, ID: {self.id}")
#
# class Patient:
#     def __init__(self, vardas, asmens_kodas, bukle):
#         self.vardas = vardas
#         self.asmens_kodas = asmens_kodas
#         self.bukle = bukle
#
#     def atspausdinti_informacija(self):
#         print(f"Pacientas: {self.vardas}, Asmens kodas: {self.asmens_kodas}, Būklė: {self.bukle}")
#
# class Hospital:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.skyriai = []
#
#     def prideti_skyriu(self, skyrius):
#         self.skyriai.append(skyrius)
#
#     def rodyti_skyrius(self):
#         for skyrius in self.skyriai:
#             skyrius.atspausdinti_informacija()
#
#
# ligonine = Hospital("Centrinė Ligoninė")
# kardiologijos_skyrius = Department("Kardiologija")
# chirurgijos_skyrius = Department("Chirurgijos skyrius")
# ligonine.prideti_skyriu(kardiologijos_skyrius)
# ligonine.prideti_skyriu(chirurgijos_skyrius)
# medikas_jonas = MedicalStaff("Jonas Jonaitis", "Kardiologas", "001")
# medikas_antanas = MedicalStaff("Antanas", "Chirurgas", "002")
#
# pacientas_petras = Patient("Petras Petraitis", "290120-12345", "Sergantis")
# kardiologijos_skyrius.prideti_medika(medikas_jonas)
# chirurgijos_skyrius.prideti_medika(medikas_antanas)
# kardiologijos_skyrius.prideti_pacienta(pacientas_petras)
#
# ligonine.rodyti_skyrius()
# Sąskaita (Account): Atspindi banko sąskaitą. Turi atributus account_number (sąskaitos numeris),
# owner (savininkas), ir balance (likutis). Metodai deposit (įnešti pinigus),
# withdraw (išsiimti pinigus), ir transfer (pervesti pinigus) leidžia valdyti sąskaitos lėšas.
#
# Bankas (Bank): Atspindi banką. Turi metodą create_account (sukurti sąskaitą),
# kuris leidžia klientams atidaryti naujas sąskaitas, ir find_account (rasti sąskaitą),
# leidžiantį rasti sąskaitą pagal jos numerį.
#
# import csv
#
# class Account:
#     def __init__(self, owner, account_number, initial_balance=0.0):
#         self.owner = owner
#         self.account_number = account_number
#         self.initial_balance = initial_balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.initial_balance += amount
#             print(f"{amount} Eur inesta i {self.account_number} saskaita. Naujas likutis: {self.initial_balance} Eur")
#         else:
#             print("Inesama suma negali buti maziau uz nuli")
#
#     def withdraw(self, amount):
#         if amount > self.initial_balance:
#             print("Nepakankamas likutis saskaitoje")
#         else:
#             self.initial_balance -= amount
#             print(f"{amount} Eur issimta is {self.account_number} saskaitos. Naujas likutis: {self.initial_balance} Eur")
#
#     def transfer(self, target_account, amount):
#         if amount <= self.initial_balance:
#             self.initial_balance -= amount
#             target_account.initial_balance += amount
#             print(f"{amount} buvo pervesta i {target_account.account_number}")
#         else:
#             print("Nepakankamas liktutis saskaitoje")
#
# class Bank:
#     def __init__(self):
#         self.accounts = {}
#
#     def create_account(self, account_number, owner):
#         if account_number in self.accounts:
#             print("Saskaitos numeris jau egzistuoja")
#         else:
#             self.accounts[account_number]=Account(owner, account_number)
#             print(f"Saskaita {account_number} sukurta sekmingai!")
#
#     def find_account(self, account_number):
#         return self.accounts.get(account_number, None)
#
#     def save_accounts_info(self, file_name):
#         with open(file_name, "w", newline="") as file:
#             csv_writer = csv.writer(file)
#             csv_writer.writerow(['Saskaitos numeris', 'Savininkas', 'Likutis'])
#             for account_number, account in self.accounts.items():
#                 csv_writer.writerow([account_number, account.owner, account.initial_balance])
#             print(f"Saskaitu informacija issaugota faile {file_name}")
#
#     def meniu(self):
#         while True:
#             print("Sveiki atvyke i banko valdymo sistema!")
#             print("1. Sukurti nauja saskaita")
#             print("2. Inesti pinigu")
#             print("3. Issimti pinigus")
#             print("4. Pervesti pinigus")
#             print("5. Rodyti saskaitu informacija")
#             print("6. Issaugoti saskaitu informacija i faila")
#             print("0. Iseiti")
#
#             pasirinkimas = input("Pasirinkite veiksma:")
#             if pasirinkimas == '1':
#                 account_number = input("Iveskite saskaitos numeri: ")
#                 owner = input("Iveskite savininko varda ir pavarde: ")
#                 self.create_account(account_number, owner)
#             elif pasirinkimas == '2':
#                 account_number = input("Iveskite saskaitos numeri: ")
#                 account = self.find_account(account_number)
#                 amount = float(input("Iveskite inesamos sumos dydi: "))
#                 if account:
#                     account.deposit(amount)
#                 else:
#                     print("Saskaita nerasta")
#
#             elif pasirinkimas == '3':
#                 account_number = input("Iveskite saskaitos numeri: ")
#                 account = self.find_account(account_number)
#                 amount = float(input("Iveskite norima isimti pinigu suma: "))
#                 if account:
#                     account.withdraw(amount)
#                 else:
#                     print("Saskaita nerasta")
#             elif pasirinkimas == '4':
#                 from_account_number = input("Iveskite siuntejo saskaitos numeri: ")
#                 to_account_number = input("Iveskite gavejo saskaitos numeri: ")
#                 amount = float(input("Iveskite pervedamos sumos dydi: "))
#                 from_account = self.find_account(from_account_number)
#                 to_account = self.find_account(to_account_number)
#                 if from_account and to_account:
#                     from_account.transfer(to_account, amount)
#                 else:
#                     print("Viena arba abi saskaitos nerastos")
#             elif pasirinkimas == '5':
#                 account_number = input("Iveskite saskaitos numeri: ")
#                 account = self.find_account(account_number)
#                 for account_number, account in self.accounts.items():
#                     print(f"Saskaita {account_number} priklauso {account.owner} ir likutis {account.initial_balance}")
#             elif pasirinkimas == '6':
#                 file_name = input("Iveskite failo pavadinima.csv ")
#                 self.save_accounts_info(file_name)
#             elif pasirinkimas == '0':
#                 print("Programa isjungiama")
#                 break
#             else:
#                 print("Neteisingas pasirinkimas, bandykite dar karta")
#
# bankas = Bank()
# bankas.meniu()
# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = {
#     'FirstName': ["Jonas", "Ona", "Antanas", "Petras", "Laura", "Linas"],
#     'LastName': ["Jonaitis", "Micke", "Antoninis", "Petrinis", "Simonyte", "Lininis"],
#     'Age': [23,32,28,16,21,16],
#     'City': ["Vilnius", "Plunge", "Klaipeda", "Siauliai", "Kaunas", "Anyksciai"]}
#
# df = pd.DataFrame(data)
#
# df['Grade'] = [5,4,8,10,7,8]
# df['Full name'] = df['FirstName'] + " " + df['LastName']
# df.drop(['FirstName', 'LastName'], axis=1, inplace=True)
# df = df[['Full name'] + [col for col in df.columns if col not in ['Full name', 'City']] + ['City']]
#
# colors = ['green' if x >= 8 else 'cornflowerblue' if x >= 7 else 'red' for x in df['Grade']]
# ax = df.plot(kind='bar', x='Full name', y='Grade', color=colors, legend=False)
# ax.set_xticklabels(df['Full name'], rotation=45, ha='right')
# plt.subplots_adjust(bottom=0.3)
# plt.show()
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# webdriver_path = "C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe"
# service = Service(webdriver_path)
# service.start()
# driver = webdriver.Chrome(service=service)
# data = []
#
# for i in range(1,5):
#     url = f"https://coinmarketcap.com/?page={i}"
#     driver.get(url)
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window. scrollBy(0,300);")
#         time.sleep(1)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height
#
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     table = soup.find('table')
#
#     if table:
#         for row in table.find("tbody").find_all("tr"):
#             columns = row.find_all("td")
#             if len(columns) >= 7:
#                 crypto_data = {
#                     'Name': columns[2].text.strip(),
#                     'Price': columns[3].text.strip(),
#                     '1h %': columns[4].text.strip(),
#                     '24h %': columns[5].text.strip(),
#                     'Market Cap': columns[6].text.strip(),
#                     'Volume(24h)': columns[7].text.strip(),
#                     'Circulating Supply': columns[8].text.strip(),
#                 }
#                 data.append(crypto_data)
#
# driver.quit()
# df = pd.DataFrame(data)
# df.to_csv("crypto.csv", index = False)
import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# masyvas = np.array([1, 2, 3, 4])
# vidurkis = np.mean(masyvas)
# print(vidurkis)

# masyvas1 = np.array([1,2])
# masyvas2 = np.array([3,4])
# masyvo_sujungimas = np.concatenate((masyvas1,masyvas2), axis=0)
# print(masyvo_sujungimas)
# masyvas = np.array([[1,2], [3,4]])
# print(masyvas)

# dates = pd.date_range(start='2023-03-01', end='2023-03-31')
# prices = np.random.randint(100,200, size=len(dates))
# stock_data = pd.DataFrame({'Date': dates, 'Price': prices})
#
# vidutine_kaina = np.mean(stock_data['Price'])
# maziausia_kaina = np.min(stock_data['Price'])
# didziausia_kaina = np.max(stock_data['Price'])
# kainos_nuokrypis = np.std(stock_data['Price'])
# mediana = np.median(stock_data['Price'])

# print(f"Vidutine kaina: {vidutine_kaina}")
# print(f"Maziausia kaina: {maziausia_kaina}")
# print(f"Didziausia kaina: {didziausia_kaina}")
# print(f"Kainos nuokrypis: {kainos_nuokrypis}")
# print(f"Mediana: {mediana}")

# market_index_prices = np.random.randint(2000,3000, size=len(dates))
# market_data = pd.DataFrame({'Date': dates, 'Market index': market_index_prices})

# merged_data = pd.merge(stock_data, market_data, on='Date')
# print(merged_data)
# koreliacijos_skaiciavimas = merged_data['Price'].corr(merged_data['Market index'])
# print(f"Koreliacija tarp imones akciju ir rinkos indekso: {koreliacijos_skaiciavimas}")

# monthly_avg = merged_data.groupby(merged_data['Date'].dt.month)['Price'].mean()
# print('Menesio vidurkiai:')
# print(monthly_avg)
# merged_data.plot(x='Date', y=['Price', 'Market index'], title="Akciju kainos ir rinkos indeksas")
# plt.show()

# np.random.seed(0)
# data = {
#     'Amzius': np.random.randint(18, 70, 100),
#     'Ugis': np.random.normal(160, 10, 100),
#     'Svoris': np.random.normal(70, 15, 100),
#     'Fizinis aktyvumas': np.random.choice(['Zemas', 'Vidutinis', 'Aukstas'], 100),
#
# }

# sveikatos_duomenys = pd.DataFrame(data)
# print(sveikatos_duomenys)

# vidutinis_ugis = np.mean(sveikatos_duomenys['Ugis'])
# print(f"vidutinis ugis: {vidutinis_ugis}")

# amziuaus_nuokrypis = np.std(sveikatos_duomenys['Amzius'])
# print(f"Standartinis amziaus nuokrypis: {amziuaus_nuokrypis}")

# def kmi(svoris, ugis):
#     return svoris / ((ugis/100)**2)

# sveikatos_duomenys['KMI']= kmi(sveikatos_duomenys['Svoris'], sveikatos_duomenys['Ugis'])
# print(sveikatos_duomenys)

# amziaus_grupes = sveikatos_duomenys.groupby(pd.cut(sveikatos_duomenys['Amzius'],bins=[18,30,40,50,60,70]),observed=True)
# amziaus_grupes_stat = amziaus_grupes['KMI'].mean()
# print(amziaus_grupes_stat)

# plt.scatter(sveikatos_duomenys['Amzius'], sveikatos_duomenys['KMI'])
# plt.title('KMI pagal amziu')
# plt.xlabel('Amzius')
# plt.ylabel('KMI')
# plt.show()
# amziaus_grupes_stat.plot(kind='bar')
# plt.title('Vidutinis KMI pagal amziaus grupes')
# plt.xlabel('Amziaus grupes')
# plt.ylabel('Vidutinis KMI')
# plt.show()

# np.random.seed(1)

# H valanda, W savaite, M menuo, D diena, Y metai
# dates = pd.date_range(start='2023-01-01', end='2023-03-31', freq='D')
# categories = np.random.choice(['Drabuziai', 'Elektronika', 'Maistas', 'Namu reikmenys'], size=len(dates))
# prices = np.round(np.random.uniform(20,200,size=len(dates)), 2)

# sales_data = pd.DataFrame({'Data': dates, 'Kategorija': categories, 'Suma': prices})
# print(sales_data)

# avg_sale = np.mean(sales_data['Suma'])
# total_sales = np.sum(sales_data['Suma'])
# print(f'Vidutines islaidos: {avg_sale:.2f}')
# print(f'Bendra pardavimo suma: {total_sales:.2f}')

# categorie_popularity = sales_data['Kategorija'].value_counts()
# print('Produktu kategoriju populiarumas:')
# print(categorie_popularity)

# sales_data['Savaites diena'] = sales_data['Data'].dt.day_name()
# week_day_sales = sales_data['Savaites diena'].value_counts()
# print('Prikimu skaicius pagal savaites dienas:')
# print(week_day_sales)

# categorie_popularity.plot(kind='bar')
# plt.title('Produktu kategoriju populiarumas')
# plt.xlabel('Kategorija')
# plt.ylabel('Pirkimu skaicius')
# plt.xticks(rotation=0)
# plt.show()

# np.random.seed(0)
# data = {
#     'Automobiliai': np.random.randint(5, 50, 100),
#     'Keliones trukme': np.random.normal(30, 20, 100),
#     'Eismo spustis': np.random.choice(['Pikas', 'Spustciu_nera', 'Vidutiniska_spustis'], 100),
#     'Spusties trukme': np.random.normal(35, 15, 100),
#     'Miesto dalis': np.random.choice(['Miestas', 'Rajonas', 'Uzmiestis'], 100)
# }

# miesto_srautu_analize = pd.DataFrame(data)
# print(miesto_srautu_analize)

# vidutine_trukme = np.mean(miesto_srautu_analize['Keliones trukme'])
# vidutine_auto = np.mean(miesto_srautu_analize['Automobiliai'])
# print(f"Vidutine keliones trukme: {vidutine_trukme} / Vidutinis automobiliu skaicius: {vidutine_auto}")

# spusties_pikas = miesto_srautu_analize['Eismo spustis']
# spusties_trukme = np.std(miesto_srautu_analize['Spusties trukme'])
# print(f'Spusties pikas: {spusties_pikas} {spusties_trukme}')

# ----
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# times = pd.date_range(start='2023-01-01', end='2023-01-31', freq='H')
# post = np.random.choice(['Facebook', 'Instagram', 'Twitter'], size=len(times))
# like_counts = np.random.randint(1,5000,size=len(times))
# comment_counts = np.random.randint(1,1000,size=len(times))
#
# soc_data = pd.DataFrame({'Irasai': post, 'Patiktuku skaicius': like_counts, 'Komentaru skaicius':
# comment_counts, 'Irasu laikas': times})
# print(soc_data.head())
#
# # Nustatyti vidutinį įrašų, patiktukų ir komentarų skaičių.
# avg_post = np.mean(soc_data['Irasai'])
# # print(f'Vidutinis irasu skaicius: {avg_post:.2f}')
# avg_like_counts = np.mean(soc_data['Patiktuku skaicius'])
# # print(f'Vidutinis patiktuku skaicius {avg_like_counts:.2f}')
# avg_comment_counts = np.mean(soc_data['Komentaru skaicius'])
# # print(f'Vidutinis irasu skaicius: {avg_comment_counts:.2f}
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
#
# np.random.seed(0)
#
# # Duomenu kurimas
# dates = pd.date_range(start='2010-01-01', end='2020-12-31', freq='M')
# energy_consumption = np.random.normal(100, 20, size=len(dates))
# solar_energy = np.random.normal(50, 10, size=len(dates))
# wind_energy = np.random.normal(40, 15, size=len(dates))
# hydro_energy = np.random.normal(30, 5, size=len(dates))
# termo_energy = np.random.normal(60, 20, size=len(dates))
#
# energy_data = pd.DataFrame({'Data': dates, 'Suvartojimas': energy_consumption, 'Saules energija': solar_energy,
#                             'Vejo energija': wind_energy,
#                             'Hydro energija': hydro_energy, 'Termo energija': termo_energy})
# # print(energy_data.head())
#
# # Metine analize
# annual_data = energy_data.resample('Y', on = 'Data').sum()
# annual_data['Atsinaujinanti gamyba (%)'] =(annual_data['Saules energija']+annual_data['Vejo energija']+
#                                            annual_data['Hydro energija'])/annual_data['Suvartojimas']*100
# annual_data['Neatsinaujinanti gamyba (%)'] =annual_data['Termo energija']/annual_data['Suvartojimas']*100
# X = np.array(range(len(annual_data))).reshape(-1, 1)
# y = annual_data['Suvartojimas'].values
# model = LinearRegression().fit(X, y)
# future_years = np.array(range(annual_data.index.year[-1]+1, annual_data.index.year[-1]+6))
# future_consumption = model.predict(future_years.reshape(-1, 1))
#
# # Vizualizavimas
# plt.figure(figsize=(10, 6))
# plt.plot(annual_data.index.year, annual_data['Suvartojimas'], label='Faktinis suvartojimas')
# plt.plot(future_years, future_consumption, label='Prognozuojamas suvartojimas', linestyle='--')
# plt.title('Metinis energijos suvartojimas ir prognoze')
# plt.xlabel('Metai')
# plt.ylabel('Energijos suvartojimas')
# plt.legend()
# plt.show()
import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns

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
# print(df.isnull().sum())


### ANALIZE:
# Vidutinis plotas pagal vietove:
# df['Patalpu dydis'] = df['Patalpu dydis'].astype(float) # Teksa pavercia i skaiciu reiksme
# avg_area_by_location = df.groupby('Adresas')['Patalpu dydis'].mean()
# print(avg_area_by_location)

# Kainu paskirstymas pagal vietove:
df['Kaina'] = df['Kaina'].astype(float)
sns.boxplot(x='Adresas', y='Kaina', data=df)
plt.xticks(rotation=45)
plt.show()