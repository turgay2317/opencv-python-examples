import cv2
import time

# Actually this method provides importing video like an image frame by frame
capture = cv2.VideoCapture("street.mp4")

width = capture.get(3) # Get capture width
height = capture.get(4) # Get capture height
interval = 100

print("Width : {}, Height: {}".format(width, height))

if not capture.isOpened:
    print("Failure")

while capture.isOpened():
    
    # Capture frame
    ret, frame = capture.read()
    
    if not ret:
        break
    
    # Display result frame
    cv2.imshow("Frame", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(interval) & 0xFF == ord('q'):
        break
    
# When everything ok, release vid capture object
capture.release()

# Close all windows
cv2.destroyAllWindows()

