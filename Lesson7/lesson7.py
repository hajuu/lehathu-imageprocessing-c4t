import numpy as np
import cv2
import matplotlib as plt

# import image
I = cv2.imread("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson6\\Image\\shape.jpg")
cv2.imshow("shape", I)
cv2.waitKey(1)

# extract 3 channels RGB: đọc từ máy tính ra là BGR
B = I[:, :, 0]  # ":" là lấy tất cả
G = I[:, :, 1]
R = I[:, :, 2]
cv2.imshow("blue", B)
cv2.imshow("green", G)
cv2.imshow("red", R)
cv2.waitKey(1)

#
C_plus = B & G & R
cv2.imshow("newImage", C_plus)
cv2.waitKey(1)

# convert Image to binary
ret, binImage = cv2.threshold(C_plus, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("binImage", binImage)
cv2.waitKey(1)

# find contour
ret, contours, hierarchy = cv2.findContours(binImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# NONE: full contour, SIMPLE: tối giản

# Cách 1: truy xuất theo giá trị/value
# for i in contours:
#     cv2.drawContours(I,i,-1,(255,0,255),5)

# Cách 2: truy xuất theo chỉ số/index
for i in range(len(contours)):
    cv2.drawContours(I, contours, i, (255, 0, 255), 3)
    leni = cv2.arcLength(contours[i], True)
    print("len of contours:", leni)
    areai = cv2.contourArea(contours[i])
    print("area of contours:", areai)
    # approximate polygon
    nedges = cv2.approxPolyDP(contours[i], 5, True)  # epsilon: sai số
    print("polyedges:",len(nedges))
    if len(nedges)==3:
        cv2.putText(I,"triangle",(nedges[1][0][0],nedges[1][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    elif len(nedges)==4:
        cv2.putText(I,"square",(nedges[0][0][0],nedges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    else:
        cv2.putText(I, "circle", (nedges[1][0][0], nedges[0][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    M = cv2.moments(contours[i]) #tìm tâm dựa vào momen
    cx = int(M['m10']/M['m00']) #tính tổng số điểm theo x
    cy = int(M['m01']/M['m00'])
    cv2.circle(I,(cx,cy),10,(120,255,0),5)

cv2.namedWindow("Image contour",cv2.WINDOW_NORMAL)
cv2.imshow("Image contour", I)

cv2.waitKey()
