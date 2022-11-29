import cv2
import matplotlib.pyplot as plt

# Import image
img = cv2.imread("shine.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show original image
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("OFF")
plt.title("Original Image")

# Threshold Operation
""""
    Binary Image: image definition as white and black
    Threshold: it is method for converting image to binary image.
    
    Some threshold types:
        * THRESH_BINARY
        * THRESH_BINARY_INV
        * THRESH_TRUNC
        * THRESH_TOZERO
        * THRESH_TOZERO_INV
"""
_, thresh_image = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_image, cmap="gray")
plt.axis("off")
plt.title("Thresh Binary")

# Adaptive Threshold Operation
"""
    Some adaptive threshold algorithms:
        * ADAPTIVE_THRESH_MEAN_C
        * ADAPTIVE_THRESH_GAUSSIAN_C
"""
# Usage: .adaptiveThreshold(img, maxValue, threshing algorithm [constant c is 8], threshold type, block size, constant c)
thresh_image2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)
plt.figure()
plt.imshow(thresh_image2, cmap="gray")
plt.axis("OFF")
plt.title("Adaptive Thresh")

cv2.waitKey(1)