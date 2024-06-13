import requests
import json
import cv2
from picamera2 import Picamera2


URL = 'http://172.20.10.2:8000/datas'

def post_data(data, deviceId):

    api_data = {
        'deviceId':deviceId,
        'temperature': data,
    }
    try:
        res = requests.post(URL, json=api_data)
        print(res.status_code)
        res_data = json.loads(res.text)
        print(res_data)
    except:
        print("connection failed")

def post_emergency():
    data = {
        'message': '기기 충돌 경보!! 확인바람'
    }
    try:
        res = requests.post('http://172.20.10.2:8000/emergency', json=data)
        print(res.status_code)
        res_data = json.loads(res.text)
        print(res_data)
        
    except Exception as e:
        print(f"emergency failed: {e}")


picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (640, 480)}))
picam2.start()
url2 = "http://172.20.10.2:8000/image"
content_type = 'multipart/form-data'
#headers = {'content-type': content_type}
def post_encoded_image():
    frame = picam2.capture_array()
    cv2.imwrite('images/c1.jpg', frame)
    img = open("images/c1.jpg", 'rb').read()
    file = {'image': img}
    data = {'identity': 'cyrus'}
    r = requests.post(url2, data=data, files=file)
    #print(r)
    print("captured\n")


