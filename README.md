# 🌍 Air Quality Prediction and Monitoring System

A real-time, web-based application that allows users to fetch and visualize air quality data for any city using OpenWeatherMap's Air Pollution API. The system calculates AQI, displays pollutant levels, and shows environmental metrics like temperature and humidity in a visually engaging format.

---

## 📌 Features

- 🔎 City-based search input
- 📊 Real-time AQI and pollutant data (PM2.5, PM10, NO₂, O₃)
- 🌡️ Environmental info (Temperature & Humidity)
- 📈 Dynamic graphs using Chart.js
- 🎨 Color-coded AQI levels (Good, Moderate, Poor, etc.)
- 📱 Responsive interface for all devices
- ⚙️ Modular backend and frontend separation
- 🌐 Cross-browser compatibility

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11, Flask (optional), Requests, Geopy, Pandas
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualization**: Chart.js, Matplotlib
- **APIs**: OpenWeatherMap Air Pollution & Weather APIs
- **Tools**: VS Code, Postman, GitHub, Chrome DevTools

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/air-quality-monitor.git
cd air-quality-monitor

install required Python libraries


pip install -r requirements.txt
Add your API key

Replace YOUR_API_KEY in the Python script with your OpenWeatherMap API key.

Run the script (if Flask used)

python app.py
