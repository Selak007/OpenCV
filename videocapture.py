import cv2 as cv

def resizeimg(frame,scale = 0.75): #for all videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0)

def changeres(width,height): #only for live video
    capture.set(3,width)
    capture.set(4,height)

while True:
    isTrue,frame = capture.read()
    reframe = resizeimg(frame)
    #cv.imshow('Cam',frame)
    cv.imshow('Resized',reframe)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()