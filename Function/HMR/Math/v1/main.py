#coding:utf8

import time
import random
import threading

import long_op  # Can't do 'from long_op import LongOp' here, because reload only works on module level
from file_monitor import FileMonitor

#register file_monitor
fm = FileMonitor()
fm.add_file("long_op.py", long_op)
fm.start()

try:
    while True:
        k = random.randint(0,100)
        algo = long_op.LongOp()
        if(k%10==0):
            i=algo.run(k)
            # print("i={0}, result={1}".format(k,i))    
        # else:
            # print("i={0}, null".format(k))
        time.sleep(1)
except KeyboardInterrupt:
    fm.stop_monitor()       

# resource = threading.BoundedSemaphore(5)

# threads = []
# lock = threading.Lock()
# EXITTHREADS = False

# def start_thread():
    # while True:
        # resource.acquire()
        # print("Start new thread")
        # t = long_op.LongOp(random.randint(0,9))
        # with lock:
            # threads.append(t)
            # t.start()
        # if EXITTHREADS:
            # break

# def clear_threads():
    # while True:
        # with lock:
            # for i, ele in enumerate(threads):
                # if not ele.isAlive():
                    # threads.pop(i)
                    # resource.release()
                    # print("Release a thread")
        # time.sleep(3)
        # if EXITTHREADS:
            # break


# t1 = threading.Thread(target=start_thread)
# t2 = threading.Thread(target=clear_threads)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
