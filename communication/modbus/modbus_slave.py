import sys
import struct  
import modbus_tk 
import modbus_tk.defines as mtk  
import modbus_tk.modbus  
import modbus_tk.modbus_tcp  
import time  
import random  
import string
  
logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")  
  
try:  
    #server = modbus_tk.modbus_tcp.TcpServer()  
    #这里的端口和地址都是默认的，地址是本地：  
    server = modbus_tk.modbus_tcp.TcpServer(port=502, address='127.0.0.1', timeout_in_sec=3)         
    server.start()  
    slave_1 = server.add_slave(1)  
   # slave_2 = server.add_slave(2)
    # 创建寄存器，寄存器的别名为block1，寄存器为保持寄存器（Holding_Register），寄存器起始地址为0，寄存器个数为...
    slave_1.add_block('block1', modbus_tk.defines.HOLDING_REGISTERS, 0, 11) 
    slave_1.set_values('block1', 0, 10*[0])
    slave_1.set_values('block1', 10, 255)   #PLC--第0011寄存器的初始值为高八位全为0，低八位全为1
   # slave_1.add_block('block2', modbus_tk.defines.HOLDING_REGISTERS, 2, 1)
    #给slave_1添加一个模块（模块名，只读，地址，长度）  
    valueAll = slave_1.get_values('block1', 0, 11)
    print 'valueAll: ', valueAll

    valueSet = slave_1.get_values('block1', 0, 1)   # 寄存器0000 -- 状态位初始值为全0
    print 'valueSet:  ', valueSet

    while True:       
        value = slave_1.get_values('block1', 10, 1)    
        print 'value', value

        ss = int(str(value[0]))
        print 'ss:', ss
        
    ## 判断执行机构开启操作
        if (((ss & 256) == 256) and (ss & 1) == 0):   # 256  判断“补光灯1启动”
            value1 = slave_1.get_values('block1', 0, 1)
            print 'open value1:', value1
            ss1 = int(str(value1[0]))
            slave_1.set_values('block1', 0, (ss1 | 256))
            valueSet = slave_1.get_values('block1', 0, 1)
            print 'valueSet:  ', valueSet
            
        if (((ss & 256<<1) == 256<<1) and  (ss & 1<<1) == 0):   # 512 左移一位 判断“补光灯2启动”
            value2 = slave_1.get_values('block1', 0, 1)
            print 'open value2:', value2
            ss2 = int(str(value2[0]))
            slave_1.set_values('block1', 0, (ss2 | 512))

        if (((ss & 256<<2) == 256<<2) and (ss & 1<<2) == 0):   # 1024 左移二位 判断“如气风机启动”
            value3 = slave_1.get_values('block1', 0, 1)
            print 'open value3:', value3
            ss3 = int(str(value3[0]))
            slave_1.set_values('block1', 0 , (ss3 | 1024))
                
        if (((ss & 256<<3) == 256<<3) and (ss & 1<<3) == 0):   # 2048 左移三位 判断“供液泵启动”   
            value4 = slave_1.get_values('block1', 0, 1)
            print 'open value4:', value4
            ss4 = int(str(value4[0]))
            slave_1.set_values('block1', 0 , (ss4 | 2048))
                
        if (((ss & 256<<4) == 256<<4) and (ss & 1<<4) == 0):   # 4096 左移四位 判断“回液泵启动”        
            value5 = slave_1.get_values('block1', 0, 1)
            print 'open value5:', value5
            ss5 = int(str(value5[0]))
            slave_1.set_values('block1', 0 , (ss5 | 4096))
           
    ##  判断执行机构关闭操作
        if ((ss & 1) == 1):                                    # 判断“补光灯1关闭”
            value01 = slave_1.get_values('block1', 0, 1)
            print 'close value01: ', value01
            ss01 = int(str(value01[0]))
            slave_1.set_values('block1', 0, (ss01 & (~256)))
            
        if ((ss & 1<<1) == 1<<1):                             # 判断“补光灯2关闭”
            value02 = slave_1.get_values('block1', 0, 1)
            print 'close value02: ', value02
            ss02 = int(str(value02[0]))
            slave_1.set_values('block1', 0, (ss02 & (~(256<<1))))
            
        if ((ss & 1<<2) == 1<<2):                              # 判断“如气风机关闭”
            value03 = slave_1.get_values('block1', 0, 1)
            print 'close value03: ', value03
            ss03 = int(str(value03[0]))
            slave_1.set_values('block1', 0, (ss03 & (~(256<<2))))   
            
        if ((ss & 1<<3) == 1<<3):                             # 判断“供液泵关闭”
            value04 = slave_1.get_values('block1', 0, 1)
            print 'close value04: ', value04
            ss04 = int(str(value04[0]))
            slave_1.set_values('block1', 0, (ss04 & (~(256<<3)))) 
            
        if ((ss & 1<<4) == 1<<4):                             # 判断“回液泵关闭”
            value05 = slave_1.get_values('block1', 0, 1)
            print 'close value05: ', value05
            ss05 = int(str(value05[0]))
            slave_1.set_values('block1', 0, (ss05 & (~(256<<4))))        
            
            
        value0 = slave_1.get_values('block1', 0, 1) 
        print 'value0:', value0
            
        value_all = slave_1.get_values('block1', 0, 11)
        sys.stdout.write('done: values read: %s\r\n' % (str(value_all)))
        


        print '======================'
        time.sleep(0.5)


except:  
    print '============error==========='  
finally:  
    print '=========stop========'  
    server.stop() 