import numpy as np
import matplotlib as plt
import cv2

I = cv2.imread("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson6\\Image\\noise_house.jpg")
cv2.imshow("Image: ",I)
cv2.waitKey(1)
gray=cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
filter_noise=cv2.medianBlur(gray,5)
cv2.imshow("Remove noise: ", filter_noise)
cv2.waitKey(1)

#Bộ lọc Mean: trung bình cộng
#Bộ lọc Median: trung vị
#Bộ lọc Gaussian

# convert gray to binary
ret,binImage=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
cv2.imshow("binImage",binImage)
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_dilate=cv2.dilate(binImage,kernel)
img_erode=cv2.erode(binImage,kernel)
cv2.imshow("dilate",img_dilate)
cv2.imshow("erode",img_erode)
cv2.waitKey()