import streamlit as st
from openai import OpenAI

st.title("Al-Hudhud AI Bot 🤖")

api_key = st.text_input("Enter your OpenAI API key:", type="password")

user_message = st.text_input("Write your message:")

if api_key and user_message:
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_message
    )

    st.write("AI:")
    st.write(response.output_text)
