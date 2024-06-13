from gpiozero import AngularServo
from time import sleep

def OpenDoor():
    servo = AngularServo(18, min_angle=0, max_angle=90)
    for i in range(0,90,15): #0~90까지 15도 씩 증가
        servo.angle = i
        sleep(0.2)
def CloseDoor():
    servo = AngularServo(18, min_angle=0, max_angle=90)
    for i in range(90,0,-15):
        servo.angle = i
        sleep(0.2)
# while True:
#     try:
#         for i in range(0,90,15): #0~90까지 15도 씩 증가
#             servo.angle = i
#             sleep(0.2)
#         for i in range(90,0,-15):
#             servo.angle = i
#             sleep(0.2)
#     except KeyboardInterrupt:
#         break

