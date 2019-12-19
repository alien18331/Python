
# 網絡攝像頭的視頻流解析直接使用通過http的Mjpeg是具有邊界幀信息的multipart / x-mixed-replace，
# 而jpeg數據只是以二進制形式發送。因此，實際上不需要關心HTTP協議標頭。
# 所有jpeg幀均以marker開頭，0xff 0xd8並以結尾0xff 0xd9。
# 因此，上面的代碼從http流中提取了此類幀，並將其一一解碼。像下面

# ...(http)
# 0xff 0xd8      --|
# [jpeg data]      |--this part is extracted and decoded
# 0xff 0xd9      --|
# ...(http)
# 0xff 0xd8      --|
# [jpeg data]      |--this part is extracted and decoded
# 0xff 0xd9      --|
# ...(http)

import cv2
import sys
import numpy as np
import urllib.request as urllib2

# host = "127.0.0.1:8888" 
# if len(sys.argv)>1:
    # host = sys.argv[1]
# hoststr = 'http://' + host + '/?action=stream'

hoststr = "http://127.0.0.1:8888/?action=stream"
print('Streaming ' + hoststr)

print('Print q to quit')
stream = urllib2.urlopen(hoststr)

bytes=b''
while True:
    bytes += stream.read(16384)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        
        i = cv2.imdecode(np.fromstring(jpg, dtype = np.uint8), flags = 1)
        cv2.imshow("LIVE",i)
        cv2.waitKey(1)
        
        cv2.imwrite('output.jpg', i)
        break
        
        # if cv2.waitKey(1) & 0xFF == ord('q'):
            # break
