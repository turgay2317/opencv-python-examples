import cv2
import matplotlib.pyplot as plt

img = cv2.imread("steve.png")
img2 = cv2.imread("bill.png")

# BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Resize operations
img = cv2.resize(img, (400, 400))
img2 = cv2.resize(img2, (400,400))

# Mix operation
blended = cv2.addWeighted(src1 = img, alpha = 0.5, src2 = img2 , beta = 0.5, gamma = 0)
plt.figure()
plt.axis("off")
plt.imshow(blended)
