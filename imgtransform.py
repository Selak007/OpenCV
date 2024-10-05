import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\selva\Desktop\OpenCV\Posters\4.jpeg')



def resizeimg(frame,scale = 0.75): #for all videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cv.imshow('Poster',resizeimg(img,0.4))

cv.waitKey(0)