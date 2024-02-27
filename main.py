from machine import Pin, PWM
from time import sleep_ms, ticks_ms
from neopixel import NeoPixel
from random import randint

neo = NeoPixel(Pin(3),8)




hatalari_passive = PWM(Pin(14), freq=1000)
#pin3=red pin2=græn pin1=gulur
Pin3 = Pin(12, Pin.OUT)
Pin2 = Pin(11, Pin.OUT)
Pin1 = Pin(10,Pin.IN, Pin.PULL_UP)

neo.fill([0, 0, 0])
neo.write()
slokkt = [0, 0, 0]

neo[0] = [0, 255, 0]
neo[1] = [255, 0, 0]
neo.write()

slokkt = [0, 0, 0]

neo_ljos = 0
neo_litur = None
start = False

while True:
    if not Pin1.value():
        #position = randint(0, 7)
        start = True
    # Loop in forward direction
    if start == True:
        start = False
        ##for _ in range(5):
        for i in range(randint(40, 60)):
            r_random = randint(0, 255)
            g_random = randint(0, 255)
            b_random = randint(0, 255)
            neo.fill(slokkt)
            neo[i % 8] = [r_random, g_random, b_random]
            neo_ljos = i % 8
            neo_litur = [r_random, g_random, b_random]
            neo.write()
            sleep_ms(25)
            
    # if ýtt er á gula takkann
        # þá setja start = True
                
    
    
    # Loop in reverse direction
#     for i in range(7, -1, -1):
#         r_random = randint(0, 255)
#         g_random = randint(0, 255)
#         b_random = randint(0, 255)
#         neo.fill(slokkt)
#         neo[i] = [r_random, g_random, b_random]
#         neo.write()
#         sleep_ms(3)
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
        

