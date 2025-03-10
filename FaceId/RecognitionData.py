import cv2
import numpy as np
from PIL import Image
import queryDB as db
from time import sleep
from gtts import gITS
import time
import os
# Khoi tao webcam va dat do phan giai cua no thanh 732x720
cam = cv2.VideoCapture(0)
cam.set(3,732)
cam.set(4,720)
# khoi tao mot doi tuong CascadeClassifier trong thu vien OpenCV voi tep tin XML chua thong tin ve mo hinh Cascade de phat hien khuon mat tren hinh anh dau vao
face_cascade=cv2.CascadeClassifier("libs/haarcascade_frontalface_default.xml")
# tao ra mot doi tuong nhan dang khuon mat bang thuat toan LBPH
recognizer = cv2.face. LBPHFaceRecognizer_create()
# dung de doc du lieu dugc trani tir tep
recognizer.read( "recognizer/trainningData.yml")
imgBackground = cv2.imread('image/background.png")
mode Type = 3
last_time_checked = time.time()
fontface = cv2. FONT_HERSHEY_SIMPLEX
folderModePath = 'image'
modePathList = os. listdir(folderModePath)
imgModeList = []
for path in modePathList:
imgModeList.append(cv2.imread(os.path. join(folderModePath, path)))
# Vong lap vo han de lay lien tuc hinh anh tu camera.
while(True):
# cam.read() la ham de doc hinh anh tu camera va luu tru vao bien frame
ret, frame = cam.read()
# dói kich thuoc cua hinh anh.
frame_resized = cv2.resize(frame, (732, 720))
imgBackground[0:0+720,0:0+732] = frame_resized
imgBackground[44:44 +634,800:800 + 414] = imgModeList[modeType]
# chuyen doi hinh anh mau sang do xam de don gian hoa trong viec phat hien khuon mat
faces=face_cascade.detectMultiscale(gray);