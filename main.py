
from machine import Pin, PWM
from time import sleep_ms, ticks_ms
from neopixel import NeoPixel

neo = NeoPixel(Pin(5),8)

alpappir = Pin(button_pin, Pin.IN, Pin.PULL_UP)

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
def slokkva():
    Pin1.value(0)
    Pin2.value(0)
    Pin3.value(0)
while True:

    if alpappir.value() == 1:
        slokkva()
        Pin3.value(1)
        start = True
        lag()
        
    if alpappir.value() == 0:
        slokkva()
        Pin2.value(1)
        start = True
        lag()
        

