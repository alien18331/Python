
from shutil import copyfile

while True:
	tmp = input("select mode:\n1. Original Mode\n2. Gray Mode\n3. HSV Mode\n4. Rotate Mode\n5. Color_Catch Mode\n")
	mode = int(tmp)
	
	if(mode == 1):
		print("Algorithm update with original frame")
		copyfile("./Algorithm/Algorithm.color.py", "./Algorithm.py")		
	elif(mode == 2):
		print("Algorithm update with Gray transform")
		copyfile("./Algorithm/Algorithm.gray.py", "./Algorithm.py")
	elif(mode == 3):
		print("Algorithm update with HSV transform")
		copyfile("./Algorithm/Algorithm.hsv.py", "./Algorithm.py")
	elif(mode == 4):
		print("Algorithm update with Rotate transform")
		copyfile("./Algorithm/Algorithm.rotate.py", "./Algorithm.py")
	elif(mode == 5):
		print("Algorithm update with Specific Color")
		copyfile("./Algorithm/Algorithm.color_catch.py", "./Algorithm.py")
	
	print("input number is: {0}\n".format(mode))
