import streamlit as st
import base64
import io
# from PIL import Image as img
from openai import OpenAI as honeyy

honey = honeyy.api_key=st.secrets["OPENAI"]["OPENAI_API_KEY"]


def encode_image(image_data):
   return base64.b64encode(image_data).decode('utf-8')


def vision_file(file_path):
   base64_image = encode_image(file_path)
   response = honey.chat.completions.create(
       model="gpt-4o",
       messages=[{
           "role":
           "system",
           "content":
           """
        You are an image analysis assistant powered by GPT-4 with vision capabilities. 
        Your task is to identify and describe objects in images provided by the user. 
        """
       }, {
           "role":
           "user",
           "content": [{
               "type": "image_url",
               "image_url": {
                   "url": f"data:image/jpeg;base64,{base64_image}"
               }
           }]
       }],
       max_tokens=300,
   )
   return (response.choices[0].message.content)


st.title("Vision Assistant")
image = st.camera_input('', help="Show anything within this frame")

# image = "lol.png"

if image:
   st.write("Executing")
   image_data = image.getvalue()
   st.image(image_data, caption='Captured Image', use_column_width=True)
   try:
        description = vision_file(image_data)
        st.write("GPT-4 Analysis Result:")
        st.write(description)
   except Exception as e:
        st.error(f"An error occurred: {e}")
