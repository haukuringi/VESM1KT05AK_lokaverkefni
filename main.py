from machine import Pin, PWM,

from time import sleep_ms, ticks_ms

hatalari_passive = PWM(Pin(14), freq=1000)
Pin2 = Pin(7)
Pin1 = Pin(8)
def lag():
    hatalari_passive.duty(553)
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
           

   

    
    
    
