"""
Basic example: Load and display an image using OpenCV
This is the first step in learning computer vision with OpenCV.
"""

import cv2

# Load an image from file
# Replace 'path_to_image.jpg' with your actual image path
image = cv2.imread('../../sample_images/sample.jpg')

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load image. Please check the path.")
else:
    print(f"Image loaded successfully!")
    print(f"Image shape: {image.shape}")  # (height, width, channels)
    print(f"Image size: {image.size} pixels")
    print(f"Image data type: {image.dtype}")
    
    # Display the image in a window
    cv2.imshow('Loaded Image', image)
    
    # Wait for a key press and then close the window
    print("\nPress any key to close the image window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
