from cv2 import(VideoCapture, imwrite)
from ultralytics import YOLO
import RPi.GPIO as GPIO
import time

model=YOLO("best.pt")

cam_port = 0
cam = VideoCapture(cam_port)
while(True):

    in1 = 16

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(in1, GPIO.OUT)

    GPIO.output(in1, False)

    GPIO.output(in1, True)
    time.sleep(0.2)
    GPIO.output(in1, False)
    GPIO.cleanup()

    time.sleep(0.1)

    result, image = cam.read()


    imwrite("out.png", image)


    model.predict(source="out.png", show=True)
