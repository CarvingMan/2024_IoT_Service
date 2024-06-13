from gpiozero import PWMLED 
from time import sleep

class LED:
    
    def __init__(self, led):
        self.led = PWMLED(led)
    def LED_on(self):
        self.led.value = 1
    
    def LED_off(self):
        self.led.value = 0

    def LED_Gradiant(self, value):
        self.led.value = value

# def LED_fadeIn():
#     for i in range(0.0,1.0,)
# led = actuator(20)
# led.LED_on()