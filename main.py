import streamlit as st
from call_api import note_generator,audio_transcript,quiz_generator
from PIL import Image

st.title('Note Summary and Quiz Generator',anchor=False)
st.write('Upload upto 3 images to generate Note and Summary and Quiz')
st.divider()

with st.sidebar:
    st.subheader('Controls')
    images=st.file_uploader('Upload the Photos of your notes',type=['JPEG','JPG','PNG'],accept_multiple_files=True)

    pil_images=[Image.open(img) for img in images]
    if images:
        if len(images)>3:
            st.error('Upload 3 images at most')
        else:
            cols=st.columns(len(images))
            st.subheader('Uploaded images')

            for i,img in enumerate(images):
                with cols[i]:
                    st.image(img)

    choice=st.selectbox('Enter the difficulty of Quiz',['Easy','Medium','Hard'],index=None)
    if choice:
        st.markdown(f"you have selected **{choice}** level")
    pressed = st.button('Click the button to initiate AI', type="primary")

    # if pressed:
    #     if not images:
    #         st.error('please upload at least one image')
    #     elif not choice:
    #         st.error('Please choose difficulty level')
    #     else:
    #         pass




if pressed:
    if not images:
        st.error('you must upload at least one image')

    if not choice:
        st.error('You must select a difficulty')

    if images and choice:
        #note
        with st.container(border=True):
            st.subheader('Your Note')
            with st.spinner('Ai is writing for you'):
                generated_notes = note_generator(pil_images)
                generated_notes=generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*", "")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("' ", "")
                st.markdown(generated_notes)





        #Audio transcription
        with st.container(border=True):
            st.subheader('Audio Transcription')
            with st.spinner:
                voice=audio_transcript(generated_notes)
                st.audio(voice)

        #quiz
        with st.container(border=True):
            st.subheader(f'Quiz ({choice}) Difficulty')
            with st.spinner('AI is generating quizzes'):
                quiz = quiz_generator(pil_images, choice)
                st.markdown(quiz)



