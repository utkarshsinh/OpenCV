# Median blur similar to gaussian blur
import cv2
import numpy as np

img = cv2.imread('/Users/utkarshsinh/Downloads/celeb.jpg')

resize = cv2.resize(img,(520,520))

ksize = 3

blur = cv2.medianBlur(resize,ksize)

cv2.imshow('Input',resize)
cv2.imshow('Blur',blur)

cv2.waitKey(0)