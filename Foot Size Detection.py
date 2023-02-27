import cv2
import numpy as np

# Load the image
img = cv2.imread('D:\Projects\Python\photo_2023-02-27_21-39-24.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding to create a binary image
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the largest contour by area
max_contour = max(contours, key=cv2.contourArea)

# Get the bounding rectangle of the largest contour
x, y, w, h = cv2.boundingRect(max_contour)

# Draw the bounding rectangle on the original image
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Calculate the foot size (assuming rectangular shape)
foot_size = w * h

# Show the image and foot size
cv2.imshow('image', img)
print("Foot size: ", foot_size)

# Wait for user input to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
