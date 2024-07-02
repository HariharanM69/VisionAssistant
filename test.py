import streamlit as st
from openai import OpenAI

st.title("Vision Assistant")
picture = st.camera_input("",help="Show anything within this frame")

if picture == True:
    st.write("Execute")