import numpy as np
import cv2

# connect webcam
cap = cv2.VideoCapture(0)
lower = np.array([0, 45, 62])
higher = np.array([255, 203, 255])
cascade = cv2.CascadeClassifier("C:\\Users\\Admin\\Documents\\c4t\\Image Processing\\Lesson7\\haarcascade_frontalface_alt2.xml")

while (True):
    ret, frame = cap.read()  # ret: trả về là có đọc được ảnh hay không
    # cv2.rectangle(erodeImage,(0,0),(int(frame.shape[1]/2),int(frame.shape[0]/2)),(0,0,255),5)
    cv2.rectangle(frame, (0, 0), (int(frame.shape[1] / 2), int(frame.shape[0] / 2 + 200)), (255, 255, 255), 5)

    # get ROI
    roi = frame[0:int(frame.shape[0] / 2 + 200), 0:int(frame.shape[1] / 2), :]
    # roi = cv2.flip(roi, 1)

    hsvImage = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)

    # convert to binary
    binImage = cv2.inRange(hsvImage, lower, higher)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    erodeImage = cv2.erode(binImage, kernel)

    # find contour
    ret, contours, hierarchy = cv2.findContours(binImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        cv2.drawContours(roi, i, -1, (255, 0, 255), 5)
    if len(contours) > 0:
        maxlen = cv2.arcLength(contours[0], True)
        indexmax = 0
        for i in range(len(contours)):
            leni = cv2.arcLength(contours[i], True)
            if leni > maxlen:
                maxlen = leni
                indexmax = i
        cv2.drawContours(roi, contours, indexmax, (255, 255, 0), 5)

        M = cv2.moments(contours[indexmax])
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(frame, (cx, cy), 10, (120, 255, 0), 5)
        cv2.circle(binImage, (cx, cy), 10, (120, 255, 0), 5)

    faces = cascade.detectMultiScale(erodeImage)
    for x, y, w, h in faces:
        cv2.rectangle(erodeImage, (x, y), (x + w, y + h), (0, 0, 0), cv2.FILLED)
        # frame[y:y + h, x:x + w, :] = frame[y:y + h, x:x + w, :] - newmask
    cv2.rectangle(erodeImage, (0, 0), (int(frame.shape[1] / 2), int(frame.shape[0] / 2+200)), (255, 255, 255), 5)
    # erodeImage=cv2.flip(erodeImage,1)

    cv2.imshow("roiImage", roi)
    cv2.imshow("binImage",binImage)
    cv2.imshow("erode",erodeImage)
    # cv2.imshow("hsvImage",hsvImage)
    # cv2.imshow("video",frame)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
