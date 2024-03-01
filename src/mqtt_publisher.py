# Import the MQTT client from the Paho library
import paho.mqtt.client as mqtt

# Import the necessary settings from the config module
from config.settings import (
    BROKER,
    PORT,
    DEVICE_ID,
    HYDRAULIC_RESPONSE_TOPIC,
)


# Define the MQTTPublisher class
class MQTTPublisher:
    def __init__(self):
        # Initialize the MQTT client and set up the connection and message callbacks
        self.client = mqtt.Client(client_id=DEVICE_ID)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # Initialize the connection status to False
        self.connected = False
        self.device_statuses = {}

    def on_connect(self, client, userdata, flags, rc):
        # This method is called when the client successfully connects to the MQTT broker
        if rc == 0:
            print("Connected successfully.")
            # Set the connection status to True
            self.connected = True
            # Subscribe to the status topics and the hydraulic response topic
            client.subscribe("status/#")
            client.subscribe(HYDRAULIC_RESPONSE_TOPIC)
            # Publish the initial status
        else:
            print(f"Failed to connect, return code {rc}")

    def is_connected(self):
        # Return the current connection status
        return self.connected

    def on_message(self, client, userdata, msg):
        # This method is called when a message is received
        payload = msg.payload.decode()
        # Check if the message is a response to a command
        if msg.topic == HYDRAULIC_RESPONSE_TOPIC:
            print(f"Received response on {msg.topic}: {payload}")
        elif msg.topic.startswith("status/"):
            device_id = msg.topic.split("/")[1]  # Get the device ID from the topic
            self.device_statuses[device_id] = payload  # Update the device's status
            # Handle the response here
            print(f"Received message on {msg.topic}: {payload}")
        else:
            print(f"Received message on {msg.topic}: {payload}")
            # Handle other messages here

    def publish_command(self, topic, command):
        # Publish a command message to a specified topic
        if command is not None:
            self.client.publish(topic, command)
            print(f"Published to {topic}: {command}")
        else:
            print("No command to publish.")

    def disconnect(self):
        """Gracefully disconnect the client from the MQTT broker."""
        # Stop the network loop and disconnect the client
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected successfully.")

    def run(self):
        # Connect the client to the MQTT broker and start the network loop
        try:
            self.client.connect(BROKER, PORT, 60)
            self.client.loop_start()
        except Exception as e:
            print(f"An error occurred: {e}")
