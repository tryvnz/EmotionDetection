import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from video_processor import analyze_video_feed  

st.set_page_config(page_title="Therapist Support Dashboard", layout="centered")
st.title("Therapist Emotion Insight Tool")
st.write("This tool supports therapists by analyzing a patient's emotional expressions. It provides insights into facial emotions during a consultation session to help improve understanding.")

if st.button("Start Session (30 seconds)"):
    with st.spinner("Analyzing patient's emotion in real-time..."):
        emotions = analyze_video_feed()

    if not emotions:
        st.warning("No emotions detected. Please ensure patient's face is visible and try again.")
    else:
        st.success("Emotion analysis complete.")
        emotion_counts = pd.Series(emotions).value_counts()

        st.subheader("Emotion Summary")
        fig, ax = plt.subplots()
        emotion_counts.plot(kind='bar', color='orchid', ax=ax)
        ax.set_ylabel("Frequency")
        ax.set_xlabel("Emotion")
        ax.set_title("Emotion Distribution During Session")
        st.pyplot(fig)

        # Calculate percentages
        total = len(emotions)
        emotion_percent = (emotion_counts / total * 100).round(1)

        st.subheader("Detailed Emotion Breakdown")
        st.dataframe(emotion_percent.rename("Percentage (%)"))

        # Highlight dominant emotion
        dominant = emotion_counts.idxmax()
        st.metric("Most Frequent Emotion", dominant)

        st.subheader("AI Insight")
        if dominant == "Happy":
            st.success("The patient predominantly expressed happiness. This may indicate comfort or openness during the session.")
        elif dominant == "Sad":
            st.info("The patient showed signs of sadness. Consider exploring underlying emotional topics or recent events that may have contributed.")
        elif dominant == "Angry":
            st.warning("Elevated signs of frustration or anger were detected. It may be helpful to explore possible sources of emotional agitation or unmet needs.")
        elif dominant == "Neutral":
            st.write("The patient maintained a neutral expression for most of the session. Consider probing gently to assess emotional state beneath the surface.")
        elif dominant == "Fear":
            st.warning("Signs of anxiety or fear were observed. This could reflect internal tension or sensitive subject matter. Grounding techniques might be beneficial.")
        elif dominant == "Surprise":
            st.write("The patient appeared surprised or caught off guard at moments. This may indicate unexpected emotional triggers during discussion.")
        else:
            st.write("Emotion detected: " + dominant)

        st.caption("This summary is intended to support therapist interpretation. It is not a diagnostic conclusion.")
