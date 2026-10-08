from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
import streamlit as st

load_dotenv()
model= ChatOpenRouter(
    model='dots-studio/dots-3-note-preview:free'
)



st.header("Research Tool")

user_input = st.text_input("Enter the prompt")

if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)