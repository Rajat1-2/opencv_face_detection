"""
Basic example: Image manipulation - resize, rotate, convert to grayscale
Learn basic image transformations with OpenCV.
"""

import cv2

# Load an image
image = cv2.imread('../../sample_images/sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # 1. Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Converted to grayscale")
    
    # 2. Resize image
    # Method 1: Specify exact dimensions
    resized = cv2.resize(image, (300, 300))
    print("Resized to 300x300")
    
    # Method 2: Scale by a factor
    scale_percent = 50  # 50% of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    scaled = cv2.resize(image, (width, height))
    print(f"Scaled to {scale_percent}% of original size")
    
    # 3. Rotate image
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # 45 degrees
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h))
    print("Rotated by 45 degrees")
    
    # Display all images
    cv2.imshow('Original', image)
    cv2.imshow('Grayscale', gray_image)
    cv2.imshow('Resized', resized)
    cv2.imshow('Scaled 50%', scaled)
    cv2.imshow('Rotated', rotated)
    
    print("\nPress any key to close all windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
