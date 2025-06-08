# EmotionDetection
# Therapist Support Tool – Emotion Detection Dashboard

This is a Streamlit-based AI tool designed to help **therapists monitor and interpret patient emotions** during virtual or in-person video sessions. It uses a deep learning model to detect facial expressions and provides emotion distribution summaries, positive emotion ratio, and therapist-focused insights.

---

## Folder Contents

- `dashboard.py` – Streamlit dashboard UI for real-time emotion monitoring  
- `video_processor.py` – Captures webcam or virtual camera feed and runs detection  
- `model.py` – Face detection (Haar cascade) and emotion classification (CNN model)  
- `emotion_detection_model.keras` – Pretrained emotion classification model (MobileNetV2)  
- `requirements.txt` – List of required Python packages

---

## How to Run

### 1. Install Python (3.8 or above)  
[Download Python here](https://www.python.org/downloads/)

### 2. Open terminal in project folder
cd pc/yourpath/EmoDetect

### 3. Create and activate a virtual environment  
python -m venv venv
.\venv\Scripts\activate

### 4. Install required packages
pip install -r requirements.txt

### 5. Run the app
streamlit run dashboard.py
