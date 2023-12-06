import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


url = 'http://www.meteo.lt/en/miestas?placeCode=Vilnius'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

weekdays = soup.find_all('span', class_='date')
temperatures = soup.find_all('span', class_='temperature')[2::2]
wind = soup.find_all('span', class_='small')[::2]

weather_data = []
for day, temp, wind in zip(weekdays, temperatures, wind):
    day_text = day.get_text().split(',')[0][:-5]
    temp_text = temp.get_text().replace('°C', '').strip()
    wind_text = wind.get_text().strip()
    wind_speed = int(wind_text.split()[0])
    weather_data.append({'Weekday': day_text, 'Temperature': int(temp_text), 'Wind Speed': wind_speed})

df = pd.DataFrame(weather_data)

max_temperature = df['Temperature'].max()
min_temperature = df['Temperature'].min()
average_temperature = df['Temperature'].mean()
df['Temp_Difference'] = df['Temperature'].diff()

X = df[['Wind Speed']]
y = df['Temperature']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
X_range = pd.DataFrame({'Wind Speed': range(int(min(X['Wind Speed'])), int(max(X['Wind Speed'])) + 1)})
y_predicted = model.predict(X_range)
plt.figure(figsize=(10, 6))
plt.scatter(df['Wind Speed'], df['Temperature'], color='blue', label='Actual Data')
plt.plot(X_range, y_predicted, color='red', label='Predicted Temperatures')

plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature vs. Wind Speed and Predicted Temperatures')
plt.legend()
plt.show()