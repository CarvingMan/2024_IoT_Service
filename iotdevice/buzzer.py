from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep



#경보
def AlretBuzzer():
    # 부저 객체 생성 (GPIO 핀 번호 지정)
    buzzer = TonalBuzzer(20)
    # 부저 울리기
    buzzer.play(Tone("C4"))  # C4(도) 음을 울립니다.
    sleep(0.5)  # 1초 동안 대기
    buzzer.stop()
    buzzer.play(Tone("D4"))  # D4(레) 음을 울립니다.
    sleep(0.5)  # 1초 동안 대기
    buzzer.stop()
    buzzer.play(Tone("E4"))  # E4(미) 음을 울립니다.
    sleep(0.5)  # 1초 동안 대기
    # 부저 멈추기
    buzzer.stop()

