
import time
import random
import logging
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp

logger = modbus_tk.utils.create_logger(name = "console", record_format = ">> %(message)s")

# Create server
server = modbus_tcp.TcpServer(address = "127.0.0.1", port = 502) # Default port = 502
slaver = server.add_slave(1) # Slave_ID = 1

def setup():
    slaver.add_block("A", cst.HOLDING_REGISTERS, 0, 16)
    # slaver.set_values("A", 0, 0)
       
def loop():
    logger.info("running...")
    
    # START
    server.start()    
    while True:
        # SET VALUE
        slaver.set_values("A", 0, random.randint(0,100))
        slaver.set_values("A", 1, random.randint(0,100))
        
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
