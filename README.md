# Smart Irrigation System (V2)

An IoT-based smart irrigation system built with **NodeMCU (ESP8266)** and integrated with **Blynk.io** for remote monitoring and control.  
This project automates watering based on soil moisture readings and provides a mobile dashboard for real-time data visualization and manual override.

---

## 🚀 Features
- **Automated Watering**: Soil moisture sensor triggers irrigation when thresholds are met.
- **Remote Monitoring**: View live sensor data via Blynk mobile app.
- **Manual Control**: Toggle irrigation pump/relay remotely.
- **Real-Time Dashboard**: Visualize soil moisture levels and irrigation status.
- **Wi-Fi Connectivity**: NodeMCU communicates with Blynk cloud over Wi-Fi.

---

## 🛠️ Hardware Requirements
- NodeMCU (ESP8266)
- Motion sensor
- Soil Moisture Sensor
- Relay Module (for pump/valve control)
- Water Pump / Solenoid Valve
- Jumper wires, breadboard, power supply

---

## 💻 Software Requirements
- [Arduino IDE](https://www.arduino.cc/en/software)
- ESP8266 Board Package
- Blynk Library (`BlynkSimpleEsp8266.h`)
- Wi-Fi credentials (SSID & Password)
- Blynk Auth Token (from Blynk app)

---

## ⚙️ Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/lewan-ski/smart-irrigation-system-with-node-mcu.git

## ⚠️ IMPORTANT
Before uploading the code to your NodeMCU, update the following values with your own Blynk Auth Token and Wi-Fi credentials:

```cpp
char auth[] = "YourAuthToken";   // Replace with your Blynk Auth Token
char ssid[] = "YourWiFiSSID";    // Replace with your Wi-Fi SSID
char pass[] = "YourWiFiPassword"; // Replace with your Wi-Fi password
