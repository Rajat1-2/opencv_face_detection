"""
Smile Detection Example: Detect smiles in a static image
This example shows how to detect smiles within detected faces.
"""

import cv2

# Load the Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Check if cascades loaded successfully
if face_cascade.empty() or smile_cascade.empty():
    print("Error: Could not load cascade classifiers")
    exit()

# Load an image
image = cv2.imread('../../sample_images/sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces first
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    print(f"Number of faces detected: {len(faces)}")
    
    # For each detected face, detect smiles
    total_smiles = 0
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Region of Interest (ROI) for smile - only look in the lower half of the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        
        # Detect smiles within the face ROI
        # Note: Smile detection can be less reliable than face/eye detection
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.8,
            minNeighbors=20,
            minSize=(25, 25)
        )
        
        # If smile detected, add label
        if len(smiles) > 0:
            cv2.putText(image, 'Smiling!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            total_smiles += 1
            
            # Draw rectangles around detected smiles
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
        else:
            cv2.putText(image, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    
    print(f"Total smiles detected: {total_smiles}")
    
    # Display the result
    cv2.imshow('Smile Detection', image)
    
    print("\nPress any key to close the window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the result
    cv2.imwrite('smile_detected_output.jpg', image)
    print("Result saved as 'smile_detected_output.jpg'")
