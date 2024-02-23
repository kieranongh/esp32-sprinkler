from machine import Pin
import time

ledPin = Pin(18, Pin.OUT)

class Sprinkler:
  def loop():
    while True:
      ledPin.value(not ledPin.value())
      time.sleep(0.1)
