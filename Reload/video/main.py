#coding:utf8

import os 
import sys
import cv2
import time
import datetime
import threading
import __main__ as main

import paho.mqtt.client as mqtt

import Algorithm 
from file_monitor import FileMonitor

# parameters
camDevID = 0
exeName = ""

def on_connect(client, userdata, flags, rc):
	global exeName
	
	print("[{0}] Connected with result code ".format(exeName) + str(rc))
	# client.subscribe("STATUS")
	client.subscribe([("MODE",0)])

def on_message(client, userdata, msg):
	# print(msg.topic + " {}".format(msg.payload.decode("utf-8")))	
	print("Detect Algorithm Updated..!")
	print("Waiting for reallocate memory...")

def Camera():	
	while True:			
		ret, frame = cap.read()
		
		algo = Algorithm.Algorithm()
		nFrame = algo.do_func(frame)
		
		cv2.imshow('CCD LIVE', nFrame) # update frame

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
			
		print("FPS: %d" %cap.get(cv2.CAP_PROP_FPS), end = '\r')
		
	print("\nEnd Camera..!")
	
	cap.release()
	cv2.destroyAllWindows()

# start-up
if __name__ == "__main__":	
	exeName = main.__file__
	
	# check folder
	# if not (os.path.isdir(chkDir)):
		# os.mkdir(chkDir)
			
	# camera obj
	cap = cv2.VideoCapture(camDevID) 
	if not (cap.isOpened()):
		print("Camera Open Fail..!")
		sys.exit(0)
	
	# file monitor
	fm = FileMonitor()
	fm.add_file("./Algorithm.py", Algorithm)
	fm.start()
	
	# mqtt
	try:	
		camThr = threading.Thread(target = Camera)
		camThr.start()
		
		# subscribe
		# client = mqtt.Client()
		# client.on_connect = on_connect
		# client.on_message = on_message
		# client.connect("localhost", 1883, 60)
		# client.loop_forever()
		
	except KeyboardInterrupt:
		_stop = True
		camThr.join()
		print("End process!\n")
