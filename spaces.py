import cv2 as cv
#import matplotlib.pyplot as plt

img = cv.imread('C:/Users/offic/Downloads/Cat.jpg')
cv.imshow('Cat', img)

# plt.imshow(img)
# plt.show()

#BGR  to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab= cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB )
cv.imshow('RGB', rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV--> BGR', hsv_bgr)

#LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR', lab_bgr)

cv.waitKey(0)