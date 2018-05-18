import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#xml: ma trận
cascade = cv2.CascadeClassifier("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson7\\haarcascade_frontalface_alt2.xml")
mask = cv2.imread("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson7\\6.jpg")
mask=mask.astype(float)
cv2.imshow("mask",mask)
#convert mask to binary
ret,binImage=cv2.threshold(mask,50,255,cv2.THRESH_BINARY)
# cv2.imshow("binImage",binImage)
# cv2.waitKey()
binImage=binImage.astype(float)/255
mask1=cv2.multiply(binImage,mask)
cv2.imshow("mask1",mask1)
cv2.waitKey()

while (True):
    ret,frame=cap.read()
    #cvt to gray
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #detectface
    faces = cascade.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        newmask = cv2.resize(mask1,(w,h),cv2.INTER_CUBIC)
        frame[y:y+h,x:x+w,:]=frame[y:y+h,x:x+w,:]-newmask

    cv2.imshow("video", frame)
    key=cv2.waitKey(30)
    if key==ord('q'):
        break

#HW: giữ màu hồng filer + xác định tâm bàn tay
# viết một hàm con vẫn giữ được phần màu hồng
# contour tay -> xác định tâm
