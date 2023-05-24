# Filename: publisher_v3.py
# Author:   Adrian Gould
# Purpose:  To demonstrate sending an MQTT message
#           at regular intervals in JSON format

# import mqtt client (as an alias of mqtt)
import paho.mqtt.client as mqtt

# import other things as needed
import time
from random import randrange, uniform
import json
from datetime import datetime

# configure the client
MQTT_HOST = "localhost"  # actual machine is "L306-25" aka Broker
MQTT_PORT = 1883  # default MQTT port
MQTT_KEEP_ALIVE = 300  # send an "oi" message every 5 minutes
TOPIC = "test/ducks"  # ie channel on discord/teams
MQTT_CLIENT_NAME = "duck-right"

# start the client & connect to MQTT broker/server
client = mqtt.Client(MQTT_CLIENT_NAME)
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

while True:
    temperature = uniform(10, 25)  # range of temperatures
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    data = {
        "client":MQTT_CLIENT_NAME,
        "temp": temperature,
        "date": now
    }
    json_data = json.dumps(data)
    print(f"Temperature: {temperature}")
    message_to_send = json_data
    client.publish(TOPIC, message_to_send)
    time.sleep(5)
