#-*- coding: UTF-8 -*-

import numpy as np # 引入numpy 用于矩阵运算
import cv2 # 引入opencv库函数

## parameter
camDevID = 0
camFPS = 120
fram_W = 1920
fram_H = 1080

cap = cv2.VideoCapture(camDevID) # video capture obj
# 0 : 默认为笔记本上的摄像头(如果有的话) / USB摄像头 webcam
# 1 : USB摄像头2
# 2 ：USB摄像头3 以此类推
# -1：代表最新插入的USB设备 

print("check camera open ？ {}".format(cap.isOpened()))

if (cap.isOpened()):
    cap.set(cv2.CAP_PROP_FPS, camFPS)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, fram_W)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, fram_H)

    cv2.namedWindow('CCD LIVE', flags = cv2.WINDOW_GUI_EXPANDED)
    #   * WINDOW_NORMAL：窗口可以放缩
    #   * WINDOW_KEEPRATIO：窗口缩放的过程中保持比率
    #   * WINDOW_GUI_EXPANDED： 使用新版本功能增强的GUI窗口

    try:
        while(True):
            # ret=True，frame是读取到的图片对象(numpy的ndarray格式)
            ret, frame = cap.read()

            if not ret:
                print("[Error] cap read fail..!")
                break

            cv2.imshow('CCD LIVE', frame) # update frame

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            print("FPS: %d" %cap.get(cv2.CAP_PROP_FPS), end = '\r')

    except KeyboardInterrupt:
        print("\nuser terminated..!\n")
        cap.release() #release videoCapture
        cv2.destroyAllWindows() # destroy all windows
