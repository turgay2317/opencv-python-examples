import cv2
import numpy as np

# Read original image (size : 470x470)
original_img = cv2.imread("view.png")

# Set start points of image
points1 = np.float32([[283,0], [0,281],[190,470],[465,187]])

# Set new start points of image
points2 = np.float32([[470,0], [0, 0], [0, 282], [465, 282]])

# define matrix as transform first points to last points
matrix = cv2.getPerspectiveTransform(points1, points2)

# Create output image by matrix
output_img = cv2.warpPerspective(original_img, matrix, (470, 282))

# Show output image
cv2.imshow("Rotated Image", output_img)

cv2.waitKey(1)
