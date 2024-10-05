import cv2
import numpy as np
img = cv2.imread(r"C:\Users\selva\Desktop\DeskTop\OpenCV\Posters\2.png")
width,height = 300,500
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
imgResize = cv2.resize(img,(500,700))
imgcrop = imgResize[0:200,0:400]
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(imgResize,matrix,(width,height))
cv2.imshow("Old",imgResize)
cv2.imshow("Image",imgOutput)


cv2.waitKey(0)