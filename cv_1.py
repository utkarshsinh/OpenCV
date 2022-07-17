import cv2

img = cv2.imread("/Users/utkarshsinh/Downloads/216800414_130887749429709_9074051543781220190_n.jpg")

print('Dimensions of Image',img.shape)

width = img.shape[1]
height = 400
dim = (width,height)
resized = cv2.resize(img,dim)

print('Dimensions of New Image',resized.shape)

cv2.imshow("window", resized)

# cv2.imwrite('/Users/utkarshsinh/Downloads/car.jpg', img)

cv2.waitKey(5000)

cv2.destroyAllWindows()