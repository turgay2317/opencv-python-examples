import cv2
import numpy as np

# Set Canvas width and height
width   = 512
height  = 512

# Create canvas with numpy zero matrix
# np.zeros((width, height, type), datatype)
canvas = np.zeros((width, height, 3), np.uint8)

# Show canvas
cv2.imshow("My Black Canvas", canvas)

# Create a line

# cv2.line(image, (startX, startY), (endX, endY), (BGR Color Code))
# BGR -> (Blue, Green, Red) color codes range 0-255
line1 = cv2.line(canvas, (0,0), (100,100), (255, 255, 255))
cv2.imshow("First line", line1)

line2 = cv2.line(canvas, (100,100), (100,200), (0,255,0))
cv2.imshow("Second line", line2)

# Create a rectangle
# cv2.rectangle(img, (startX, startY), (endX, endY), (BGR Color Code))
rectangle = cv2.rectangle(canvas, (100,200), (150,250), (255,0,0,0))
cv2.imshow("Rectangle", rectangle)

# OR you can fill the rect
rectangle2 = cv2.rectangle(canvas, (150,250), (200,300), (255,50,50), cv2.FILLED)
cv2.imshow("Rectangle filled", rectangle2)

# Create a circle
# cv2.circle(img, (startX, startY), radius, (BGR Color Code))
circle = cv2.circle(canvas, (200,300), 50, (0,0,255))
cv2.imshow("Circle", circle)

# Create a ellipse
# cv2.ellipse(img, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)
ellipse = cv2.ellipse(canvas,(256,256),(50,50),0,0,180,255,-1)
cv2.imshow("Ellipse", ellipse)

# Create a text
# cv2.putText(img, value, (startX, startY), font, fontScale, color)
creator = cv2.putText(canvas, "Turgay Ceylan", (200,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.imshow("Creator", creator)

cv2.waitKey(1)
