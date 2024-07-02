import streamlit as st
import base64
import requests
from openai import OpenAI

st.title("Vision Assistant")
# picture = st.camera_input("",help="Show anything within this frame")
def encode_image(file_path):
  with open(file_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
      
picture = st.image('lol.png')

if picture:
    st.write("Execute")
    st.image(encode_image(picture))