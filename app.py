import streamlit as st
import hashlib
import time
from streamlit_mic_recorder import mic_recorder

from agent import RealEstateAgent
from stt import transcribe
from tts import speak
from recommender import recommend_property


st.set_page_config(page_title="Dubai Real Estate AI", page_icon="🏢")

st.title("🏢 Dubai Real Estate AI Assistant")


# ---------- MODEL SELECTOR ----------

st.sidebar.header("🧠 Model Selection")

model_name = st.sidebar.selectbox(
    "Choose AI Model",
    [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
    ]
)


# ---------- SESSION STATE ----------

if "agent" not in st.session_state or st.session_state.get("model") != model_name:
    st.session_state.agent = RealEstateAgent(model_name)
    st.session_state.model = model_name

if "last_audio_hash" not in st.session_state:
    st.session_state.last_audio_hash = None


# ---------- SIDEBAR VOICE ----------

st.sidebar.header("🎤 Voice Query")

audio = mic_recorder(
    start_prompt="🎤 Speak",
    stop_prompt="Stop recording"
)


# ---------- CHAT HISTORY ----------

for msg in st.session_state.agent.messages[1:]:

    if msg["role"] == "user":

        st.markdown(
            f"""
            <div style="display:flex; justify-content:flex-end; margin-bottom:10px;">
                <div style="
                    background:#DCF8C6;
                    padding:10px 14px;
                    border-radius:12px;
                    max-width:60%;
                    font-size:15px;">
                    {msg["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        with st.chat_message("assistant"):
            st.markdown(msg["content"])


# ---------- TEXT INPUT ----------

user_input = st.chat_input("Ask about Dubai properties...")


# ---------- TEXT QUERY ----------

if user_input:

    # user bubble right
    st.markdown(
        f"""
        <div style="display:flex; justify-content:flex-end; margin-bottom:10px;">
            <div style="
                background:#DCF8C6;
                padding:10px 14px;
                border-radius:12px;
                max-width:60%;
                font-size:15px;">
                {user_input}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        full_response = ""

        for token in st.session_state.agent.chat_stream(user_input):

            full_response += token

            message_placeholder.markdown(full_response)

            time.sleep(0.03)

    # voice output
    audio_file = speak(full_response)

    audio_bytes = open(audio_file, "rb").read()

    st.audio(audio_bytes, format="audio/mp3")

    # property recommendation
    recommended = recommend_property(user_input)

    if recommended:

        st.sidebar.subheader("🏡 Recommended Properties")

        for prop in recommended:

            st.sidebar.image(prop["image"])
            st.sidebar.write(prop["name"])
            st.sidebar.write(f"Location: {prop['location']}")
            st.sidebar.write(f"Price: AED {prop['price']:,}")


# ---------- VOICE QUERY ----------

if audio:

    audio_bytes = audio["bytes"]

    audio_hash = hashlib.md5(audio_bytes).hexdigest()

    if audio_hash != st.session_state.last_audio_hash:

        st.session_state.last_audio_hash = audio_hash

        with open("voice_input.wav", "wb") as f:
            f.write(audio_bytes)

        user_text = transcribe("voice_input.wav")

        # user bubble right
        st.markdown(
            f"""
            <div style="display:flex; justify-content:flex-end; margin-bottom:10px;">
                <div style="
                    background:#DCF8C6;
                    padding:10px 14px;
                    border-radius:12px;
                    max-width:60%;
                    font-size:15px;">
                    {user_text}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.chat_message("assistant"):

            message_placeholder = st.empty()

            full_response = ""

            for token in st.session_state.agent.chat_stream(user_text):

                full_response += token

                message_placeholder.markdown(full_response)

                time.sleep(0.03)

        # voice reply
        audio_file = speak(full_response)

        reply_audio = open(audio_file, "rb").read()

        st.audio(reply_audio, format="audio/mp3", autoplay=True)

        # recommendations
        recommended = recommend_property(user_text)

        if recommended:

            st.sidebar.subheader("🏡 Recommended Properties")   

            for prop in recommended:

                st.sidebar.image(prop["image"])
                st.sidebar.write(prop["name"])
                st.sidebar.write(f"Location: {prop['location']}")
                st.sidebar.write(f"Price: AED {prop['price']:,}")