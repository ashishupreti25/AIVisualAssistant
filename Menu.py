import streamlit as st
from PIL import Image
from google import genai
import os
from dotenv import load_dotenv

# ✅ API key from Streamlit secrets
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = GEMINI_API_KEY)


# ✅ Page config
st.set_page_config(
    page_title="AI Assistant Hub",
    page_icon="🤖",
    layout="centered"
)

# ✅ Optional logo
try:
    logo = Image.open("logo.png")  # or use logo-transparent.png
    st.image(logo, width=120)
except:
    st.write("")

# ✅ Title & intro
st.markdown(
    """
    <h2 style='text-align: center;'>Welcome to <span style="color:#5a78d1;">AI Visual Assistant</span> 🌟</h2>
    <p style='text-align: center; font-size: 1.1rem; color: #444;'>Hi! What would you like to do today?</p>
    """,
    unsafe_allow_html=True
)

# ✅ Style override for pastel theme
st.markdown("""
    <style>
    .stButton > button {
        background-color: #b3c7ff; /* Light blue */
        color: #222; /* Dark gray */
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
        width: 100%;
        margin: 0.5rem 0;
        transition: all 0.2s ease-in-out;
    }

    .stButton > button:hover {
        background-color: #a0bfff; /* Slightly darker blue */
        color: #000; /* Black */
    }

    .footer-text {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #888; /* Light gray */
    }

    hr {
        border: none;
        border-top: 1px solid #eee; /* Light gray */
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Centered columns with equal-width buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)

    if st.button("🎨  Generate an Image", key="btn1"):
        st.switch_page("pages/image_generator.py")

    if st.button("🖼️  Generate an Image Caption", key="btn2"):
        st.switch_page("pages/image_caption.py")

    if st.button("✏️ Edit an Image", key="btn3"):
        st.switch_page("pages/image_editor.py")

    if st.button("📺  Summarize a YouTube Video", key="btn4"):
        st.switch_page("pages/youtube_summary.py")

    st.markdown('</div>', unsafe_allow_html=True)

# ✅ Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer-text'>*Created by Ashish*</div>", unsafe_allow_html=True)
