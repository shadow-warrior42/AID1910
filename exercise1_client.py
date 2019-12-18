from socket import *
import struct

ADDR = ('127.0.0.1',8888)

# 定义数据格式
st = struct.Struct('i16sif')

s = socket(AF_INET,SOCK_DGRAM)

while True:
    print("===========================")
    id = int(input('ID:'))
    name = input("Name:").encode()
    age = int(input("Age:"))
    height = float(input("Height:"))
    # 数据打包发送
    data = st.pack(id,name,age,height)
    s.sendto(data,ADDR)
