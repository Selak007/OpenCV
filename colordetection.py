import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\selva\Desktop\DeskTop\OpenCV\Posters\2.png")

# Function for trackbar callback (does nothing but is required for trackbars)
def empty():
    pass

# Create a window for trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)

# Create trackbars for adjusting Hue, Saturation, and Value ranges
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)

cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)

cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    # Resize the image
    imgResize = cv2.resize(img, (250, 350))

    # Convert the image to HSV color space
    imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)

    # Get the current positions of all trackbars
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")

    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")

    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Define the lower and upper bounds for HSV
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create a mask that isolates the colors in the range
    mask = cv2.inRange(imgHSV, lower, upper)

    # Apply the mask to the original image (optional: get the result of the mask on the original image)
    result = cv2.bitwise_and(imgResize, imgHSV, mask=mask)

    # Display the original image, the HSV image, and the mask
    cv2.imshow("Image", imgResize)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close all windows
cv2.destroyAllWindows()
