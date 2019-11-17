#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

channel1 = 11
channel2 = 13
i = 10

GPIO.setup(channel1, GPIO.OUT)
GPIO.setup(channel2, GPIO.OUT)
while i:
    GPIO.output(channel1, 1)
    GPIO.output(channel2, 0)
    time.sleep(0.2)
    GPIO.output(channel1, 0)
    GPIO.output(channel2, 1)
    time.sleep(0.2)
    i -= 1

GPIO.output(channel1, 0)
GPIO.output(channel2, 0)
GPIO.cleanup()
