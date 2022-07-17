# Color above threshold value changes to white while those under it remains the same

import cv2
import numpy as np

img = cv2.imread('/Users/utkarshsinh/Downloads/celeb.jpg')

threshold_value = 100

_,binary_threshold = cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow('Original', img)
cv2.imshow('Binary Threshold',binary_threshold)

cv2.waitKey(0)