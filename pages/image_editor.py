from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import streamlit as st
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = GEMINI_API_KEY)

st.title("AI Image Editor")
uploaded_image = st.file_uploader("Upload an image for editing", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image")

user_prompt = st.text_input("How you want to edit the image?")

if st.button("ReGenerate Image"):
    if not user_prompt:
        st.warning("Please enter the edit prompt!")
    else:
        try:
            with st.spinner("Regenerating image..."):
                response = client.models.generate_content(
                model="gemini-2.0-flash-exp-image-generation",
                contents=[user_prompt, image],
                config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image']
                )
            )
            
            st.subheader("Edited Image")
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    st.write(part.text)
                elif part.inline_data is not None:
                    image = Image.open(BytesIO((part.inline_data.data)))
                    st.image(image)
                
        except Exception as e:
            st.error("Error generating image")
