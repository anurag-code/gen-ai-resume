import streamlit as st
from job_reqmnt_based_resume_content import *
from ms_word_cv_format_generator import *
from dotenv import load_dotenv
import os

if __name__=="__main__":
    
    # Create a title
    st.title("Resume Ideation")

    st.markdown('''This app aims to help you in creation of your Resume,
     by helping you with the relevant content in your Resume based on job requirements.''')

    st.markdown("To get some help in your Resume, you need to follow below steps.")
    st.markdown("Step 1. Enter job requirements in the box below.")
    st.markdown("Step 2. Download the generated Word file with the content.")
    st.markdown("Step 3. After downloading  the word file, edit it based on your requirements.")

    # Input for Job description
    job_requirements = st.text_area('''Enter Job Requirements''', height=100)

    # Add submit button. Also add if clause so that script move beyond it only if it is clicked.
    if st.button("Submit"):
        # Run the first script
        st.info("Creating Content for Ideation... ")

        # create content related to the job requirements
        create_content_yaml(job_requirement=job_requirements)

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