import os
import can
import time

can0 = can.interface.Bus(channel='can0', bustype='socketcan')

def send(id, data, ext=False):
    msg = can.Message(id, data, ext)
    can0.send(msg)
    
while(True):
    send(0x01, [0,0,0,0,1,1,1,1])
    time.sleep(0.1)


