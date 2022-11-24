import cv2

# import image file
# img = cv2.imread(FILENAME, READING_TYPE)
#   Reading Types 0 : Grayscale | 1 : Colorful
img = cv2.imread("steve.jpeg", 0)
cv2.imshow("Steve Jobs (Grayscale)", img)

img2 = cv2.imread("steve.jpeg", 1)
cv2.imshow("Steve Jobs (Colorful)", img2)

cv2.waitKey(1)