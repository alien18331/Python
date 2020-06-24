
import time
import random

import Algorithm
global Math

class Event(list):
	def __call__(self, *args):
		global Math		
				
		in1 = random.randint(0,10)
		in2 = random.randint(10,20)
		eventFunc(in1, in2)
		# result = eventFunc(in1, in2)
		# print(result)
		
def eventFunc(*args):
	global Math
	a = args[0]
	b = args[1]
	print("execute with arg {0} {1} = ".format(a, b), end="")
	print(Math.do_func(a, b))

if __name__=='__main__':
	Math = Algorithm.Math()
	
	e = Event()
	e.append(eventFunc)
	try:
		while True:
			time.sleep(5)
			e("1") # trigger
			
	except KeyboardInterrupt:
		e.remove(eventFunc)
