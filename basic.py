import cv2 as cv

img= cv.imread("C:/Users/offic/Downloads/Cat.jpg")
cv.imshow('Cat', img)

# Converting to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur
blur= cv.GaussianBlur(img,(1,1), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascading
canny = cv.Canny(img, 125,175)
cv.imshow('Canny Edges', canny)


# Dilating the image
dilated = cv.dilate(canny,(3,3), iterations=1)
cv.imshow('Dialated', dilated)


# Eroding
eroded = cv.erode(dilated,(3,3),iterations = 3)
cv.imshow('Eroded', eroded)


# Resize
resized= cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Cropping
cropped= img[50:100,100:200]
cv.imshow('Cropped', cropped)


cv.waitKey(0)