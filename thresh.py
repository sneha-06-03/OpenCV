import cv2 as cv

img = cv.imread("C:/Users/offic/Downloads/wlpr.jpg")
cv.imshow('pic', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simole Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simole Thresholded Inverse', thresh_inv)

#Adaptive Thesholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV,11, 3)
cv.imshow('Adaptive Thesholding', adaptive_thresh)


cv.waitKey(0)