import streamlit as st

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

    st.button("Generate Summary and Quiz",type="primary")

