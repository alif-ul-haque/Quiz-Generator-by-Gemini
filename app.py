import streamlit as st
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image

st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate summaries and quizzes based on the content of the images.")
st.divider()

with st.sidebar:
    st.header("Upload Images")
    images = st.file_uploader(
        "Upload your images here (up to 3)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
    )

    if images:
        if len(images) > 3:
            st.error("Please upload a maximum of 3 images.")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))
            for i,image in enumerate(images):
                with col[i]:
                    st.image(image)
                
    #difficulty
    selected_option = st.selectbox(
        "Select Quiz Difficulty",
        options=["Easy", "Medium", "Hard"],
        index=None,
    )
    
    if selected_option:
        st.markdown(f"You have selected difficulty level {selected_option}")
    else:
        st.error("Please select a quiz difficulty level.")

    pressed = st.button("Generate Summary and Quiz",type="primary")

if pressed:
    if not images:
        st.error("Please upload at least one image to generate summary and quiz.")
    if not selected_option:
        st.error("Please select a quiz difficulty level to generate quiz.")
    if images and selected_option:

        #note

        with st.container(border=True):
            st.subheader("Summary")
            
            #summary
            with st.spinner("AI Generating summary..."):
                pil_images = [Image.open(image) for image in images]
                generated_note = note_generator(pil_images)
                st.markdown(generated_note)


        #audio transcript
        with st.container(border=True):
            st.subheader("Audio Transcript")
            
            #audio
            with st.spinner("AI Generating audio..."):
                generated_audio = audio_transcription(generated_note)
                st.audio(generated_audio)
        
        #quiz
        with st.container(border=True):
            st.subheader("Quiz")
            
            #quiz
            with st.spinner("AI Generating quiz..."):
                generated_quiz = quiz_generator(pil_images, selected_option)
                st.markdown(generated_quiz)





