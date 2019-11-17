#!/usr/bin/env python
# encoding: utf-8

# 导入socket库:
import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.43.162', 9527))
# 接收欢迎消息:
print s.recv(1024)
try:
    while True:
        dig = input("please input number or 'exit' : ")
        # 发送数据:
        s.send(str(dig))
except:
    print('exit')
    s.close()
