# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Publisher.py
import sys
import paho.mqtt.client as mqtt

MQTT_ServerIP = "10.192.249.136"
MQTT_ServerPort = 1883 #port
MQTT_TopicName = "MODE" #TOPIC name

val = str(sys.argv[1])
print(val)

mqttc = mqtt.Client("Test")
mqttc.connect(MQTT_ServerIP, MQTT_ServerPort)
mqttc.publish(MQTT_TopicName, val)
