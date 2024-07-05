import streamlit as st
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder
import base64
import io
from openai import OpenAI

honey = OpenAI(api_key=st.secrets["OPENAI"]["OPENAI_API_KEY"])


def whisper_stt(openai_api_key=None, start_prompt="Start recording", stop_prompt="Stop recording", just_once=False, use_container_width=False, language=None, callback=None, args=(), kwargs=None, key=None):
    if not 'openai_client' in st.session_state:
        st.session_state.openai_client = OpenAI(api_key=openai_api_key or os.getenv('OPENAI_API_KEY'))
    if not '_last_speech_to_text_transcript_id' in st.session_state:
        st.session_state._last_speech_to_text_transcript_id = 0
    if not '_last_speech_to_text_transcript' in st.session_state:
        st.session_state._last_speech_to_text_transcript = None
    if key and not key + '_output' in st.session_state:
        st.session_state[key + '_output'] = None
    audio = mic_recorder(start_prompt=start_prompt, stop_prompt=stop_prompt, just_once=just_once,
                         use_container_width=use_container_width,format="webm", key=key)
    new_output = False
    if audio is None:
        output = None
    else:
        id = audio['id']
        new_output = (id > st.session_state._last_speech_to_text_transcript_id)
        if new_output:
            output = None
            st.session_state._last_speech_to_text_transcript_id = id
            audio_bio = io.BytesIO(audio['bytes'])
            audio_bio.name = 'audio.webm'
            success = False
            err = 0
            while not success and err < 3:  # Retry up to 3 times in case of OpenAI server error.
                try:
                    transcript = st.session_state.openai_client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_bio,
                        language=language
                    )
                except Exception as e:
                    print(str(e))  # log the exception in the terminal
                    err += 1
                else:
                    success = True
                    output = transcript.text
                    st.session_state._last_speech_to_text_transcript = output
        elif not just_once:
            output = st.session_state._last_speech_to_text_transcript
        else:
            output = None

    if key:
        st.session_state[key + '_output'] = output
    if new_output and callback:
        callback(*args, **(kwargs or {}))
    return output


def tts(description):
    response = honey.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=description
    )
    voice = response.content
    return io.BytesIO(voice)


def encode_image(image_data):
    return base64.b64encode(image_data).decode('utf-8')


def vision(image, speech):
    base64_image = encode_image(image)
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
            "content": [
                {"type": "text", "text": f"{speech}"},
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }]
        }],
        max_tokens=300,
    )
    return response.choices[0].message.content


st.title("Vision Assistant")
image = st.camera_input('', help="Show anything within this frame")


if image:
    st.write("Executing")
    image_data = image.getvalue()
    st.image(image_data, caption='Captured Image', use_column_width=True)
    try:
        speech = whisper_stt(openai_api_key=st.secrets['OPENAI']['OPENAI_API_KEY'], language = 'en')
        if speech:
            description = vision(image_data, speech)
            tts = tts(description)
            st.write("You : " + speech)
            st.write("Vision Analysis Result:")
            audio_base64 = base64.b64encode(tts.read()).decode('utf-8')
            components.html(f"""
                    <section hidden>
                        <audio id="audio" controls>
                            <source src="data:audio/mp3;base64,
                            {audio_base64}" type="audio/mp3">
                        </audio>
                    </section>
                    <script>
                var audioElement = document.getElementById('audio');
                audioElement.currentTime = 0; // Ensure playback starts from the beginning
                audioElement.play();
            </script>
                    """,height=0)
            st.write(description)
    except Exception as e:
        st.error(f"An error occurred: {e}")
