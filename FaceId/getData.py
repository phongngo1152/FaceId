import cv2
import numpy as np
import mysql.connector
import os
import queryDb as db
# nhap Id va name nguoi minh muon add mit vão
id = input("Nhip Id :")
name = input("Nhap Name :")
# gyi den ham insert vao db de luu tri thong tin
db. insertOrUpdate(id, name)
# Khoi tao webcam va dit do phan giai cua no thanh 1280x720
cam = cv2. VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)
# khai tao mot doi tuong CascadeClassifier trong thu vien OpenCV vol tep tin XML chua thoog tin ve mo hinh Cascade de phat hien khuon mat tren hinh anh dau vao
detector = cv2. CascadeClassifier("./libs/haarcascade_frontalface_default.xml")
# bien nay se dugc sir dung de theo dal s& lung anh khuon nat duge chyp cho agual dung nay.
samplelNum = 0
while(True):
#doc du lieu video tu may anh va luu tru cac khung hinh trong bien img.
    ret, img = cam.read()
    # chuyen doi hinh anh mau sang do xam de don gian hoa trong viec phat hien kh
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # phat hien khuon mat trong hinh anh thang do xam
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
    # Ve mot hinh chu nhat xung quanh khuon mat duoc phat hien
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
        # tao ra mot thu muc co ten dataset neu no chua ton tai
        if not os.path.exists('dataset'):
            os.makedirs('dataset')
            
        sampleNum=sampleNum+1
    # luu khuon mat dugc phat hien vão tep dataset
        cv2. imwrite("dataSet/User."+id +'.'+ str(sampleNum) + ". jpg", gray[y:y+h,x:x+w])
        cv2. imshow('frame', img)
    # nhan phim q de ket thuc chuong trinh
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# neu so anh luu duoc du 300 anh thi xe dung chwong trinh
    elif samplelNum > 250:
        break
cam.release() 
cv2.destroyAllWindows()   