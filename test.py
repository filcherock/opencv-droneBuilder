from promtools import ConveyerLineNamet
import time
a = ConveyerLineNamet('192.168.10.21', 8888, 'B')
a.setSpeed(150)
time.sleep(2)
a.setSpeed(0)
time.sleep(1)
a.setSpeed(250)
time.sleep(1)
a.setSpeed(0)