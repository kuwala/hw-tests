import RPIO
from OSC import OSCClient, OSCMessage

# Set Buttons as Inputs
# 5 Buttons on pins
# Pins: 5, 6, 12, 13, 16

BUT1 = 5
BUT2 = 6
BUT3 = 12
BUT4 = 13
BUT5 = 16
BUT6 = 19

#debounce delay in ms
DEBOUNCE = 5

client = OSCClient()
client.connect( ("127.0.0.1", 57122) )

def gpio_callback(gpio_id, val):
  print("gpio %s: %s" % (gpio_id, val))

  if(val == 1):
    obj = OSCMessage("/b/r %s" % gpio_id)
  else:
    obj = OSCMessage("/b/p %s" % gpio_id)
  client.send(obj)

  

RPIO.add_interrupt_callback(BUT1, gpio_callback, debounce_timeout_ms=DEBOUNCE)
RPIO.add_interrupt_callback(BUT2, gpio_callback, debounce_timeout_ms=DEBOUNCE)
RPIO.add_interrupt_callback(BUT3, gpio_callback, debounce_timeout_ms=DEBOUNCE)
RPIO.add_interrupt_callback(BUT4, gpio_callback, debounce_timeout_ms=DEBOUNCE)
RPIO.add_interrupt_callback(BUT5, gpio_callback, debounce_timeout_ms=DEBOUNCE)
RPIO.add_interrupt_callback(BUT6, gpio_callback, debounce_timeout_ms=DEBOUNCE)

RPIO.wait_for_interrupts()

