import streamlit as st
from PIL import Image
from openai import OpenAI

st.title("Vision Assistant")
# picture = st.camera_input("",help="Show anything within this frame")

picture = st.image('lol.png')

if picture:
    st.write("Execute")
    st.image(Image.open(picture))