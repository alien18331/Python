#coding:utf8
import time
import threading

class LongOp():
    # def __init__(self):
        # super(LongOp, self).__init__()
        # self.id = id

    def run(self, x):
        y = 1000
        result = x * y
        print("(A,B) = ({0},{1}), {0} x {1} = {2}".format(x, y, result))
        return result
