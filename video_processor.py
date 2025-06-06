import cv2
import time
import numpy as np
import streamlit as st
from model import detect_emotion

def analyze_video_feed(source=0, duration=30):
    cap = cv2.VideoCapture(source)
    emotions_log = []
    frame_placeholder = st.empty()  # Placeholder for live webcam frame

    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, emotions = detect_emotion(frame)
        emotions_log.extend(emotions)

        # Convert for streamlit
        rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(rgb, channels="RGB", caption="Live Emotion Detection")

    cap.release()
    return emotions_log
