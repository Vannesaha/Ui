import paho.mqtt.client as mqtt
from config.settings import (
    BROKER,
    PORT,
    STATUS_TOPICS,
    MQTT_CLIENT_ID,
    HYDRAULIC_RESPONSE_TOPIC,
)


class MQTTPublisher:
    def __init__(self):
        self.client = mqtt.Client(client_id=MQTT_CLIENT_ID)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # self.client.on_publish = self.on_publish  # Add this line
        self.connected = False  # Add this line

    def on_publish(self, client, userdata, mid):
        print(f"Debug: Message published, mid={mid}")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected successfully.")
            self.connected = True  # Set connected to True when connected
            client.subscribe("status/#")
            client.subscribe(
                HYDRAULIC_RESPONSE_TOPIC
            )  # Subscribe to the response topic

            self.publish_messages()

        else:
            print(f"Failed to connect, return code {rc}")

    def is_connected(self):
        return self.connected  # Return the current connection status

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()

        # Check if the message is a response to a command
        if msg.topic == HYDRAULIC_RESPONSE_TOPIC:
            print(f"Received response on {msg.topic}: {payload}")
            # Add your response handling code here
        else:
            print(f"Received message on {msg.topic}: {payload}")
            # Handle regular messages
            # Your existing message handling code goes here

    def publish_messages(self):
        for topic, message in STATUS_TOPICS.items():
            self.client.publish(topic, message)
            print(f"Published to {topic}: {message}")

    def publish_command(self, topic, message):
        # print(f"Debug: Publishing to topic={topic}, message={message}")  # Debug print
        self.client.publish(topic, message)
        print(f"Published to {topic}: {message}")

    def disconnect(self):
        """Gracefully disconnect the client from the MQTT broker."""
        self.client.loop_stop()  # Stop the network loop
        self.client.disconnect()  # Disconnect the client
        print("Disconnected successfully.")

    def run(self):
        try:
            self.client.connect(BROKER, PORT, 60)
            self.client.loop_start()
        except Exception as e:
            print(f"An error occurred: {e}")
