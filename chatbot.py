import streamlit as st

def chatbot_main():
    st.title("AI Chatbot")
    user_input = st.text_input("Ask something:")
    if user_input:
        st.write(f"🤖 Bot: I don't understand '{user_input}', but I'm learning!")
