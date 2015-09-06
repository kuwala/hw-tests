#!/usr/bin/env python

import os
from time import sleep
from OSC import OSCClient, OSCMessage
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(16, GPIO.OUT)

client = OSCClient()
client.connect( ("127.0.0.1", 57122) )

def buttPressed(butt):
  obj = OSCMessage("/b/p")
  obj.append(int(butt))
  obj.append(1)
  client.send(obj)

def buttReleased(butt):
  obj = OSCMessage("/b/r")
  obj.append(2)
  client.send(obj)

while True:
  if (GPIO.input(5) == False):
    os.system('echo "button 1 pressed"')
    GPIO.output(16, True)
    buttPressed(1)
  if (GPIO.input(13) == False):
    os.system('echo "button 2 pressed"')
    GPIO.output(16, False)
    buttPressed(2)
  sleep(0.01)
