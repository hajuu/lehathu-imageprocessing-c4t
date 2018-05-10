import numpy as np
import cv2

# connect webcam
cap = cv2.VideoCapture(0)
lower=np.array([0,45,62])
higher=np.array([255,203,255])

while (True):
    ret,frame = cap.read() #ret: trả về là có đọc được ảnh hay không
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    #convert to binary
    binImage=cv2.inRange(hsvImage,lower,higher)
    cv2.imshow("binImage",binImage)
    cv2.imshow("hsvImage",hsvImage)
    cv2.imshow("video",frame)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break