#!/usr/bin/env python
# encoding: utf-8

# 导入socket库:
import socket, time
import RPi.GPIO as GPIO

pins = [11, 13, 15, 19, 21, 23, 29] #GPIO ports
sels = [32, 36, 38, 40]             #GPIO ports to select led, there are four led lights
nums = [
        [1, 2, 3, 4, 5, 6],    #0
        [3, 4],                #1
        [2, 3, 7, 6, 5],       #2
        [2, 3, 7, 4, 5],       #3
        [1, 7, 3, 4],          #4
        [2, 1, 7, 4, 5],       #5
        [2, 1, 6, 5, 4, 7],    #6
        [2, 3, 4],             #7
        [1, 2, 3, 4, 5, 6, 7], #8
        [7, 1, 2, 3, 4, 5]     #9
    ]

GPIO.setmode(GPIO.BOARD)

#test
for i in pins + sels:
    GPIO.setup(i, GPIO.OUT)

GPIO.output(sels, 0)
GPIO.output(pins, 1)
time.sleep(1)
GPIO.output(pins, 0)

def flush(sel, n):
    #将选择的位负极置0,未选择的置1
    GPIO.output(sels, 1)
    GPIO.output(pins, 0)

    GPIO.output(sels[sel], 0)
    #先将所有笔画置0，再将相应数字笔画置1
    digital = [pins[i - 1] for i in nums[n]]
    GPIO.output(digital, 1)

def clean():
    GPIO.output(sels, 0)
    GPIO.output(pins, 0)

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('0.0.0.0', 9527))
s.listen(1)
print 'Waiting for connection...'

try:
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        print 'Accept new connection from %s:%s...' % addr
        sock.send('Welcome!')
        while True:
            data = sock.recv(1024)
            time.sleep(0.3)
            if data == 'exit' or not data:
                sock.close()
                print 'Connection from %s:%s closed.' % addr
            else:
                dig = int(data) % 10
                flush(0, dig)
                time.sleep(2)
                clean()
except:
    GPIO.cleanup()
    print 'exit'
