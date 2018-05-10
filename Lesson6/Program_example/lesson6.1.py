import cv2
import numpy as np #nhân ma trận
import matplotlib as plt #vẽ

# Read image: must have
I = cv2.imread("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson6\\Image\\Lenna.png")
# Show image
cv2.namedWindow("image",cv2.WINDOW_NORMAL) # sử dụng hàm windows
cv2.imshow("image",I) #must have
cv2.waitKey(1) # wait until press key #must have
# get dimension
print("color: ", I.shape)
print(len(I.shape))
[rows,cols,channel]=I.shape # -> [height (rows), width (cols), channel] = [y, x, channel]; gốc tọa độ top left # gray[row,col] = gray[y,x]
# convert color to gray
gray=cv2.cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray",gray)
print(gray.shape)
print(len(gray.shape))
cv2.waitKey(1)

# get value: giá trị chỉ từ 0->255
[rows,cols]=gray.shape
# for i in range(10):
#     for j in range(10):
#         print(gray[i,j],end=' ') #truy xuất tuple: hàng, cột
#         gray[i,j]=0
#     print('\n')
# cv2.imshow("new gray",gray)
# cv2.waitKey(2)

# hàng chẵn cột chẵn -> 255
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if i%2==0 and j%2==0:
            gray[i,j]=255
    print()
cv2.imshow("gray2.0",gray)
cv2.waitKey(1)

# get pixel
rows=0
cols=0
channel=0
if (len(I.shape)==3):
    [rows,cols,channel]=I.shape
else:
    [rows,cols]=I.shape
# for i in range(rows):
#     for j in range(cols):
#         print("{",end="")
#         for k in range(channel):
#             if k == channel-1:
#                 print(I[i,j,k],end='')
#             else:
#                 print(I[i,j,k],end=',')
#         print("}",end=", ")
#     print('\n')
print(I[0:10,0:10,0])
I[100:200,30:40,:]=255
cv2.imshow("gray3.0",I)
cv2.waitKey()