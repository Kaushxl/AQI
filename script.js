const API_KEY = "0aac8b7675b6a7fc19d6096c77e2ad85"; 

async function getAirQuality() {
    const city = document.getElementById("city").value;
    if (!city) return;

    const geocodeUrl = `https://nominatim.openstreetmap.org/search?city=${city}&format=json`;
    const geoRes = await fetch(geocodeUrl);
    const geoData = await geoRes.json();

    if (!geoData.length) {
        alert("City not found!");
        return;
    }

    const lat = geoData[0].lat;
    const lon = geoData[0].lon;

    
    const aqUrl = `https://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
    const aqRes = await fetch(aqUrl);
    const aqData = await aqRes.json();

    
    const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
    const weatherRes = await fetch(weatherUrl);
    const weatherData = await weatherRes.json();

    updateUI(city, aqData.list[0], weatherData);
}

function updateUI(city, aq, weather) {
    document.getElementById("city-name").textContent = city;
    document.getElementById("date-time").textContent = new Date().toLocaleString();
    document.getElementById("aqi-value").textContent = aq.main.aqi;
    
    const levels = ["Good", "Fair", "Moderate", "Poor", "Very Poor"];
    document.getElementById("aqi-level").textContent = levels[aq.main.aqi - 1];

    document.getElementById("temperature").textContent = `${weather.main.temp}°C`;
    document.getElementById("humidity").textContent = `${weather.main.humidity}%`;

    document.getElementById("pm2_5").textContent = `${aq.components.pm2_5} µg/m³`;
    document.getElementById("pm10").textContent = `${aq.components.pm10} µg/m³`;
    document.getElementById("o3").textContent = `${aq.components.o3} µg/m³`;
    document.getElementById("no2").textContent = `${aq.components.no2} µg/m³`;

    document.getElementById("result").classList.remove("hidden");

    updateChart(aq.components);
}

function updateChart(components) {
    const ctx = document.getElementById("airQualityChart").getContext("2d");

    if (window.airChart) window.airChart.destroy();

    window.airChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['PM2.5', 'PM10', 'O₃', 'NO₂'],
            datasets: [{
                label: 'Pollutants (µg/m³)',
                data: [components.pm2_5, components.pm10, components.o3, components.no2],
                backgroundColor: ['#ff6384', '#36a2eb', '#ffce56', '#4bc0c0']
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}
