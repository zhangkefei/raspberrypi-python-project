#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

channel = 11
i = 10

GPIO.setup(channel, GPIO.OUT)
while i:
    GPIO.output(channel, 1)
    time.sleep(0.3)
    GPIO.output(channel, 0)
    time.sleep(0.3)
    i -= 1

GPIO.cleanup()
