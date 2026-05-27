# import streamlit as st
# from google import genai
# from dotenv import load_dotenv
# from PIL import Image
# import os
#
#
# load_dotenv()
#
# key=os.environ.get('GEMINI_API_KEY')
# client =genai.Client(api_key=key)
#
# images=st.file_uploader('Upload the Photos of your notes',
#                         type=['JPEG','JPG','PNG'],
#                         accept_multiple_files=True
#
#                         )
#
#
#
# if images:
#     pil_images = [Image.open(img) for img in images]
#     prompt = """Summarize the picture in note format at max 100 words,
#             ensure to add markdown to differentiate relevancy"""
#
#     response = client.models.generate_content(
#         model='gemini-3.1-pro-preview',
#         contents=[pil_images, prompt]
#     )
#
#     st.text(response.text)
