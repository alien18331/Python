import sys
import logging
import threading
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp
import time

logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

# Create server
server = modbus_tcp.TcpServer() # Default port = 502
slaver = server.add_slave(1) # Slave_ID = 1

def setup():
    slaver.add_block("coil", cst.COILS, 0, 16)
    slaver.set_values("coil", 0, 16*[0])
       
def loop():
    logger.info("running...")
    # START
    server.start()
    while True:
        values = slaver.get_values("coil", 0, 8)
        #print values[0]
        str = ''
        for i in range(0, 8):
            if values[i] == 1:
                str = str + '1'
            else:
                str = str + '0'
        print  str
        # DELAY
        time.sleep(1)
        
def destory():
    logger.info("destory")
    # STOP
    server.stop()
       
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destory()