import cv2 as cv

img = cv.imread("C:/Users/offic/Downloads/wlpr.jpg")
cv.imshow('PIC', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Averag Blur', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur
median = cv.medianBlur(img,3)
cv.imshow('MedianBlur', median)

#Bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 15, 35)
cv.imshow('Bilateral Bluring', bilateral)

cv.waitKey(0)