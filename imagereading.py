import cv2 as cv

poster = cv.imread(r'C:\Users\selva\Desktop\OpenCV\Posters\1.png')

def resizeimg(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cv.imshow('Poster',resizeimg(poster,0.5))

cv.waitKey(0)