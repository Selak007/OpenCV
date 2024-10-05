import cv2
img = cv2.imread(r"C:\Users\selva\Desktop\DeskTop\OpenCV\Posters\2.png")
print(img.shape)
imgResize = cv2.resize(img,(500,700))
imgcrop = imgResize[0:200,0:400]
cv2.imshow("Image",imgResize)
cv2.imshow("Crop",imgcrop)

cv2.waitKey(0)