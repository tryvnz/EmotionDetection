AI Teaching Assistant - Emotion Detection Dashboard
===================================================

This project is a Streamlit-based dashboard that monitors student emotions in real time using your webcam.
It uses a trained deep learning model to detect facial expressions and generate an engagement score based on emotional feedback.

📁 Folder Contents:
-------------------
- dashboard.py – Main Streamlit UI for emotion monitoring  
- video_processor.py – Captures webcam feed and runs detection  
- model.py – Contains face detection and emotion classification logic  
- emotion_detection_model.keras – Pre-trained emotion detection model  
- requirements.txt – Python package dependencies

🚀 How to Run:
--------------
1. Install Python (3.8 or above)  
   https://www.python.org/downloads/

2. Create and activate a virtual environment  
   On Windows:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install required packages  
   ```
   pip install -r requirements.txt
   ```

4. Run the app  
   ```
   streamlit run dashboard.py
   ```

5. Press "Start Monitoring"  
   It will activate your webcam for 30 seconds, analyze emotions, and display a chart.

⚠️ Notes:
---------
- If you get a script execution error while activating venv, run PowerShell as Administrator and use:
  ```
  Set-ExecutionPolicy RemoteSigned
  ```

- Ensure your webcam is functional and accessible by OpenCV.
- Press `Q` to manually stop the webcam feed if needed.

🧠 Emotion Labels:
------------------
- Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral