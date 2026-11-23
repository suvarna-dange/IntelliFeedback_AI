import streamlit as st
import pandas as pd

from src.preprocessing import load_data
from src.sentiment_analysis import train_model
from src.analytics import (
    get_sentiment_counts,
    get_sentiment_percentage,
    get_total_feedback
)

st.set_page_config(page_title="IntelliFeedback AI", layout="wide")

st.title("IntelliFeedback AI")
st.markdown(
    "### AI-Powered Student Feedback Analysis Dashboard"
)
st.caption("Analyze student feedback, understand sentiments and generate reports.")
st.subheader("Student Feedback Analytics & Intelligence Platform")

# Load dataset
# Upload Dataset
uploaded_file = st.file_uploader("Upload Student Feedback CSV", type=["csv"])

if uploaded_file is not None:
    data = load_data(uploaded_file)
else:
    data = load_data("data/student_feedback.csv")
# Train AI model
model, vectorizer = train_model(data)

# Analytics
total = get_total_feedback(data)
counts = get_sentiment_counts(data)
percentage = get_sentiment_percentage(data)

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Feedback", total)
col2.metric("Positive Feedback", counts.get("Positive", 0))
col3.metric("Negative Feedback", counts.get("Negative", 0))
col4.metric("Neutral Feedback", counts.get("Neutral", 0))

# Sentiment chart
st.subheader("Sentiment Analysis")
st.bar_chart(counts)

# Percentage
st.subheader("Sentiment Percentage")
st.write(percentage.round(2))
st.subheader("Sentiment Distribution Pie Chart")

st.pyplot(
    percentage.plot(
        kind="pie",
        autopct="%1.1f%%",
        figsize=(6, 6)
    ).figure
)
st.subheader("Sentiment Percentage")
st.write(percentage.round(2))

# Dataset
st.subheader("Student Feedback Data")
st.dataframe(data)
st.download_button(
    label="Download Feedback Report",
    data=data.to_csv(index=False),
    file_name="student_feedback_report.csv",
    mime="text/csv"
)

# AI Prediction
st.subheader("Check New Feedback")

user_feedback = st.text_area("Enter Student Feedback")

if st.button("Analyze Feedback"):
    if user_feedback.strip():
        cleaned_feedback = user_feedback.lower()
        transformed = vectorizer.transform([cleaned_feedback])
        prediction = model.predict(transformed)

        st.success(f"Predicted Sentiment: {prediction[0]}")
    else:
        st.warning("Please enter feedback first.")