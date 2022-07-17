import cv2
import numpy as np

img = cv2.imread('/Users/utkarshsinh/Downloads/celeb.jpg')

resize = cv2.resize(img,(520,520))

d=7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(resize,d,sigmacolor,sigmaspace)

cv2.imshow('Original', resize)
cv2.imshow('Final',b)

cv2.waitKey(0)