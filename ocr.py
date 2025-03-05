import streamlit as st
from backend.ocr import extractTextFromImage

def ocr_main():
    st.title("Bank Data Processing OCR")
    uploaded_file = st.file_uploader("Upload an image")
    if uploaded_file:
        st.image(uploaded_file)
        result = extractTextFromImage(uploaded_file)
        st.write(result.ParsedResults[0].ParsedText)
