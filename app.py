# Install required libraries (if not installed already)
# !pip install streamlit transformers

import streamlit as st
from transformers import pipeline

# Load the pre-trained model from Hugging Face
# You can change the model to other summarization models from Hugging Face
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)

# Streamlit app title
st.title("Text Summarization using Hugging Face")

# Text input from the user
text = st.text_area("Enter text to summarize", "")

# When the user clicks the button, summarize the input text
if st.button("Summarize"):
    if text:
        with st.spinner("Summarizing..."):
            summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
            st.write("**Summary:**")
            st.write(summary[0]['summary_text'])
    else:
        st.write("Please enter some text for summarization.")

# To run the Streamlit app, save this script and run: streamlit run <script_name>.py
