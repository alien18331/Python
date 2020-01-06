
import cv2
import numpy as np

class Algorithm():
	# def __init__(self, in1 = 10, in2 = 20):
		# self.in1 = in1
		# self.in2 = in2
        
	def do_func(self, frame):
				
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		lower = np.array([100,20,20])
		upper = np.array([150,255,255])
		
		mask = cv2.inRange(hsv, lower, upper)
		res = cv2.bitwise_and(frame, frame, mask=mask)
		
		result = res
		return (result)
	
	# def __del__(self):
		# print("deleted")
