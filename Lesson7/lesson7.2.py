import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#xml: ma trận
cascade = cv2.CascadeClassifier("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson7\\haarcascade_frontalface_alt2.xml")
mask = cv2.imread("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson7\\6.jpg")

while (True):
    ret,frame=cap.read()
    #cvt to gray
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #detectface
    faces = cascade.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        newmask = cv2.resize(mask,(w,h),cv2.INTER_CUBIC)
        frame[y:y+h,x:x+w,:]=frame[y:y+h,x:x+w,:]-newmask

    cv2.imshow("video", frame)
    key=cv2.waitKey(30)
    if key==ord('q'):
        break

#HW: giữ màu hồng filer + xác định tâm bàn tay
# viết một hàm con vẫn giữ được phần màu hồng
# contour tay -> xác định tâm
