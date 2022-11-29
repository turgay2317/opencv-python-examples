import cv2
import matplotlib.pyplot as plt

# Import a building image
img = cv2.imread("buildings.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Mean Filter usage (ksize : blurring kernel size.)
mf = cv2.blur(img, ksize = (5,5))

# Plot show mean filtered image
plt.figure()
plt.imshow(mf)
plt.title("Mean Filtered image")
plt.axis("OFF")

# Gauss Filter usage
gf = cv2.GaussianBlur(img, ksize = (5,5), sigmaX = 10)

# Plot show gauss filtered image
plt.figure()
plt.imshow(gf)
plt.title("Gaussian Filtered image")
plt.axis("OFF")

# Import an image that contains salt-pepper noise
"""
    Salt pepper noise: presents itself as sparsely occurring white and black pixels.
"""

img2 = cv2.imread("salt-papper-img.jpeg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Plot show original image and configuration
plt.figure()
plt.imshow(img2)
plt.title("Image with salt-pepper noise")
plt.axis("OFF")

# Median
mb = cv2.medianBlur(img2, ksize = 3)

# Plot show median filtered image and configuration
plt.figure()
plt.imshow(mb)
plt.title("Median Filtered image")
plt.axis("OFF")


