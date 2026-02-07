"""
Face Detection Example: Detect faces in a static image
This example shows how to use Haar Cascade classifier for face detection.
"""

import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Check if cascade loaded successfully
if face_cascade.empty():
    print("Error: Could not load face cascade classifier")
    exit()

# Load an image
image = cv2.imread('../../sample_images/sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # Convert to grayscale (face detection works better on grayscale images)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    # Parameters: scaleFactor, minNeighbors, minSize
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    print(f"Number of faces detected: {len(faces)}")
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        # Draw rectangle: (image, top-left corner, bottom-right corner, color, thickness)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Add text label
        cv2.putText(image, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Display the result
    cv2.imshow('Face Detection', image)
    
    print("\nPress any key to close the window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Optionally save the result
    cv2.imwrite('face_detected_output.jpg', image)
    print("Result saved as 'face_detected_output.jpg'")
