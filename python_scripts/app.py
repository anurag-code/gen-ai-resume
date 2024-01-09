import streamlit as st
from job_reqmnt_based_resume_content import *
from ms_word_cv_format_generator import *
from dotenv import load_dotenv
import os

if __name__=="__main__":

    # Display image and title
    col1, col2 = st.columns([1, 5])  # Create columns for layout
    with col1:
        st.image("./images/pic_cv.png", width=100)
    with col2:
        st.title("Resume Ideation")

    st.markdown('''This app aims to help you in creation of your Resume,
     by helping you with the relevant content in your Resume based on job requirements.''')

    st.markdown("To get some help in your Resume, you need to follow below steps.")
    st.markdown("Step 1. Enter job requirements in the box below.")
    st.markdown("""Step 2. Copy and Paste texts for different sections (Experience, Skills..) from your old CV.
    If you dont have old CV then just write few words/sentences. You dont need to write nice sentences, AI will take care of that.""")
    st.markdown("Step 3. Download the generated Word file with the content.")
    st.markdown("Step 4. After downloading  the word file, edit it based on your requirements.")


    # Function to create a styled label with a specific color
    def styled_label(text, color):
        return f"<span style='color:{color}; font-weight:bold;'>{text}</span>"
    
    #  unsafe_allow_html=True

    # st.markdown(":blue[Enter Job Requirements]")
    job_requirements = st.text_area(":blue[Enter Job Requirements]", height=100)
    
    # Copy and paste Experience from your existing CV
    # st.markdown('<h6 style="color:red;">Write or Copy and Paste your Experience Section from your old cv here</h6>', unsafe_allow_html=True)
    experience_past = st.text_area(':blue[Write or Copy and Paste your Experience Section from your old cv here]', height=150)
    # Number of words for Experience
    exp_nos_words = st.slider(":orange[Experience: Pick max number of words]", 0, 500,220)

    # Copy and paste Skills from your existing CV
    skills_past = st.text_area(''':blue[Write or Copy and Paste your Skills Section from your old cv here]''', height=150)
    # Number of words for Skills
    skills_nos_words = st.slider(":orange[Skills: Pick max number of words]", 0, 500,200)

    # Copy and paste education from your existing CV
    edu_past = st.text_area(''':blue[Write or Copy and Paste your Education Section from your old cv here]''', height=150)
    # Number of words for education
    edu_nos_words = st.slider(":orange[Education: Pick max number of words]", 0, 500,75)

    # Copy and paste Projects from your existing CV
    projects_past = st.text_area(''':blue[Write or Copy and Paste your Projects Section from your old cv here]''', height=150)
    # Number of words for Skills
    projects_nos_words = st.slider(":orange[Projects: Pick max number of words]", 0, 500,150)

    # Copy and paste Achievements/Awards from your existing CV
    awards_past = st.text_area(''':blue[Write or Copy and Paste your Awards Section from your old cv here]''', height=150)
    # Number of words for Skills
    awards_nos_words = st.slider(":orange[Awards: Pick max number of words]", 0, 500,150)

    # Initialize button state
    submit_clicked = st.button("Submit All")

    # Also added if clause so that script move beyond it only if all submit buttons are clicked. on click Submit button returns 1 else 0.
    if submit_clicked:
        st.success("All submit button clicked! Proceeding...")
        
        # Run the first script
        st.info("Creating Content for Ideation... ")

        # create content related to the job requirements
        create_content_yaml(experience_past,exp_nos_words,skills_past,skills_nos_words,edu_past,edu_nos_words,awards_past,awards_nos_words,projects_past,projects_nos_words,job_requirement=job_requirements)

        # completion of first script
        st.info("Created Content for Ideation.")

        # Run second script
        st.info("Creating word file from the content created in the previous step.")

        # create word file
        output_file_path=create_ms_word_doc()

        # Run second script
        st.info(f"Successfully Created Resume Ideation Word File {output_file_path}")

        # Download the word file
        # Download button
        st.download_button(
            label="Download Word File",
            data=open(output_file_path, "rb"),
            file_name="downloaded_word_file.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    
    else:
        st.warning("Please click all submit buttons before proceeding.")


# Note:
# Add default value to the text areas to generate default CV.
# Add space between respective text areas.
# add a section for probable interview questions based on Resume.
# topics to prepare
