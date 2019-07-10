import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib.image as  mpimg
#matplotlib inline

img1 = cv2.imread('images/road.jpg')
cv2.imshow('1',img1)
gray = np.copy(img1)
gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
#cv2.imshow('2',gray)
blur = np.copy(gray)
blur = cv2.GaussianBlur(blur,(9,9),0)
#cv2.imshow('3',blur)

#canny = cv2.Canny(blur,80,150)
canny = cv2.Canny(blur,255/3,255/2)
cv2.imshow('4',canny)

#hough_img = np.zeros(canny.shape,dtype=np.int8)
hough_img = np.copy(img1)
#hough_img = cv2.cvtColor(hough_img,cv2.COLOR_BGR2RGB)

#lines = cv2.HoughLinesP(canny,1,np.pi/180,10,0,4,18)
lines = cv2.HoughLinesP(canny,1,np.pi/180,10,0,40,20)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(hough_img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('5',hough_img)

img2 = np.zeros(canny.shape,dtype=np.int8)
vertices = np.array([[0,img2.shape[0]],[img2.shape[1],img2.shape[0]],[5*(img2.shape[1])/10,310],[5*(img2.shape[1])/10,310]],np.int32)
cv2.fillPoly(img2,[vertices],255)

masked = cv2.bitwise_and(img2,img2,mask = canny)
cv2.imshow('scdf',masked)

cv2.waitKey(0)
cv2.destroyAllWindows()