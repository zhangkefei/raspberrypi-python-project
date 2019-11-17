#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO as GPIO
import time

#
#     __2_
#    |     |
#  1 |     | 3
#    |__7__|
#    |     |
#  6 |     | 4
#    |__5__|
#

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

# def setp(n, status='on'):
#     if status == 'on':
#         GPIO.output(n, GPIO.HIGH)
#     else:
#         GPIO.output(n, GPIO.LOW)

#test
for i in pins + sels:
    GPIO.setup(i, GPIO.OUT)

GPIO.output(sels, 0)
GPIO.output(pins, 1)

def flush(sel, n):
    #将选择的位负极置0,未选择的置1
    GPIO.output(sels, 1)
    GPIO.output(pins, 0)

    GPIO.output(sels[sel], 0)
    #先将所有笔画置0，再将相应数字笔画置1
    digital = [pins[i - 1] for i in nums[n]]
    GPIO.output(digital, 1)

try:
    while True:
        t = time.gmtime()
        flush(3, t.tm_min / 10)
        time.sleep(0.005)
        flush(2, t.tm_min % 10)
        time.sleep(0.005)
        flush(1, t.tm_sec / 10)
        time.sleep(0.005)
        flush(0, t.tm_sec % 10)
        time.sleep(0.005)
except:
    GPIO.cleanup()
