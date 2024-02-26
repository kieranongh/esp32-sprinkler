from machine import Pin
import time

ledPin = Pin(2, Pin.OUT)

class Sprinkler:
  def loop(self):
    while True:
      ledPin.value(not ledPin.value())
      print(f'ledPin.value() => {ledPin.value()}', end='\r')
      time.sleep(0.1)

