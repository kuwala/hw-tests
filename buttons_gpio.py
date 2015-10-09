#!/usr/bin/env python

import os
from time import sleep
from OSC import OSCClient, OSCMessage
import RPi.GPIO as GPIO

print "GPIO Version"
print GPIO.VERSION

# Set Buttons as Inputs
# 5 Buttons on pins
# Pins: 5, 6, 12, 13, 16, 19
BUT1 = 5
BUT2 = 6
BUT3 = 12
BUT4 = 13
BUT5 = 15
BUT6 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUT1, GPIO.IN)
GPIO.setup(BUT2, GPIO.IN)
GPIO.setup(BUT3, GPIO.IN)
GPIO.setup(BUT4, GPIO.IN)
GPIO.setup(BUT5, GPIO.IN)
GPIO.setup(BUT6, GPIO.IN)

# Debounceing
# - can add 0.1uF Cap across switch
# - software debounce with bouncetime= millis
# - combination of both

DEBOUNCE = 40

client = OSCClient()
client.connect( ("127.0.0.1", 57122) )

def threadCallBack(channel):
  value = GPIO.input(channel)
  if (value==0):
    print ("Pin %s is Pressed - 0" % channel)
  else:
    print ("Pin %s is Released - 1" % channel)
  sendOSCMessage(channel, value)

GPIO.add_event_detect(BUT1, GPIO.BOTH, callback=threadCallBack, bouncetime=DEBOUNCE)
GPIO.add_event_detect(BUT2, GPIO.BOTH, callback=threadCallBack, bouncetime=DEBOUNCE)
GPIO.add_event_detect(BUT3, GPIO.BOTH, callback=threadCallBack, bouncetime=DEBOUNCE)
GPIO.add_event_detect(BUT4, GPIO.BOTH, callback=threadCallBack, bouncetime=DEBOUNCE)
GPIO.add_event_detect(BUT5, GPIO.BOTH, callback=threadCallBack, bouncetime=DEBOUNCE)
GPIO.add_event_detect(BUT6, GPIO.BOTH, callback=threadCallBack, bouncetime=DEBOUNCE)

def sendOSCMessage(pin, value):
  # LOW/0 = pressed and HIGH/1 = released
  # example: "/b/p 12 0"
  if (value == 0):
    obj = OSCMessage("/b/p")
  else:
    obj = OSCMessage("/b/r")
  obj.append(int(pin))
  obj.append(int(value))
  client.send(obj)


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
  print "Ctrl-C to exit"
  while(1):
    sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup() 
  print "clean up on Ctrl-C"

GPIO.cleanup
print "clean up on normal exit"

