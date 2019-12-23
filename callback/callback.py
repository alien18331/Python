from event import *
import time
import random

#中间函数
#接受一个生成偶数的函数作为参数
#返回一个奇数
def getOddNumber(k, getEvenNumber):
    return 1 + getEvenNumber(k)
    
#起始函数，这里是程序的主函数
def main():    
	while True:
		k=random.randint(0,1000)
		
		if(k%100==0 and k>500):
			i = getOddNumber(k, double)
			print("k={0}, result={1}".format(k, i))
		elif(k%150==0 and k<500):
			i = getOddNumber(k, quadruple)
			print("k={0}, result={1}".format(k, i))
		time.sleep(0.2)
		
if __name__ == "__main__":
	main()
