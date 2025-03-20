import BlynkLib
import dht
import machine
import time

# Define the pins
soil_pin = 0  # A0 Soil Moisture Sensor
PIR_pin = 14  # D5 PIR Motion Sensor
relay_pin = 0  # D3 Relay (Water Pump)

PIR_ToggleValue = 0
relay1State = 0

# Add your Blynk  details available on the website 
BLYNK_AUTH_TOKEN = "*************************"
ssid = "**********" #Add your wifi network name 
password = "************" #Your wifi netwrok pw

# Initialize DHT sensor
dht_sensor = dht.DHT11(machine.Pin(2))

BLYNK_TEMPLATE_ID = "TMPL6N8wiOcO_"
BLYNK_TEMPLATE_NAME = "smart irrigation system"

BLYNK = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

@BLYNK.VIRTUAL_READ(6)
def on_button_click(value):
    global PIR_ToggleValue
    PIR_ToggleValue = int(value[0])

@BLYNK.VIRTUAL_WRITE(12)
def on_relay_change(value):
    global relay1State
    relay1State = int(value[0])
    machine.Pin(relay_pin, machine.Pin.OUT).value(relay1State)

# Function to read DHT11 values
def read_dht_sensor():
    h, t = dht_sensor.read()
    if not isinstance(h, float) or not isinstance(t, float):
        print("Failed to read from DHT sensor!")
        return None, None
    return t, h

# Function to read soil moisture sensor values
def read_soil_moisture():
    value = machine.ADC(soil_pin).read()
    value = (value / 1024.0) * 100.0
    return value

# Function to read PIR sensor values
def read_pir_sensor():
    value = machine.Pin(PIR_pin, machine.Pin.IN).value()
    return value

# Function to control the water pump
def control_water_pump():
    global relay1State
    soil_moisture = read_soil_moisture()
    
    if soil_moisture < 35:  # Pump starts when moisture is below 35 
        relay1State = 1
        machine.Pin(relay_pin, machine.Pin.OUT).value(1)
    elif soil_moisture > 75:  # Pump stops when moisture is above 75
        relay1State = 0
        machine.Pin(relay_pin, machine.Pin.OUT).value(0)
    
    BLYNK.virtual_write(12, relay1State)

# Main loop
while True:
    BLYNK.run()
    control_water_pump()

    if PIR_ToggleValue == 1:
        PIR_value = read_pir_sensor()
        if PIR_value == 1:
            BLYNK.log_event("pirmotion", "WARNING! Motion Detected!")
            BLYNK.virtual_write(5, 255)
        else:
            BLYNK.virtual_write(5, 0)
    else:
        BLYNK.virtual_write(5, 0)

    t, h = read_dht_sensor()
    if t is not None and h is not None:
        BLYNK.virtual_write(0, t)
        BLYNK.virtual_write(1, h)

    soil_moisture = read_soil_moisture()
    BLYNK.virtual_write(3, soil_moisture)

    time.sleep_ms(100)
