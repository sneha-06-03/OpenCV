import cv2 as cv
# import matplotlib.pyplot as plt


img = cv.imread("C:/Users/offic/Downloads/wlpr.jpg")
cv.imshow('pic', img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#GrayScale Histogram
gray_hist = cv.calcHist([gray],[0], None, [256], [0,256]) 

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlable('Bins')
# plt.ylable('# of pixels')
# plt.xlim([0,256])
# plt.show()

cv.waitKey(0)
