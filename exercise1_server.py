"""
使用udp和struct完成
     1. 从客户端循环录入学生信息
        信息包含
        id  姓名  年龄  身高

     2. 将信息打包发送给服务端
     3. 在服务端将学生信息写到一个文件中，每个
     学生的信息占1行
"""
from socket import *
import struct

# 创建数据格式对象
st = struct.Struct('i16sif')

# 创建udp套接字
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))

# 打开一个文件
f = open('student.txt', 'a')

while True:
    data, addr = s.recvfrom(1024)
    # 对数据解包操作 (1,b'Lily',15,1.66)
    data = st.unpack(data)
    # 将数据写入文件
    info = "%d   %-10s  %d   %.2f\n"%(data[0],data[1].decode().strip('\0'),data[2],data[3])
    f.write(info)
    f.flush()

f.close()
s.close()
