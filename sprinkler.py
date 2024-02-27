from machine import Pin
import time

ledPin = Pin(2, Pin.OUT)
buttonPin = Pin(0, Pin.IN, pull=Pin.PULL_UP)
relayPins = [
  Pin(18, Pin.OUT)
]

def interrupter(pin):
  relayPins[0].value(not relayPins[0].value)

class Sprinkler:
  def run(self):
    print(f'Run')
    buttonPin.irq(trigger=Pin.IRQ_FALLING, handler=interrupter)
    for i in range(50):
      ledPin.value(not ledPin.value())
      print(f'ledPin.value() => {ledPin.value()}', end='\r')
      if i%2 == 0:
        time.sleep(0.1)
      else:
        time.sleep(0.4)


