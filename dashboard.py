import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from video_processor import analyze_video_feed  # Expects list of emotions like ["Happy", "Sad", ...]

st.set_page_config(page_title="Emotion-Aware Virtual Therapist", layout="centered")
st.title("🧘‍♀️ Emotion-Aware Virtual Therapist")
st.write("This tool summarizes your emotional state during a short reflection session.")

if st.button("Start Session (30 seconds)"):
    with st.spinner("Analyzing your emotional expressions..."):
        emotions = analyze_video_feed()

    if not emotions:
        st.warning("No emotions detected. Please ensure your face is visible and try again.")
    else:
        # Emotion count breakdown
        emotion_counts = pd.Series(emotions).value_counts()

        st.subheader("🧠 Emotion Summary")
        fig, ax = plt.subplots()
        emotion_counts.plot(kind='bar', color='orchid', ax=ax)
        ax.set_ylabel("Frequency")
        ax.set_xlabel("Emotion")
        ax.set_title("Emotion Distribution During Session")
        st.pyplot(fig)

        # Calculate percentages
        total = len(emotions)
        emotion_percent = (emotion_counts / total * 100).round(1)

        st.subheader("📊 Detailed Emotion Breakdown")
        st.dataframe(emotion_percent.rename("Percentage (%)"))

        # Highlight dominant emotion
        dominant = emotion_counts.idxmax()
        st.metric("Most Frequent Emotion", dominant)

        st.subheader("🗣️ AI Insight")
        if dominant == "Happy":
            st.success("You seemed cheerful and positive during this session. Keep nurturing those good vibes.")
        elif dominant == "Sad":
            st.info("You appeared a bit down. Remember, it's okay to feel this way — consider talking to someone you trust.")
        elif dominant == "Angry":
            st.warning("You showed signs of frustration. Reflecting on triggers can be a helpful first step.")
        elif dominant == "Neutral":
            st.write("You maintained a neutral expression. Consider journaling to explore your internal state further.")
        elif dominant == "Fear":
            st.warning("Some signs of anxiety were detected. Practicing mindfulness or grounding exercises could help.")
        elif dominant == "Surprise":
            st.write("You seemed surprised or startled. If something unexpected happened, talking about it might help.")
        else:
            st.write("Emotion detected: " + dominant)

        st.caption("This session summary is for self-awareness and is not a clinical diagnosis.")
