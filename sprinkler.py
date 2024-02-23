from machine import Pin
import time

ledPin = Pin(18, Pin.OUT)

while True:
  ledPin.value(not ledPin.value())
  time.sleep(0.1)
