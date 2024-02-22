# Configuration settings for MQTT Broker
BROKER = "localhost"  # broker address
PORT = 1883
MQTT_CLIENT_ID = "ui_rasberryPi"  # client ID for MQTT broker
DEVICE_1 = "hydraulic"
DEVICE_2 = "pneumatic"  # for other devices
DEVICE_3 = "electrical"  # for other devices

HYDRAULIC_RESPONSE_TOPIC = (
    f"response/device/{DEVICE_1}"  # response topic for this device
)
