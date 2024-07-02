import streamlit as st
import base64
from PIL import Image as img
import requests
from openai import OpenAI

st.title("Vision Assistant")
image = st.camera_input("",help="Show anything within this frame")
      
# image = img.open('lol.png')

if image:
    st.write("Execute")
    st.image(image)