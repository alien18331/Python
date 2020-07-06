
import cv2

cam = cv2.VideoCapture(0)

while True:
	ret, img = cam.read()
	vis = img.copy()
	cv2.imshow('Camera', vis)
	
	if(0xFF & cv2.waitKey(5)==27):
		break

cv2.destroyAllWindows()
