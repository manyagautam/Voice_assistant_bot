import streamlit as st
from chatbot import chatbot_main
from ocr import ocr_main

st.sidebar.title("Navigation")
app_choice = st.sidebar.radio("Choose App", ["Chatbot", "Bank OCR"])

if app_choice == "Chatbot":
    chatbot_main()

elif app_choice == "Bank OCR":
    ocr_main()
