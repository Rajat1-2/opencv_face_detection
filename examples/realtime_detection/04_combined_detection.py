"""
Real-time Combined Detection: Detect faces, eyes, and smiles from webcam feed
This is the most comprehensive example combining all detection features.
Press 'q' to quit, 's' to save a snapshot.
"""

import cv2
from datetime import datetime

# Load all Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

if face_cascade.empty() or eye_cascade.empty() or smile_cascade.empty():
    print("Error: Could not load cascade classifiers")
    exit()

# Initialize webcam
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not access the webcam")
    exit()

print("Starting real-time combined detection...")
print("Press 'q' to quit, 's' to save snapshot")

# Main loop for real-time detection
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    if not ret:
        print("Error: Could not read frame from webcam")
        break
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    total_eyes = 0
    total_smiles = 0
    
    # Process each detected face
    for (x, y, w, h) in faces:
        # Region of Interest
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Detect eyes within face
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(20, 20)
        )
        
        # Detect smile within face
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.8,
            minNeighbors=20,
            minSize=(25, 25)
        )
        
        # Draw rectangles around eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            total_eyes += 1
        
        # Draw face rectangle and label based on smile detection
        is_smiling = len(smiles) > 0
        if is_smiling:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(frame, 'Smiling! :)', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            total_smiles += 1
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    
    # Display statistics on frame
    cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f'Eyes: {total_eyes}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f'Smiles: {total_smiles}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Display the resulting frame
    cv2.imshow('Real-time Combined Detection', frame)
    
    # Handle key presses
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('s'):
        # Save snapshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'snapshot_{timestamp}.jpg'
        cv2.imwrite(filename, frame)
        print(f"Snapshot saved as {filename}")

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()
print("Real-time combined detection stopped")
