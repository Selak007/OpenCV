import cv2
import numpy as np

imag = np.zeros((512,512,3),np.uint8)
cv2.line(imag,(0,0),(imag.shape[1],imag.shape[0]),(0,255,0),3)
cv2.rectangle(imag,(0,0),(250,250),(0,0,255),2)
cv2.circle(imag,(400,50),30,(0,255,255),3)
cv2.putText(imag,"Open CV",(300,100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,150,0),1)\

cv2.imshow("Art",imag)
cv2.waitKey(0)