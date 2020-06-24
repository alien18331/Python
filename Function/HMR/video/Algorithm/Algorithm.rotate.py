
import cv2
import numpy as np

class Algorithm():
	# def __init__(self, in1 = 10, in2 = 20):
		# self.in1 = in1
		# self.in2 = in2
        
	def do_func(self, frame):
		
		rows, cols, channels = frame.shape
		M = cv2.getRotationMatrix2D((cols/2, rows/2), 180, 1)
		dst = cv2.warpAffine(frame, M, (cols, rows))
		
		result = dst
		return (result)
	
	# def __del__(self):
		# print("deleted")
