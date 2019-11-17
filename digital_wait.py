#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

c1 = 11
c2 = 13
c3 = 15
c4 = 19
c5 = 21
c6 = 23
c7 = 29

GPIO.setup(c1, GPIO.OUT)
GPIO.setup(c2, GPIO.OUT)
GPIO.setup(c3, GPIO.OUT)
GPIO.setup(c4, GPIO.OUT)
GPIO.setup(c5, GPIO.OUT)
GPIO.setup(c6, GPIO.OUT)
GPIO.setup(c7, GPIO.OUT)

GPIO.output([c1,c2,c3,c4,c5,c6,c7], 1)
time.sleep(1)
GPIO.output([c1,c2,c3,c4,c5,c6,c7], 0)

for i in range(0, 20):
    GPIO.output(c7, 1)
    GPIO.output([c1,c2,c3,c4,c5,c6], 0)
    time.sleep(1)
    GPIO.output([c1,c2,c3,c4,c5,c6,c7], 0)
    time.sleep(1)

GPIO.output([c1,c2,c3,c4,c5,c6,c7], 0)
GPIO.cleanup()
