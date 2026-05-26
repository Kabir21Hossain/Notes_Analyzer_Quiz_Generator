import streamlit as st

st.title('Note Summary and Quiz Generator',anchor=False)
st.write('Upload upto 3 images to generate Note and Summary and Quiz')
st.divider()

with st.sidebar:
    st.subheader('Controls')
    files=st.file_uploader('Upload the Photos of your notes',type=['JPEG','JPG','PNG'],accept_multiple_files=True)

    choice=st.selectbox('Enter the difficulty of Quiz',['Easy','Medium','Hard'],index=None)
    if st.button('Click the button to initiate AI'):
        if len(files)


