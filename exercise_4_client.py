from socket import *
from time import sleep

ADDR = ('127.0.0.1',8000)
filename = input(">>")

f = open(filename,'rb')

s = socket()
s.connect(ADDR)

while True:
    data = f.read(1024)
    if not data:
        sleep(0.5)
        s.send(b'##')
        break
    s.send(data)
f.close()

msg = s.recv(1024).decode()
print("检测结果:",msg)

s.close()
