import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from video_processor import analyze_video_feed

st.set_page_config(page_title="AI Teaching Assistant", layout="centered")
st.title("🎓 AI Teaching Assistant")
st.write("Monitor student emotions during online classes.")

if st.button("Start Monitoring (30 seconds)"):
    with st.spinner("Analyzing emotion feed..."):
        emotions = analyze_video_feed()

    if not emotions:
        st.warning("No emotions detected. Try again.")
    else:
        emotion_counts = pd.Series(emotions).value_counts()

        st.subheader("Emotion Distribution")
        fig, ax = plt.subplots()
        emotion_counts.plot(kind='bar', color='skyblue', ax=ax)
        st.pyplot(fig)

        positive = emotion_counts.get("Happy", 0) + emotion_counts.get("Surprise", 0)
        engagement_score = (positive / len(emotions)) * 100
        st.metric("Engagement Score", f"{engagement_score:.1f}%")

        if emotion_counts.get("Sad", 0) + emotion_counts.get("Angry", 0) > len(emotions) * 0.3:
            st.error("⚠️ Many students look frustrated or sad. You may need to re-engage the class.")
