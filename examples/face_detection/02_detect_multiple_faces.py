"""
Multiple Face Detection Example: Detect multiple faces in an image
Shows how the algorithm can detect multiple faces simultaneously.
"""

import cv2

# Load the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Error: Could not load face cascade classifier")
    exit()

# Load an image (preferably with multiple people)
image = cv2.imread('../../sample_images/sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    # Adjusting parameters for better detection:
    # - scaleFactor: How much the image size is reduced at each scale (1.1 = 10% reduction)
    # - minNeighbors: How many neighbors each candidate rectangle should have (higher = fewer detections but more reliable)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    print(f"Number of faces detected: {len(faces)}")
    
    # Draw rectangles and labels for each face
    for i, (x, y, w, h) in enumerate(faces):
        # Different color for each face
        color = (0, 255, 0)  # Green
        cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
        
        # Add face number label
        label = f'Face {i+1}'
        cv2.putText(image, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        # Print face coordinates and size
        print(f"Face {i+1}: Position ({x}, {y}), Size {w}x{h}")
    
    # Display the result
    cv2.imshow('Multiple Face Detection', image)
    
    print("\nPress any key to close the window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
