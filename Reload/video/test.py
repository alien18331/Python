#coding:utf8

import cv2
import time
import random
import threading

import Algorithm  # Can't do 'from long_op import LongOp' here, because reload only works on module level
from file_monitor import FileMonitor

#register file_monitor
fm = FileMonitor()
fm.add_file("./Algorithm.py", Algorithm)
fm.start()

cap = cv2.VideoCapture(0) 

if (cap.isOpened()):
    
    try:
        while True:
            ret, frame = cap.read()              
            if not ret:
                print("[Error] cap read fail..!")
                break
            
            algo = Algorithm.Algorithm()
            nFrame = algo.do_func(frame)
            cv2.imshow('CCD LIVE', nFrame) # update frame

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            print("FPS: %d" %cap.get(cv2.CAP_PROP_FPS), end = '\r')
            
    except KeyboardInterrupt:
        fm.stop_monitor() 
else:
    print("Camera Open Fail..!")
