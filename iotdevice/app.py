from flask import Flask, request
from flask_cors import CORS #cors 허용
import RPi.GPIO as GPIO
import sensor
from LED import LED
import time
import post_data
import threading
from gpiozero import DistanceSensor
import servo
import post_data
import sensor
from gpiozero import Button
from signal import pause
import buzzer

#LED 클래스 인스턴스화
redLed = LED(4)
greenLed = LED(21)


#초음파 센서
disSensor = DistanceSensor(24,23)
#문이 열려있는지 확인
isOpen = False

#플라스크 라우팅
app = Flask(__name__)
CORS(app)
@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/door")
def OpenGate():
    global isOpen
    isOpen = True
    greenLed.LED_on()
    servo.OpenDoor()
    time.sleep(3)
    isOpen = False
    greenLed.LED_off()
    servo.CloseDoor()
    return "Door opened and closed successfully"  # 응답 반환

def t1_main():
    global isOpen
    while True:
        distance=disSensor.distance
        #print("Distance: %.2f m" %distance)
        # isOpen 변수에 Lock 적용
        if distance <= 1:
            #print(isOpen)
            if not isOpen:
                redLed.LED_Gradiant(1-distance)
            else:
                redLed.LED_off()
        else:
            redLed.LED_off()
        time.sleep(0.1)
#전역변수
deviceId = 0
#2번째 스레드 버튼 이벤트 처리
def t2_main():
    #버튼
    button = Button(15, pull_up=False)

    button.when_pressed = PressBtn
    pause()

def PressBtn():
    global deviceId
    temp = sensor.read_temperature()
    print("Temperature: %.2f" %temp)
    deviceId += 1
    #8000번 포트 datas로 post요청
    post_data.post_data(temp, deviceId)
    post_data.post_encoded_image()
    time.sleep(2)


#3번째 스레드 충돌감지
def t3_main():
    while True:
        try:
            vive = sensor.read_vibration()
            #print(vive)
            #진동이 느껴질시
            if vive >= 30:
                buzzer.AlretBuzzer() #경적울림
                post_data.post_emergency()#서버에 알림
                time.sleep(1)
                continue
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("Measurement stopped by User")
    
 
if __name__=="__main__":
    t1 = threading.Thread(target=t1_main)
    t1.start()
    t2 = threading.Thread(target=t2_main)
    t2.start()
    t3 = threading.Thread(target=t3_main)
    t3.start()
    app.run(host="0.0.0.0", port="5000", debug=False)