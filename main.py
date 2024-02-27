
from machine import Pin, PWM
from time import sleep_ms, ticks_ms
from neopixel import NeoPixel

neo = NeoPixel(Pin(5),8)

button_pin = 4  
led_pin = 5     


button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
led = Pin(led_pin, Pin.OUT)


hatalari_passive = PWM(Pin(14), freq=1000)
#pin3=red pin2=græn pin1=gulur
Pin3 = Pin(12, Pin.OUT)
Pin2 = Pin(11, Pin.OUT)
Pin1 = Pin(10, Pin.OUT)
def lag():
    hatalari_passive.duty(511)
    hatalari_passive.freq(90)
    sleep_ms(500)
    hatalari_passive.freq(174)
    sleep_ms(500)
    hatalari_passive.freq(90)
    sleep_ms(500)
    hatalari_passive.freq(174)
    sleep_ms(500)
    hatalari_passive.freq(90)
    sleep_ms(500)
    hatalari_passive.freq(174)
    sleep_ms(500)
    hatalari_passive.freq(90)
    sleep_ms(500)
    hatalari_passive.freq(174)
    sleep_ms(500)
    hatalari_passive.freq(90)
    hatalari_passive.duty(0)


lives = 3

while True:

    if alfpappir.value() == 1:
        slokkva()
        pin3.value(1)
        start = True
        lag()
        
        if alfpappir.value() == 0:
        slokkva()
        pin2.value(1)
        start = True
        lag()





