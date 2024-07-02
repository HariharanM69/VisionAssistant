import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


def main():
    img_file_buffer = st.camera_input("Take a picture")

    img_file = UploadedFile(img_file_buffer.getvalue(), "image/jpeg",
                            img_file_buffer.name)
    st.image(img_file)


if __name__ == "__main__":
    main()
