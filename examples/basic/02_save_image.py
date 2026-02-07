"""
Basic example: Load an image and save it with a different name
Learn how to read and write images using OpenCV.
"""

import cv2

# Load an image
image = cv2.imread('../../sample_images/sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # Save the image with a new name
    output_path = 'output_image.jpg'
    success = cv2.imwrite(output_path, image)
    
    if success:
        print(f"Image saved successfully as '{output_path}'")
    else:
        print("Error: Could not save image.")
    
    # You can also save with different formats
    cv2.imwrite('output_image.png', image)
    print("Image also saved as PNG format")
