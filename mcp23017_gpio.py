#!/usr/bin/env python

import os, time
from subprocess import call
#call needed for shutdown
from Adafruit_MCP230xx import Adafruit_MCP230XX
from OSC import OSCClient, OSCMessage
#OSC Module from https://github.com/ptone/pyosc
import RPi.GPIO as GPIO

print "GPIO Version"
print GPIO.VERSION

OUTPUT = 0
INPUT = 1

class Buttons:
  def __init__(self, start_pin = 2, total_pins = 4):
    """ Manages button input changes on a mcp. all the pins
    must be sequential."""

    self.poll_time = 50
    self.start_pin = 0
    self.total_pins = 16
    self.pins = []
    self.pin_values = []
    self.last_pin_values = []

    for p in range(self.total_pins):
      self.last_pin_values.append(0)
      self.pin_values.append(0)
      self.pins.append(0)

    # Newer Rpi settings
    # use `$ sudo i2cdetect -y 1`
    self.mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)

  def set_up_mcp(self):
    for pin_index in range(self.total_pins):
      pin = self.start_pin + pin_index
      self.pins[pin_index] = pin
      print("Configuring MCP23017 pin %d INPUT & pullup" % pin)
      self.mcp.config(pin, INPUT)
      self.mcp.pullup(pin, 1)
  def poll(self):
    for pin_index in range(self.total_pins):
      self.last_pin_values[pin_index] = self.pin_values[pin_index]
      self.pin_values[pin_index] = self.mcp.input(self.pins[pin_index])
      #print("MCP23017 pin value: %d " % self.pin_values[pin_index] )

  def check(self):
    for pin_index in range(self.total_pins):
      if(self.last_pin_values[pin_index] > self.pin_values[pin_index]):
        print("MCP23017 pin %d down" % self.pins[pin_index] )
      elif(self.last_pin_values[pin_index] < self.pin_values[pin_index]):
        print("MCP23017 pin %d up" % self.pins[pin_index] )
    
butts = Buttons()
butts.set_up_mcp()

print ("Press crl-c to quit")
#for i in range(300):
while(1):
  butts.poll()
  butts.check()
  time.sleep(0.06)

