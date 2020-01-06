#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:27:39 2019

@author: pi
"""

# Subscriber.py
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("MYTOPIC")
    client.subscribe([("STATUS",0),("AAA",0)]) # sub multi topic

def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload))
    
    # if(msg.payload.decode("utf-8")):
        # print("OK")
    
    print(msg.topic + " {}".format(msg.payload.decode("utf-8")))
    # print(msg.topic + " {}".format(msg.payload.decode("utf-8")))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()

