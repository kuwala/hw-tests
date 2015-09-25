#!/usr/bin/env python2.7
# Script by Daniel
# Refrence http://RasPi.tv
# GPIO Input Threaded Callback with Interupts
# Uses pyOSC from https://github.com/ptone/pyosc

import RPi.GPIO as GPIO
from time import sleep
from OSC import OSCClient, OSCMessage

# Connect OSC Client to the loopback address
# The OSC Server must be started before this
# I think ...

cleint = OSCClient()
client.connect( ("127.0.0.1", 57122) )

def buttonPressed(butt):
  # Sends a OSC Message of what button 
  # was pressed
  obj = OSCMessage("/b/p")
  obj.append(int(butt))
  client.send(obj)
  
def buttonReleased(butt):
  # Sends a OSC Message of what button
  # was released
  obj = OSCMessage("/b/r")
  obj.append(int(butt))
  client.send(obj)



# Set pin mode to use BCM
GPIO.setmode(GPIO.BCM)

# Set Buttons as Inputs
# 5 Buttons on pins
# Pins: 5, 6, 12, 13, 16

BUT1 = 5
BUT2 = 6
BUT3 = 12
BUT4 = 13
BUT5 = 16

#debounce delay in ms
DEBOUNCE = 40

# Setup buttons as INPUTss
# I am Using external PULL UP 10k Resistors
# # Example: GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(BUT1, GPIO.IN)
GPIO.setup(BUT2, GPIO.IN)
GPIO.setup(BUT3, GPIO.IN)
GPIO.setup(BUT4, GPIO.IN)
GPIO.setup(BUT5, GPIO.IN)



def but1_pressed(channel):
  print "button 1 pressed"
  buttonPressed(BUT1)
  
def but2_pressed(channel):
  print "button 2 pressed"
  buttonPressed(BUT2)
  
def but1_released(channel):
  print "button 1 released"
  buttonReleased(BUT1)
  
def but2_released(channel):
  print "button 2 released"
  buttonReleased(BUT2)
  
  
# Add events to detect for falling edge and rising edge
# its for the button pressed down and released

GPIO.add_event_detect(BUT1, GPIO.FALLING, callback=but1_pressed, bouncetime=DEBOUNCE)
GPIO.add_event_detect(BUT1, GPIO.RISING, callback=but1_released, bouncetime=DEBOUNCE)
GPIO.add_event_detect(BUT2, GPIO.FALLING, callback=but2_pressed, bouncetime=DEBOUNCE)
GPIO.add_event_detect(BUT2, GPIO.RISING, callback=but2_released, bouncetime=DEBOUNCE)
# add same for 3 other buttons

try:
  print "Button Input is running. Press Ctrl-C to close"
  while(1):
    sleep(1)
  
except KeyboardInterrupt:
  GPIO.cleanup()          # clean up on Ctrl-C exit
GPIO.cleanup()            # clean up on normal exit







  
