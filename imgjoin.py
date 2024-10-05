import cv2
import numpy as np
img = cv2.imread(r"C:\Users\selva\Desktop\DeskTop\OpenCV\Posters\2.png")

imgResize = cv2.resize(img,(250,350))

hor = np.hstack((imgResize,imgResize))
ver = np.vstack((imgResize,imgResize))
cv2.imshow("Image",hor)
cv2.imshow("Image",ver)

cv2.waitKey(0)