#coding:utf8
import os
import threading
import time
import sys
import imp
import datetime

EXIT = False

class FileMonitor(threading.Thread):
    def __init__(self, file2module=None, interval=3):
        '''
        :param files: files that need to be monitored
        :param modules:  objs that needs to be reloaded when corresponding files changes
        :param interval: 
        '''
        super(FileMonitor, self).__init__()
        if not file2module:
            file2module = {}
        self._lock = threading.Lock()
        self._file2module = file2module
        self._interval = interval
        self._modified_time = {}  # file to last modified time to determine if reload is needed
        for file in self._file2module:
            self._modified_time[file] = self.get_modified_time(file)

    @staticmethod
    def get_modified_time(file):
        state = os.stat(file)
        return state.st_mtime

    def run(self):
        try:
            global EXIT
            EXIT = True
            while EXIT:
                receiveTime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                with self._lock:
                    for file in self._file2module:
                        if self.get_modified_time(file) != self._modified_time[file]:
                            # print("Detect Algorithm Updated..!")
                            print("{0} Program Memory Reallocate done!!".format(receiveTime))
                            imp.reload(self._file2module[file])
                            self._modified_time[file] = self.get_modified_time(file)
                            print("{0} Program update done!!\n".format(receiveTime))
                
                time.sleep(self._interval)
        except KeyboardInterrupt as error:
            print("KeyboardInterrupt caught")
            sys.exit(0)

    def add_file(self, file, module):
        with self._lock:
            self._file2module[file] = module
            self._modified_time[file] = self.get_modified_time(file)

    def stop_monitor(self):
        global EXIT
        EXIT = False
