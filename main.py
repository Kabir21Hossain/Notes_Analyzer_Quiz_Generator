import streamlit as st

st.title('Note Summary and Quiz Generator',anchor=False)
st.write('Upload upto 3 images to generate Note and Summary and Quiz')
st.divider()

with st.sidebar:
    st.subheader('Controls')
    images=st.file_uploader('Upload the Photos of your notes',type=['JPEG','JPG','PNG'],accept_multiple_files=True)

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

    else:
        pass