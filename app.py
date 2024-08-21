import streamlit as st
import google.generativeai as genai


st.title("WELCOME TO KANI's GPT")

genai.configure(api_key="AIzaSyDV37W3oM9yOLdM7DNsNDfZbffpmPB48Bc")  

text = st.text_input("Enter your Question:")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)