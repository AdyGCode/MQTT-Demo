# Filename: subscriber_v3.py
# Author:   Adrian Gould
# Purpose:  To demonstrate listening for MQTT messages
#           at regular intervals in JSON format
#
#           This uses publisher_v3 to send data in required format

# import required packages
import json

# import mqtt client (as an alias of mqtt)
import paho.mqtt.client as mqtt

# configure the client
MQTT_HOST = "localhost"  # actual machine is "L306-25" aka Broker
MQTT_PORT = 1883  # default MQTT port
MQTT_KEEP_ALIVE = 300  # send an "oi" message every 5 minutes
# TOPIC = "primary_topic/secondary_topic/tertiary_topic"
TOPIC = "test/ducks"  # ie channel on discord/teams
MQTT_CLIENT_NAME = "duck-down-again"

# start the client & connect to MQTT broker/server
client = mqtt.Client(MQTT_CLIENT_NAME)
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

# subscribe to the topic to listen to
client.subscribe(TOPIC)


# Set up the message handler
def on_message(client, userdata, message):
    original_msg = message
    msg_text = str(original_msg.payload.decode("UTF-8"))
    data = json.loads(msg_text)
    # structure of data:
    #   "client":MQTT_CLIENT_NAME,
    #   "temp": temperature,
    #   "date": now

    print(f"message received: {msg_text}")
    print(data)
    print(f"At {data['date']} it is {data['temp']}°C (client {data['client']})")
    if data["temp"] < 15:
        print("it's cold for ducks 😢")
    elif data["temp"] > 20:
        print("Roast duck anyone? 🦆")
    print(f"Topic: {original_msg.topic} QOS {original_msg.qos} ", end="")
    print(F"Retain? {original_msg.retain}")


# when a message arrives - display it
client.on_message = on_message

# listen forever
client.loop_forever()
