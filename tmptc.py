import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim


def get_lat_lon(city_name):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.geocode(city_name)
    
    if location:
        return location.latitude, location.longitude
    else:
        print("City not found!")
        exit()

city_name = input("Enter the city name: ")
CITY_LAT, CITY_LON = get_lat_lon(city_name)
print(f"Latitude: {CITY_LAT}, Longitude: {CITY_LON}")

API_KEY = "0aac8b7675b6a7fc19d6096c77eXXXXX"
URL = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={CITY_LAT}&lon={CITY_LON}&start={int((datetime.now() - timedelta(days=5)).timestamp())}&end={int(datetime.now().timestamp())}&appid={API_KEY}"


def fetch_air_quality_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data['list']
    else:
        print("Failed to fetch data.")
        return []


def calculate_aqi(pm2_5, pm10):
    if pm2_5 <= 50 and pm10 <= 50:
        return "Good"
    elif pm2_5 <= 100 or pm10 <= 100:
        return "Moderate"
    elif pm2_5 <= 150 or pm10 <= 150:
        return "Unhealthy for Sensitive Groups"
    elif pm2_5 <= 200 or pm10 <= 200:
        return "Unhealthy"
    else:
        return "Very Unhealthy"


data_list = fetch_air_quality_data()
data_records = []
for item in data_list:
    dt = datetime.utcfromtimestamp(item['dt'])
    components = item['components']
    aqi = calculate_aqi(components['pm2_5'], components['pm10'])
    data_records.append({
        'time': dt,
        'pm2_5': components['pm2_5'],
        'pm10': components['pm10'],
        'aqi': aqi
    })


df = pd.DataFrame(data_records)

fig, ax1 = plt.subplots(figsize=(10, 6))


ax1.plot(df['time'], df['pm2_5'], label='PM2.5', color='blue')
ax1.plot(df['time'], df['pm10'], label='PM10', color='orange', linestyle='--')
ax1.set_xlabel('Time (Past 5 Days)')
ax1.set_ylabel('Pollutant Concentration (µg/m³)')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()
ax2.plot(df['time'], df['aqi'], label='AQI', color='green', linestyle='-.')
ax2.set_ylabel('AQI Level')
ax2.tick_params(axis='y')

fig.suptitle(f"Air Quality Trends and AQI Analysis of {city_name}")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()

