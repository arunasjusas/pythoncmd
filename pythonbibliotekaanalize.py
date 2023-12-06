import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import psycopg2
from sqlalchemy import create_engine

# Atidaro visa informacija
engine = create_engine('postgresql://postgres:Pprivatu22@localhost:5432/biblioteka2')
df = pd.read_sql('SELECT * from bibliotekos2', engine)
# print(df)
engine2 = create_engine('postgresql://postgres:Pprivatu22@localhost:5432/biblioteka')
df1 = pd.read_sql('SELECT * from bibliotekos', engine2)

merge_table = pd.merge(df, df1, on='biblioteka_id', how='outer')
analisis_result = merge_table.describe()
# print(analisis_result)
# print(merge_table.columns)

# group_data = merge_table.groupby('pavadinimas_x')
# grouped_data = group_data['autorius_x'].unique()
# print(grouped_data)

# group_data = merge_table.groupby('pavadinimas_x').agg({
#     'autorius_x': lambda x: list(set(x)),
#     'autorius_y': lambda y: list(set(y))
# })
# grouped_data = group_data['autorius_x'].unique()
# print(group_data)
merge_table['Pavadinimai']=np.where(merge_table['pavadinimas_x'].notna(), merge_table['pavadinimas_x'],
                                    merge_table['pavadinimas_y'])

group_data = merge_table.groupby('Pavadinimai').agg({
    'autorius_x': lambda x: list(set(x)),
    'autorius_y': lambda y: list(set(y))
})
print(group_data)

# Daugiausiai pasikartojantys "autoriai"
# populiariausi_aktoriai = df['autorius'].value_counts()
# print(populiariausi_aktoriai)

# df['metai'] = df['publikavimo_duomenys'].str.extract(r'(\b\d{4}\b)')
# print(df)

# Isskirstyti eilute i norimus stulpelius
# df[['leidykla', 'metai', 'miestas']] = df['publikavimo_duomenys'].str.split(' ', expand = True)
# print(df)

# Isskirstyti su regex is vienos eilutes tam tikra info pvz:
# df['leidykla'] = df['publikavimo_duomenys'].str.extract(r'([^\d]+)')
# df['metai'] = df['publikavimo_duomenys'].str.extract(r'(\d+)')
# df['miestas'] = df['publikavimo_duomenys'].str.extract(r'([^\d]+$)')
# df['metai'] = pd.to_numeric(df['metai'], errors='coerce')
# print(df)

# Isskirstyti daugiausiai pasikartojancius:
# populiariausia_leidykla = df['leidykla'].value_counts()
# print(populiariausia_leidykla)
# populiariausi_miestai = df['miestas'].value_counts()
# print(populiariausi_miestai)
# populiariausi_metai = df['metai'].value_counts()
# print(populiariausi_metai)

# Isskirto pagal metus, kokios knygos su autoriais buvo sarase
# metu_analize = df.groupby('metai').agg({'pavadinimas': 'count', 'autorius': lambda x:len(set(x))})
# metu_analize.sort_index(inplace=True)
# print(metu_analize)

# Diagrama:
# fig, ax1 = plt.subplots(figsize=(10,6))
# ax1.bar(metu_analize.index, metu_analize['pavadinimas'], color='b', alpha=0.7)
# ax2 = ax1.twinx()
# ax2.plot(metu_analize.index, metu_analize['autorius'], color='r', marker='o')
# ax1.set_xlabel('metai')
# ax1.set_ylabel('knygu skaicius', color='b')
# ax2.set_ylabel('unikalus autoriai', color='r')
# plt.title('Metu analize')
# plt.show()
