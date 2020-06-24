# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Publisher.py
import paho.mqtt.client as mqtt

MQTT_ServerIP = "localhost"
MQTT_ServerPort = 1883 #port
MQTT_TopicName = "STATUS" #TOPIC name

mqttc = mqtt.Client("python_pub")
mqttc.connect(MQTT_ServerIP, MQTT_ServerPort)
mqttc.publish(MQTT_TopicName, "Hello World")
