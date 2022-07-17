import cv2
import numpy as np

img = cv2.imread('/Users/utkarshsinh/Downloads/celeb.jpg')

row = img.shape[1]
column = img.shape[0]

center = (column/2 , row/2)
angle = 180
r = cv2.getRotationMatrix2D(center, angle, 1)

rotated = cv2.warpAffine(img,r,(column,row))

cv2.imshow('Original', img)
cv2.imshow('Rotated', rotated)

cv2.waitKey(0)