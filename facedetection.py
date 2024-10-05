import cv2

# Correct path to the Haar Cascade XML file
faceCascade = cv2.CascadeClassifier(r"C:\Users\selva\Desktop\DeskTop\OpenCV\haarcascade_frontalface_default.xml")

# Read the image
img = cv2.imread(r"C:\Users\selva\Desktop\DeskTop\OpenCV\Posters\9.png")

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or cannot be opened.")
else:
    # Resize the image to a reasonable size for faster processing
    imgResize = cv2.resize(img, (500, 700))  # Adjust the dimensions as needed

    # Convert the resized image to grayscale
    imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)

    # Perform face detection with fine-tuned parameters
    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.05, minNeighbors=3, minSize=(200, 200))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(imgResize, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the result
    cv2.imshow("Detected Faces", imgResize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

