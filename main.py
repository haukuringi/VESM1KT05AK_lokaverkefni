from machine import Pin, PWM
from time import sleep_ms, ticks_ms
from neopixel import NeoPixel

neo = NeoPixel(Pin(5),8)

button_pin = 4  
led_pin = 5     


button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
led = Pin(led_pin, Pin.OUT)


hatalari_passive = PWM(Pin(14), freq=1000)
Pin2 = Pin(7, Pin.OUT)
Pin1 = Pin(8, Pin.OUT)
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

    

    while lives > 0:

        if Pin2.value() == 1:
            Pin1.value(1)
            sleep(200)
            lives = lives -1
            Pin1.value(0)
            Pin2.value(0)
            

        else:
            lives = 3
    
    if button.value() == 0:
        led.value(1)    
        lag()
       
    else:
        led.value(0)   
