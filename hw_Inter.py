#!/usr/bin/env python

import os
from time import sleep
from OSC import OSCClient, OSCMessage
import RPi.GPIO as GPIO

print "GPIO Version"
print GPIO.VERSION

#Input Pin Defines
PIN1 = 5
PIN2 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN2, GPIO.IN)

# GPIO.setup(5, GPIO.IN)
# GPIO.setup(16, GPIO.OUT)

GPIO.setup(PIN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

client = OSCClient()
client.connect( ("127.0.0.1", 57122) )

def threadCallBack(channel):
  print "Threaded call back called"
  obj = OSCMessage("/threadcall")
  obj.append(777)
  client.send(obj)

GPIO.add_event_detect(PIN2, GPIO.FALLING, callback=threadCallBack)

def buttpressed(butt):
  obj = OSCMessage("/b/p")
  obj.append(int(butt))
  obj.append(1)
  client.send(obj)

def buttreleased(butt):
  obj = OSCMessage("/b/r")
  obj.append(2)
  client.send(obj)

try:
  GPIO.wait_for_edge(5, GPIO.FALLING)
  print "button pressed~!"

except KeyboardInterrupt:
  GPIO.cleanup() # clean up on Ctrl-C

# cleanup on normal exit
GPIO.cleanup

