import cv2
import numpy as np
img = cv2.imread("Posters\3.jpeg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,100,200)
kernel = np.ones((5,5),np.uint8)
imgDil = cv2.dilate(imgCanny,kernel,iterations=1)
imgerode = cv2.erode(imgDil,kernel,iterations=1)