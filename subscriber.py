
# import mqtt client (as an alias of mqtt)
import paho.mqtt.client as mqtt

# configure the client
MQTT_HOST = "localhost"  # actual machine is "L306-25" aka Broker
MQTT_PORT = 1883  # default MQTT port
MQTT_KEEP_ALIVE = 300  # send an "oi" message every 5 minutes
# TOPIC = "primary_topic/secondary_topic/tertiary_topic"
TOPIC = "test/ducks"  # ie channel on discord/teams
MQTT_CLIENT_NAME = "duck-down"

# start the client & connect to MQTT broker/server
client = mqtt.Client(MQTT_CLIENT_NAME)
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

# subscribe to the topic to listen to
client.subscribe(TOPIC)

# Set up the message handler
def on_message(client, userdata, message):
    original_msg = message
    msg_text = str(original_msg.payload.decode("UTF-8"))
    print(f"message received: {msg_text}")
    print(f"message Topic: {original_msg.topic}")
    print(f"message Quality of Service: {original_msg.qos}")
    print(f"message Retain? {original_msg.retain}")

# when a message arrives - display it
client.on_message = on_message

# listen forever
client.loop_forever()