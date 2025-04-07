import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import os

# ✅ Use API key from Streamlit secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = GEMINI_API_KEY)

st.title("AI Caption Generator")
uploaded_img = st.file_uploader("Generating the caption of the img")

if uploaded_img:
    image = Image.open(uploaded_img)
    st.image(image, caption="Uploaded image")

    if st.button("Generate Caption"):
        try:
            with st.spinner("Generating Image Caption ..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp",
                    contents=["What is this image?", image]
                )
                st.subheader("Generated Caption")
                st.write(response.text)

        except Exception as e:
            st.error('Error in generating caption')
