import cv2
import numpy as np

video = cv2.VideoCapture('/Users/utkarshsinh/Desktop/vaccine.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('Output.mp4',fourcc,25.0,(1920,1080))
while video.isOpened():
    ret,frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow('Frame',frame)

        if cv2.waitKey(10) == ord('s'):
            break
    else:
        break