import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

latest_ball_x = 100
latest_ball_y = 100
ball_width = 63
current_hands = []
previous_hands = []

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
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

    previous_hands = current_hands
    current_hands = results.multi_hand_landmarks
    if current_hands:
      for hand_landmarks in current_hands:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    if current_hands and previous_hands:
      i = -1
      for hand_landmarks in current_hands:
        i = i + 1
        try: 
          current_index_finger_tip_x = hand_landmarks.landmark[0].x * image_width
          previous_index_finger_tip_x = previous_hands[i].landmark[0].x * image_width
          moved_on_x = current_index_finger_tip_x - previous_index_finger_tip_x 
          # hand moved to left?
          if moved_on_x < 0:
            # ball was to the left and in touched area?
            if latest_ball_x < current_index_finger_tip_x: 
              latest_ball_x = current_index_finger_tip_x
              print(latest_ball_x)
          # hand moved to right?
          if moved_on_x > 0:
            # ball was to the left and in touched area?
            if latest_ball_x > current_index_finger_tip_x: 
              latest_ball_x = current_index_finger_tip_x
              print(latest_ball_x)
        except:
          None

    cv2.circle(image,(int(latest_ball_x), int(latest_ball_y)), ball_width, (0,0,255), -1)

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()