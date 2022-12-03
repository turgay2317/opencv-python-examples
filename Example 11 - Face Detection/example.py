import cv2
import mediapipe as mp

# Capture settings
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Face detection functions, and drawing tools
mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection()
mpDraw = mp.solutions.drawing_utils

while cap.read():
    succes, img = cap.read()
    # It's optional. Mirror.
    img = cv2.flip(img,1)
    
    if succes:
        # BGR to RGB Conversion
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Get face detection results
        results = faceDetection.process(img_rgb)
        
        if results.detections:
            for id, detection in enumerate(results.detections):
                # Bounding data of the box
                box = detection.location_data.relative_bounding_box
                h,w,c = img.shape
                # Assign bounds to a variable
                box_bounds = int(box.xmin * w), int(box.ymin * h), int(box.width * w), int(box.height * h)
                # Rectangle usage : .rectangle(img, (startX, startY), (width, height), rgb_Color)
                cv2.rectangle(img, box_bounds, (0,255, 0))
        
    cv2.imshow("Capture", img)
    cv2.waitKey(1)