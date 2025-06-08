import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load emotion detection model (.keras format)
emotion_model = load_model("emotion_detection_model.keras")
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Load OpenCV Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    emotions = []
    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (48, 48))
        roi = cv2.cvtColor(roi, cv2.COLOR_GRAY2RGB) # Convert to RGB (because using MobileNetV2)
        roi = roi.astype("float32") / 255.0
        roi = np.expand_dims(roi, axis=0)

        # Predict emotion
        pred = emotion_model.predict(roi, verbose=0)
        emotion = emotion_labels[np.argmax(pred)]
        emotions.append(emotion)

        # Draw face box & label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    return frame, emotions

