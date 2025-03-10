import os
import cv2
import numpy as np
from PIL import Image
# tao ra mot doi tuong nhan dang khuon mat bang thuat toan LEPH
recognizer = cv2.face.LBPHFaceRecognizer_create()
#
# duong dan den thu muc chia hinh anh khuon mat.
path='dataSet'
# path = 'C:/Users/Admin/New folder (2)/LAP_TRINH/Python/FaceId/dataset'
# Ham nay doc coc hinh anh khuon met tir thu muc
# ham nay tra ve Id Cua nguoi trong anh va hinh anh tuong ung
def getImagesAndLabels(path):
# su dung mo-dun os de lay danh sach tat ca cac tep hinh anh trong thu muc roi lap qua tung tep da doc du lieu hinh anh
    imagePaths=[os.path. join(path, f) for f in os.listdir(path)]
    faces=[ ]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg, 'uint8')
        ID=int(os.path.split(imagePath) [-1].split(' .')[1])
        faces. append(faceNp)
        IDs.append(ID)
        cv2.waitkey(1)
    return IDs, faces
# Ham nay goi ham get ImagesAndLabelsham lay IDs va faces
def trainData():
    Ids, faces=getImagesAndLabels(path)
    # su dung phuong thic train cua recognizer
    recognizer.train(faces, np. array (Ids))
    # luu vao tep trainningData.yml
    recognizer.save( 'recognizer/trainningData.yml')
    print("train success")

trainData()
cv2.destroyAllWindows()   
