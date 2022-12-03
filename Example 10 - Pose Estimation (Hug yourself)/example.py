import cv2
import mediapipe as mp

# Video capture settings
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Pose definitions
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while cap.read():
    
    # Reading frame
    success, img = cap.read()
    # It's optional, we used mirror effect
    img = cv2.flip(img, 1)
    # BGR to RGB Color conversion
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Process pose to recognize
    results = pose.process(img_rgb)
    
    # When record every pose, this condition will use
    if results.pose_landmarks:
        # First impression is 'you are sad' (so False)
        motions = []
        result_text = "You're sad..."
        
        # Draw landmarks
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    
        for id, lm in enumerate(results.pose_landmarks.landmark):
            
            h, w, c = img.shape
            # Convert ratios to reel positions
            cx,cy = int(w * lm.x), int(h * lm.y)
            
            # We choose 19th and 20th point
            if id == 19 or id == 20:
                motions.append([id, cx, cy])
        
        # If has record
        if len(motions) != 0:
            # Set result_text according to your pose
            result_text = "You're happy! Always be like this" if motions[0][1] - 50 < motions[1][1] else "You're sad..."
    
    # Draw rectangle and put text about your happines
    cv2.rectangle(img, (int(cap.get(3)), int(cap.get(4) / 7 )), (0,0), (0,0,0), cv2.FILLED)
    cv2.putText(img, result_text,(48,48), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
    cv2.imshow("Capture", img)
    cv2.waitKey(1)