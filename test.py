import streamlit as st
import base64
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI"]["OPENAI_API_KEY"])



def encode_image(file_path):
  with open(file_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def vision_file(file_path):
    base64_image= encode_image(file_path)
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": """
        You are an image analysis assistant powered by GPT-4 with vision capabilities. Your task is to identify and describe objects in images provided by the user. Follow these guidelines:

        1. Object Identification:
           - Identify and name the primary objects present in the image.
           - Provide a brief description of each identified object.

        2. Contextual Understanding:
           - Understand the context in which the objects appear.
           - Provide relevant information about the scene, such as actions taking place, relationships between objects, and any notable background elements.

        3. User Queries:
           - Answer specific questions the user may have about the objects or the scene.
           - Provide detailed and accurate descriptions based on visual cues in the image.

        4. Clarity and Detail:
           - Ensure descriptions are clear and detailed.
           - Avoid ambiguity and be as specific as possible in your identifications and descriptions.
        """},
        {"role": "user", "content":[
            {
                "type":"image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"}
            }
        ]}
      ],
    max_token=300,
    )
    print(response.json().choices[0].message.content)

st.title("Vision Assistant")
image = st.camera_input("", help="Show anything within this frame")

# image = img.open('lol.png')

if image:
    st.write("Execute")
    vision_file(image)
