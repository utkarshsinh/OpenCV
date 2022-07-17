
import cv2
import numpy as np

img = cv2.imread('/Users/utkarshsinh/Downloads/celeb.jpg')

resize = cv2.resize(img,(640,640))

ksize = (7,7)
sigmax = 0
sigmay = 0

blur = cv2.GaussianBlur(resize,ksize,sigmax)

cv2.imshow('Input',resize)
cv2.imshow('Blur',blur)

cv2.waitKey(0)