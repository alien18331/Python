
import cv2

class Algorithm():
	# def __init__(self, in1 = 10, in2 = 20):
		# self.in1 = in1
		# self.in2 = in2
        
	def do_func(self, frame):
				
		result = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		return (result)
	
	# def __del__(self):
		# print("deleted")
