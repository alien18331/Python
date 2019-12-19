import modbus_tk
import modbus_tk.modbus as modbus
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp


#Create the server
            

try:
      # parameter(ip/port)
      
      server = modbus_tcp.TcpServer(address=_localip,port=_port)
      ##logger.info("enter 'quit' for closing the server")			      
      server.start()
      print ('server start..')
      slave = server.add_slave(_slaveid)
      slave.add_block('ro', cst.HOLDING_REGISTERS, 0, 100)
except: 
      print('server create fail')
      server.stop()
      server._do_exit()
      
      
# parameter (id,address,data)
slave.set_values('ro', 0 , data)

