from machine import Pin, PWM,

from time import sleep_ms, ticks_ms

hatalari_passive = PWM(Pin(14), freq=1000)
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

        if pin2.read_digital() == 1:

          

            pin1.write_digital(1)

            
            
            sleep(200)

            lives = lives -1

            

            pin1.write_digital(0)

            pin2.write_digital(0)

        else:
            lives = 3

           

   

    
    
    
