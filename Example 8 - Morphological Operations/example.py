import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = plt.imread("alphabet.jpeg")
plt.figure()
plt.title("Original")
plt.axis("OFF")
plt.imshow(img)

# Set kernel matrix for operations
kernel = np.ones((5,5), dtype = np.uint8)

# Erosion: allows to erode the boundaries of the object in front.
erosion = cv2.erode(img, kernel, iterations = 3)
plt.figure()
plt.title("Erosion")
plt.axis("OFF")
plt.imshow(erosion)

# Dilation: opposite of erosion. Increases the white area in the image.
dilate = cv2.dilate(img, kernel, iterations = 3)
plt.figure()
plt.title("Dilate")
plt.axis("OFF")
plt.imshow(dilate)

# Import noised image to fix with Opening
img_noise = plt.imread("car.png")
img_noise = cv2.cvtColor(img_noise, cv2.COLOR_BGR2RGB)
plt.figure()
plt.title("Original")
plt.axis("OFF")
plt.imshow(img_noise)

# Opening = Erosion + Dilation; It's using erosion and dilation in order
# It's useful to prevent noise
opening = cv2.morphologyEx(img_noise,cv2.MORPH_OPEN,kernel)
plt.figure()
plt.title("Opening")
plt.axis("OFF")
plt.imshow(opening)

# Closing: opposite of opening operation. We can use that to fix little black dots.
closing = cv2.morphologyEx(img_noise,cv2.MORPH_CLOSE,kernel)
plt.figure()
plt.title("Closing")
plt.axis("OFF")
plt.imshow(closing)

# Gradient: It's difference of dilation and erosion. With this method we can find the borders of image
gradient = cv2.morphologyEx(dilate,cv2.MORPH_GRADIENT,kernel)
plt.figure()
plt.title("Gradient")
plt.axis("OFF")
plt.imshow(gradient)

# Sobel X Operation: it's method for finding x borders of image
sudoku = cv2.imread("sudoku.png", 0)
sobelx = cv2.Sobel(sudoku, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize = 5)
plt.figure()
plt.title("Sobel X")
plt.axis("OFF")
plt.imshow(sobelx, cmap="gray")

# Sobel Y Operation: it's method for finding y borders of image
sobely = cv2.Sobel(sudoku, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize = 5)
plt.figure()
plt.title("Sobel Y")
plt.axis("OFF")
plt.imshow(sobely, cmap="gray")

# Laplacian Gradian: It's another method for finding borders
laplacian = cv2.Laplacian(sudoku, ddepth = cv2.CV_16S)
plt.figure()
plt.title("Laplacian")
plt.axis("OFF")
plt.imshow(laplacian, cmap="gray")
