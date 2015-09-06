#!/usr/bin/env python

import os
from time import sleep
from OSC import OSCClient, OSCMessage
import RPi.GPIO as GPIO

print "GPIO Version"
print GPIO.VERSION

GPIO.setmode(GPIO.BCM)
# GPIO.setup(5, GPIO.IN)
# GPIO.setup(13, GPIO.IN)
# GPIO.setup(16, GPIO.OUT)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

client = OSCClient()
client.connect( ("127.0.0.1", 57122) )

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

