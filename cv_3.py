import cv2
img = cv2.imread('/Users/utkarshsinh/Downloads/celeb.jpg')
width = 600
height = 850
dim = (width,height)
resized = cv2.resize(img,dim)
print('Size in bytes',img.size)

cv2.imshow('Original',resized)

flip = cv2.flip(resized,1)
flip1 = cv2.flip(resized,0)
flip3 = cv2.flip(resized,-1)

cv2.imshow('Horizontal',flip)
cv2.imshow('Vertical',flip1)
cv2.imshow('Horizontal and Vertical',flip3)

cv2.waitKey(0)