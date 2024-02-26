from machine import Pin
import time

ledPin = Pin(2, Pin.OUT)

class Sprinkler:
  def run(self):
    print(f'Run')
    for i in range(50):
      ledPin.value(not ledPin.value())
      print(f'ledPin.value() => {ledPin.value()}', end='\r')
      time.sleep(0.1)

