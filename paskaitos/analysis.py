import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('crypto.csv')
for col in ['1h %', '24h %', '7d %']:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df['Price'] = df['Price'].replace('$', '').replace('...', '')
df['Market Cap'] = df['Market Cap'].replace('[$,]', '', regex=True).replace('...', '')
df['Volume(24h)'] = df['Volume(24h)'].replace('[$,]', '', regex=True).replace('...', '')


def adjust_market_cap(value):
    if 'B' in value:
        return float(value.replace('B', '')) * 1e9
    elif 'M' in value:
        return float(value.replace('M', '')) * 1e6
    else:
        return float(value)


df['Market Cap'] = df['Market Cap'].apply(adjust_market_cap)
df['Volume(24h)'] = df['Volume(24h)'].astype(float)

# print(df)

avg_24h_change = df['24h %'].mean()
max_volume = df[df['Volume(24h)']==df['Volume(24h)'].max()]
max_marketcap = df[df['Market Cap']==df['Market Cap'].max()]
sorted_df = df.sort_values(by='Market Cap', ascending=False)
print(f'Vidurkis: {avg_24h_change:.2%}')
print("")
print("Cryptocurrency with the Highest Trading Volume in the Last 24h:")
print(max_volume[['Name','Volume(24h)']])
print("")
print("Cryptocurrency with the Highest Market Cap in the Last 24h:")
print(max_marketcap[['Name', 'Market Cap']])
top_cryptos = df.nlargest(5,'Market Cap')
plt.figure(figsize=(12, 6))
plt.bar(top_cryptos['Name'], top_cryptos['Market Cap'])
plt.xlabel('Cryptocurrency')
plt.ylabel('Market Cap($)')
plt.title('Top 5 Cryptocurrencies by Market Cap')
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.3)
plt.show()