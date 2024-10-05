import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\selva\Desktop\DeskTop\OpenCV\Posters\8.png")
imgResize = cv2.resize(img,(250,350))
imgContour = imgResize.copy()
imgGray = cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

def getCountours(img):
    coutours,hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in coutours:
        area = cv2.contourArea(cnt)
        print(area)
        
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            perimeter = cv2.arcLength(cnt,True)
            print(perimeter)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(approx)
            x,y,w,h = cv2.boundingRect(approx)

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            if len(approx) == 3:
                ObjectType = "Tri"
            elif len(approx) == 4:
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05:
                    ObjectType = "Square"
                else:
                    ObjectType = 'Rectangle'

            else:
                ObjectType = "None"
            
            cv2.putText(imgContour,ObjectType,(x+(w//2) - 10,y+(h//2) - 10),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,0.5,(0,255,255),1)

getCountours(imgCanny)
cv2.imshow("Orignal",imgResize)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Contours",imgContour)
cv2.waitKey(0) 

