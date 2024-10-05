import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('Blank',blank)
"""
# Paint the entire image
blank[:] = 0,255,0
cv.imshow('Green',blank)
cv.waitKey(0)

# Paint a certain portion of an image
blank[100:200,300:500] = 0,255,255
cv.imshow('Green',blank)
"""
"""
#Draw a rectangle

# No Fill
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('Rectangle',blank)

# Fill
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)
"""
# draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=cv.FILLED)
# cv.imshow('Circle',blank)

# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=3)
# cv.imshow('Circle',blank)

cv.putText(blank,"Beast mode",(225,225),cv.FONT_HERSHEY_PLAIN,1.0,(255,255,50),2)
cv.imshow('KP',blank)
cv.waitKey(0)
