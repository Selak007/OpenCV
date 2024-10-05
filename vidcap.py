import cv2
import numpy as np

# Set frame dimensions
frameWidth = 640
frameHeight = 480

# Initialize video capture, change index (0, 1) if necessary
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)  # Set brightness

# Check if the camera is opened correctly
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a window with trackbars to adjust HSV values
def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)

# Create trackbars for HSV color range
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

# Set the trackbars to default values
cv2.setTrackbarPos("HUE Min", "HSV", 0)
cv2.setTrackbarPos("HUE Max", "HSV", 179)
cv2.setTrackbarPos("SAT Min", "HSV", 0)
cv2.setTrackbarPos("SAT Max", "HSV", 255)
cv2.setTrackbarPos("VALUE Min", "HSV", 0)
cv2.setTrackbarPos("VALUE Max", "HSV", 255)

while True:
    # Capture the frame
    success, img = cap.read()

    # Check if the frame was captured properly
    if not success:
        print("Failed to grab frame.")
        break

    # Convert image from BGR to HSV color space
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get current positions of trackbars
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    # Define the HSV color range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create a mask to filter out colors within the specified range
    mask = cv2.inRange(imgHsv, lower, upper)

    # Debugging: check if any pixels are detected
    non_zero_count = cv2.countNonZero(mask)
    print(f"Non-zero mask pixels: {non_zero_count}")

    if non_zero_count == 0:
        print("No colors detected within the specified range")

    # Apply the mask to the original image to show the result
    result = cv2.bitwise_and(img, img, mask=mask)

    # Show individual windows for original image, mask, and result
    cv2.imshow("Original", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
