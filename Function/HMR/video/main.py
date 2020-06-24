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

global fm

def on_connect(client, userdata, flags, rc):
	global exeName
	
	print("[{0}] Connected with result code ".format(exeName) + str(rc))
	# client.subscribe("STATUS") # singal sub
	client.subscribe([("MODE",0)]) # multi sub

def on_message(client, userdata, msg):
	# print(msg.topic + " {}".format(msg.payload.decode("utf-8")))	
	print("[{0}] Detect Algorithm Updated..!".format(sys.argv[0]))
	print("[{0}] Waiting for reallocate memory...".format(sys.argv[0]))

def Camera():
	global fm	
	try:
		while True:			
			ret, frame = cap.read()
			
			algo = Algorithm.Algorithm()
			nFrame = algo.do_func(frame)
			
			cv2.imshow('CCD LIVE', nFrame) # update frame

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
				
			print("FPS: %d" %cap.get(cv2.CAP_PROP_FPS), end = '\r')
			
	except KeyboardInterrupt:
		fm.stop_monitor()
		cap.release()
		cv2.destroyAllWindows()
		
		print("\n[{0}] End Camera..!".format(sys.argv[0]))

# start-up
if __name__ == "__main__":	
	exeName = main.__file__
				
	# camera obj
	cap = cv2.VideoCapture(camDevID) 
	if not (cap.isOpened()):
		print("[{0}] Camera Open Fail..!".format(sys.argv[0]))
		sys.exit(0)
	
	# file monitor
	fm = FileMonitor()
	fm.add_file("./Algorithm.py", Algorithm)
	fm.start()
	
	try:
		print("[{0}] ==== Camera Activated ====".format(sys.argv[0]))
		while True:			
			ret, frame = cap.read()
			
			algo = Algorithm.Algorithm()
			nFrame = algo.do_func(frame)
			
			cv2.imshow('CCD LIVE', nFrame) # update frame

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
				
			print("FPS: %d" %cap.get(cv2.CAP_PROP_FPS), end = '\r')
			
	except KeyboardInterrupt:
		fm.stop_monitor()
		print("\n[{0}] File Manager Stop..!".format(sys.argv[0]))
		cap.release()
		cv2.destroyAllWindows()
		print("[{0}] OpenCV Stop..!".format(sys.argv[0]))
		print("\n[{0}] End Process!!\n".format(sys.argv[0]))
