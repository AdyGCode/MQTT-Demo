
# import mqtt client (as an alias of mqtt)
import paho.mqtt.client as mqtt

# configure the client
MQTT_HOST = "localhost"  # actual machine is "L306-25" aka Broker
MQTT_PORT = 1883  # default MQTT port
MQTT_KEEP_ALIVE = 300  # send an "oi" message every 5 minutes
# TOPIC = "primary_topic/secondary_topic/tertiary_topic"
TOPIC = "test/ducks"  # ie channel on discord/teams
MQTT_CLIENT_NAME = "duck-up"

# start the client & connect to MQTT broker/server
client = mqtt.Client(MQTT_CLIENT_NAME)
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

print("Sending message")
message_to_send = "Hello"
client.publish(TOPIC, message_to_send)
