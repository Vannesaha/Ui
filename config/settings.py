# Configuration settings for MQTT Broker
BROKER = "localost"  # broker address
PORT = 1883
DEVICE_ID = "ui_rasberryPi"  # client ID for MQTT broker

DEVICE_1 = "hydraulic"
DEVICE_2 = "embedded"  # for other devices
DEVICE_3 = "electrical"  # for other devices

HYDRAULIC_RESPONSE_TOPIC = (
    f"response/device/{DEVICE_1}"  # response topic for this device
)
