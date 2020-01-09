
import sys
import threading
import paho.mqtt.client as mqtt

from shutil import copyfile

global mode
global client

mode = 0

def on_connect(client, userdata, flags, rc):
    print("[{0}] Connected with result code ".format(sys.argv[0]) + str(rc))
    # client.subscribe("MYTOPIC")
    client.subscribe([("MODE",0)]) # sub multi topic

def on_message(client, userdata, msg):
	global mode
    # print(msg.topic + " {}".format(msg.payload.decode("utf-8")))
	mode = int(msg.payload.decode("utf-8"))
	print("[{0}] mode: {1}".format(sys.argv[0], mode))

def MQTT():	
	global client
	
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("localhost", 1883, 60)
	client.loop_forever() 

mqttThr = threading.Thread(target = MQTT)
mqttThr.start()
	
try:
	while True:
		# tmp = input("select mode:\n1. Original Mode\n2. Gray Mode\n3. HSV Mode\n4. Rotate Mode\n5. Color_Catch Mode\n")
		# mode = int(tmp)
		
		if(mode == 1):
			print("[{0}] Algorithm update with original frame".format(sys.argv[0]))
			copyfile("./Algorithm/Algorithm.color.py", "./Algorithm.py")	
			mode = 0	
		elif(mode == 2):
			print("[{0}] Algorithm update with Gray transform".format(sys.argv[0]))
			copyfile("./Algorithm/Algorithm.gray.py", "./Algorithm.py")
			mode = 0
		elif(mode == 3):
			print("[{0}] Algorithm update with HSV transform".format(sys.argv[0]))
			copyfile("./Algorithm/Algorithm.hsv.py", "./Algorithm.py")
			mode = 0
		elif(mode == 4):
			print("[{0}] Algorithm update with Rotate transform".format(sys.argv[0]))
			copyfile("./Algorithm/Algorithm.rotate.py", "./Algorithm.py")
			mode = 0
		elif(mode == 5):
			print("[{0}] Algorithm update with Specific Color".format(sys.argv[0]))
			copyfile("./Algorithm/Algorithm.color_catch.py", "./Algorithm.py")
			mode = 0		
		else:
			continue
	
except KeyboardInterrupt:
	# modThr.join()
	client.disconnect()
	print("\n[{0}] **** User terminated!! ****".format(sys.argv[0]))
