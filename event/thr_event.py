import threading
import time

class MyThread(threading.Thread):
	def __init__(self, signal):
		threading.Thread.__init__(self)
		# 初始化
		self.singal = signal
	def run(self):
		print ("I am %s,I will sleep ..."%self.name )
		# 進入等待狀態
		self.singal.wait()
		print ("I am %s, I awake..." %self.name )
	
if __name__ == "__main__":
	# 初始 為 False
	singal = threading.Event()
	for t in range(0, 3):
		thread = MyThread(singal)
		thread.start()
		
	print ("main thread sleep 3 seconds... ")
	time.sleep(3)
	#　喚醒含有signal,　處於等待狀態的執行緒
	singal.set()
