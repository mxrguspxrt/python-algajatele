import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

ball_width = 10

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image_height, image_width, _ = image.shape

    current_hands = results.multi_hand_landmarks
    if current_hands:
      current_hands = sorted(current_hands, key=lambda hand_landmark: hand_landmark.landmark[0].x)

    if current_hands:      
      for hand_landmarks in current_hands:
          latest_x = hand_landmarks.landmark[0].x * image_width
          latest_y = hand_landmarks.landmark[0].y * image_height

          cv2.circle(image,(int(latest_x), int(latest_y)), ball_width, (0,0,255), -1)

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()