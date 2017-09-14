import bluetooth
import time

def BTconnect():
    bd_addr="20:16:08:01:68:65"
    port =1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr,port))
    print(sock)
    print('connected')
    data='F'
    #sock.settimeout(15.0)
    #sock.send('10\r\n')
    #data=sock.recv(1)
    data=str.encode(data)
    print(data)
    sock.send(data)
'''    
    count=0
    while (count<5):
        sock.send(data)
        #data=sock.recv(12)
        print(data)
        count+=1
'''
    sock.close()

#bluetoothconnect()

