
from shutil import copyfile

import threading
import paho.mqtt.client as mqtt

global mode
mode = 0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("MYTOPIC")
    client.subscribe([("MODE",0)]) # sub multi topic

def on_message(client, userdata, msg):
	global mode
    # print(msg.topic + " {}".format(msg.payload.decode("utf-8")))
	mode = int(msg.payload.decode("utf-8"))
	print("mode: {0}".format(mode))

def Mode():	
	while True:
		global mode
		# tmp = input("select mode:\n1. Original Mode\n2. Gray Mode\n3. HSV Mode\n4. Rotate Mode\n5. Color_Catch Mode\n")
		# mode = int(tmp)
		
		if(mode == 1):
			print("Algorithm update with original frame")
			copyfile("./Algorithm/Algorithm.color.py", "./Algorithm.py")	
			mode = 0	
		elif(mode == 2):
			print("Algorithm update with Gray transform")
			copyfile("./Algorithm/Algorithm.gray.py", "./Algorithm.py")
			mode = 0
		elif(mode == 3):
			print("Algorithm update with HSV transform")
			copyfile("./Algorithm/Algorithm.hsv.py", "./Algorithm.py")
			mode = 0
		elif(mode == 4):
			print("Algorithm update with Rotate transform")
			copyfile("./Algorithm/Algorithm.rotate.py", "./Algorithm.py")
			mode = 0
		elif(mode == 5):
			print("Algorithm update with Specific Color")
			copyfile("./Algorithm/Algorithm.color_catch.py", "./Algorithm.py")
			mode = 0		
		else:
			continue
			
		# print("input number is: {0}\n".format(mode))

modThr = threading.Thread(target = Mode)
modThr.start()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever() 
