import smbus
import time
import RPi.GPIO as GPIO
# GPIO 모드 설정
vibration_pin = 17 #진동센서


from numpy import log as ln
from math import e

bus = smbus.SMBus(1)
add = 0x48
CDS_AIN0 = 0x40
THERM_AIN1 = 0X41
VID_AIN2 = 0X42
POTEN_AIN3 = 0X43
# GPIO 핀 번호 설정



def read_adc(pin):
    bus.write_byte(add,pin)
    bus.read_byte(add)
    time.sleep(0.1)
    analog = bus.read_byte(add)
    return analog

def read_potentiometer():
    potentiometer = read_adc(POTEN_AIN3)
    #255일때 0v, 0일때 3.3v
    volt = (potentiometer/255*3.3)
    I = 0.01#10mA 고정
    ohm = volt/I
    return round(ohm,2)

def read_temperature():
    tmp = read_adc(THERM_AIN1)
    temp = 1000 * tmp / (256 - tmp)
    temp = 1 / (1 / 298 + 1 / 3950 * ln(temp / 10000))
    temp = temp - 273.15
    return round(temp,2)

def read_illuminance():
    state=""
    illuminance = read_adc(CDS_AIN0)
    #voltage = 3.3/1024*illuminance
    voltage =round((3.3 - (illuminance/255) * 3.3) , 2)  
    
    if(voltage <=0.8):
        state = "dark"
    elif(voltage <=1.5):
        state = "ambient"
    else:
         state = "bright"
    return voltage, state

def read_vibration():
    analog = read_adc(VID_AIN2)
    vibration = 255 - analog 
    # 아날로그 255(기본에서) 진동이 느껴질때 값(점점 낮아짐) 빼어준다.
    return vibration


def detect_vibration():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(vibration_pin, GPIO.IN)
    # 진동 센서 값 읽기
    vibration_state = GPIO.input(vibration_pin)
    if vibration_state == 0:
      return  "진동감지!"
    else:
       return "진동 없음!"
    


