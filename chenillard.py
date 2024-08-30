import time
from machine import Pin
led1=Pin(2,Pin.OUT)
led2=Pin(4,Pin.OUT)
led3=Pin(5,Pin.OUT)
led4=Pin(18,Pin.OUT)
led5=Pin(19,Pin.OUT)
led6=Pin(21,Pin.OUT)

leds = [led1, led2, led3, led4, led5, led6]


while True:
    for i in leds:
        i.on()
        time.sleep_ms(1000)
        i.off()
