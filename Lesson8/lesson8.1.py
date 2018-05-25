import cv2
import numpy as np

# read im
I1 = cv2.imread("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson8\\1.png")
cv2.imshow("Image1", I1)
cv2.waitKey(1)

# compute SIFT
gray1 = cv2.cvtColor(I1, cv2.COLOR_RGB2GRAY)
sift1 = cv2.xfeatures2d.SIFT_create()
kpt1, des1 = sift1.detectAndCompute(gray1, None)
cv2.drawKeypoints(I1, kpt1, I1)
cv2.imshow("keypoint", I1)
cv2.waitKey(1)

# multiple images
indexgood = -1
maxpoint = -1
for i in range(1, 9):
    file = "C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson8\\" + str(i) + ".png"
    I2 = cv2.imread(file)
    gray2 = cv2.cvtColor(I2, cv2.COLOR_RGB2GRAY)
    sift2 = cv2.xfeatures2d.SIFT_create()
    kpt2, des2 = sift2.detectAndCompute(gray2, None)
    # matching bruce force; ngoài ra còn thuật cluster
    bf = cv2.BFMatcher_create()
    matches = bf.knnMatch(des1, des2, 2)
    OutImg = cv2.drawMatchesKnn(I2, kpt1, I2, kpt2, matches, None)
    cv2.imshow("matching", OutImg)
    cv2.waitKey(1)
    # choose match good
    good = []
    for m, n in matches:
        if m.distance<0.2*n.distance:
            good.append([m])
    if len(good)>maxpoint:
        maxpoint = len(good)
        indexgood = i
    # OutImg2 = cv2.drawMatchesKnn(I1, kpt1, I2, kpt2, good, None)
    # cv2.imshow("good", OutImg2)
    # cv2.waitKey()

file = "C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson8\\" + str(indexgood) + ".png"
I2 = cv2.imread(file)
cv2.imshow("best matching", I2)
cv2.waitKey()