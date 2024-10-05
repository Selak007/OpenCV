import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\selva\Desktop\OpenCV\Posters\1.png')
def resizeimg(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cv.imshow('Pic',resizeimg(img,0.3))
# Convert to grayscale

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',resizeimg(gray,0.3))

# Blur an image
# blur = cv.GaussianBlur(img,(13,13),cv.BORDER_DEFAULT)
# cv.imshow('Blur',resizeimg(blur,0.3))

# Edge Cascading (Highlight the edges)
canny = cv.Canny(img,100,100)
cv.imshow('Cascade',resizeimg(canny,0.3))

# Dilate the canny
dil = cv.dilate(canny,(5,5),iterations=5)
cv.imshow('Dilated',resizeimg(dil,0.3))

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Crop

x, y, w, h = 50, 50, 100, 100
cropped = img[y:y+h, x:x+w]

if cropped.size == 0:
    print("Error: Cropped region is empty. Check the ROI coordinates.")
else:
    cv.imshow('Cropped', cropped)
    cv.waitKey(0)
    cv.destroyAllWindows()
cv.waitKey(0)