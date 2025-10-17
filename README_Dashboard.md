# �️ InfraSense - Real-time Multi-Sensor Dashboard

A professional real-time dashboard for monitoring health, environmental, RFID, and GPS data via MQTT. Gas tiles/charts have been removed from the UI.

## 🚀 Features

- **Real-time Monitoring**: Live updates every second
- **Health & Environment**: Heart rate, SpO2, GSR, Stress, Temperature, Humidity
- **Interactive Charts**: Real-time line charts with gradient fills for non-gas sensors
- **Modern UI**: Professional dark theme with Font Awesome icons
- **Connection Status**: MQTT connection monitoring
- **Responsive Design**: Works on desktop and mobile devices

## 📋 Prerequisites

- Python 3.7 or higher
- MQTT broker access (HiveMQ Cloud configured)
- Internet connection for map tiles

## 🔧 Installation

1. **Install Required Packages**:
   ```bash
   pip install -r dashboard_requirements.txt
   ```

2. **Configure Environment**:
   Make sure your `.env` file contains:
   ```properties
   MQTT_HOST = your-hivemq-broker-url
   MQTT_PORT = 8883
   MQTT_USERNAME = your-username
   MQTT_PASSWORD = your-password
   ```

## 🎯 Usage

### Option 1: Quick Start
```bash
python start_dashboard.py
```

### Option 2: Direct Launch
```bash
python mine_armour_dashboard.py
```

### Option 3: Test with Simulated Data
```bash
# Terminal 1: Start the dashboard
python mine_armour_dashboard.py

# Terminal 2: Start sensor simulation (for testing)
python sensor_simulator.py
```

## 📡 MQTT Topic

The dashboard subscribes to `LOKI_2004` for multi-sensor data (health, environment, GPS, RFID). Gas fields, if present, are ignored by the UI.

## 📊 Dashboard Components

### 1. **Status Cards**
- Real-time connection status
- Current health/environment metrics (no gas tiles)

### 2. **Real-time Charts**
- Charts for health and environmental metrics (no gas charts)

### 2. **Interactive Charts**
- Gas level monitoring
- Temperature and humidity trends
- Heart rate and SpO2 monitoring
- GSR conductance tracking

### 3. **GPS Map**
- Real-time location tracking
- Interactive map with zoom controls
- Location history trail

### 4. **Auto-refresh**
- Updates every second
- Maintains last 100 data points per sensor
- Smooth real-time animations

## 🔧 Configuration

### Sensor Data Format

Each sensor should publish JSON data to its respective topic:

**MQ5 Gas Sensor**:
```json
{
  "sensor": "MQ5",
  "gas_level": 45.2,
  "timestamp": "2025-01-01T12:00:00.000Z",
  "unit": "ppm"
}
```

**DHT11 Temperature/Humidity**:
```json
{
  "sensor": "DHT11", 
  "temperature": 22.5,
  "humidity": 65.3,
  "timestamp": "2025-01-01T12:00:00.000Z",
  "temp_unit": "°C",
  "humidity_unit": "%"
}
```

**GPS Location**:
```json
{
  "sensor": "GPS",
  "latitude": 40.712800,
  "longitude": -74.006000,
  "altitude": 10.5,
  "timestamp": "2025-01-01T12:00:00.000Z",
  "satellites": 8
}
```

**MAX30105 Heart Rate/SpO2**:
```json
{
  "sensor": "MAX30105",
  "heart_rate": 72,
  "spo2": 98.5,
  "red": 85000,
  "ir": 95000,
  "timestamp": "2025-01-01T12:00:00.000Z"
}
```

**GSR Sensor**:
```json
{
  "sensor": "GSR",
  "conductance": 5.2,
  "resistance": 192.3,
  "timestamp": "2025-01-01T12:00:00.000Z",
  "conductance_unit": "μS",
  "resistance_unit": "kΩ"
}
```

## 🌐 Accessing the Dashboard

1. **Local Access**: http://localhost:8050
2. **Network Access**: http://YOUR_IP:8050 (replace YOUR_IP with your machine's IP)

## 🛠️ Troubleshooting

### Common Issues:

1. **MQTT Connection Failed**:
   - Check your `.env` file configuration
   - Verify internet connection
   - Ensure HiveMQ credentials are correct

2. **No Data Appearing**:
   - Verify your sensors are publishing to correct topics
   - Check MQTT message format matches expected JSON
   - Use the sensor simulator to test dashboard functionality

3. **Dashboard Won't Start**:
   - Install missing dependencies: `pip install -r dashboard_requirements.txt`
   - Check Python version (3.7+ required)
   - Verify port 8050 is not in use

4. **Charts Not Updating**:
   - Check browser console for JavaScript errors
   - Refresh the page
   - Verify MQTT connection status

## 📱 Mobile Support

The dashboard is responsive and works on mobile devices:
- Touch-friendly interface
- Optimized layouts for small screens
- Swipe navigation on charts

## 🔒 Security

- Uses TLS encryption for MQTT connections
- Credentials stored securely in environment variables
- No data persistence (real-time only)

## 🚨 Alerts & Monitoring

The dashboard provides visual indicators for:
- MQTT connection status
- Sensor data freshness
- Abnormal readings (color-coded values)

## 📈 Performance

- Optimized for real-time updates
- Maintains rolling buffer of last 100 data points
- Efficient memory usage
- Responsive to high-frequency data

---

**Made with ❤️ for real-time sensor monitoring**
