import serial
import time

'''
port can vary
baudrate can vary
'''

def BTconnect(data):
    port="COM22" #it should be changed
    bluetooth=serial.Serial(port, 38400, timeout=1)
    bluetooth.flushInput()
    #start_time=time.time()
    bluetooth.write(str.encode(data[0]))
    #print(start_time-time.time())
    time.sleep(10)
    bluetooth.close()
