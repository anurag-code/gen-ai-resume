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
        st.title("Resume Assistant")

    job_req_default='''Job Requirements: 
        Qualifications & Experience:
        - Hands-on data engineering expertise. Experience in building a data ingestion, transformation, and egress framework will be highly advantageous
        - Knowledge of best practices for data warehousing, data management and architecture, with significant experience in data pipelines, frameworks, tools and technologies and their use in business contexts
        - Exposure to developing technical designs, including data profiling, cataloguing, and mapping exercises
        - Experience in the design and build of APIs (REST/SOAP) to push and pull data from various data systems and platforms
        - Familiar working with DevSecOps tools, methodologies such as CI/CD with GitHub, and Azure DevOps
        - Ideally you will have good knowledge of the Azure Data platform (Azure Synapse, Data Factory, Data Bricks, Data Lake, Power BI) and Azure cloud data technologies (Spark, ADLS2, CosmosDB, AKS, AEH).
        - Strong SQL background particularly with capability to write performant queries and troubleshoot performance'''

    experience_default='''
    June 2018- Till Now,  Lead Engineer , ABC Company, New York 
    June 2017 – June 2018, Developer, XYZ Pty Ltd, Chicago
    June 2015 – June 2017, Consultant, QWE Pty Ltd, New York
    '''

    skill_default='''
    Programming Language: C++, Python & R
    Big Data: PySpark, Databricks
    Digital Analytics: Google Analytics, Adobe Analytics
    '''

    edu_default='''
    MS (2014-2015) - Data Science, RMIT, Melbourne 
    BS (2008-2012) - Mechanical Engineering, Melbourne Univerity, Melbourne
    '''

    project_default='''
    - Developed a campaign optimization tool for Sales team.
    - Conceptualized & developed a text summarization application. 
    '''

    awards_default='''Employee of The Year Award, 2019'''


    st.markdown('''This app aims to help you in creation of your Resume,
     by helping you with the relevant content in your Resume based on job requirements.''')
    st.markdown("To get some help in your Resume, you need to follow below steps.")
    st.markdown("**Step 1.** Enter job requirements in the box below.")
    st.markdown("""**Step 2.** Copy and Paste texts for different sections (Experience, Skills..) from your old CV.
    If you dont have old CV then just write few words/sentences. You dont need to write nice sentences, AI will take care of that. 
    Default values are given inside text boxes are just for reference. You can delete those and write (copy paste) your own in any format. """)
    st.markdown("**Step 3.** Download the generated Word file with the content.")
    st.markdown("**Step 4.** After downloading  the word file, edit it based on your requirements.")


    # # Function to create a styled label with a specific color
    # def styled_label(text, color):
    #     return f"<span style='color:{color}; font-weight:bold;'>{text}</span>"
    
    # unsafe_allow_html=True
    st.markdown("---")
    # st.markdown(":blue[Enter Job Requirements]")
    job_requirements = st.text_area(":blue[**Enter Job Requirements**]", value=job_req_default ,height=150)
    st.markdown("---")
    
    # Copy and paste Experience from your existing CV
    # st.markdown('<h6 style="color:red;">Write or Copy and Paste your Experience Section from your old cv here</h6>', unsafe_allow_html=True)
    experience_past = st.text_area(':blue[**Write or Copy and Paste your Experience Section from your old cv here**]',value=experience_default, height=150)
    st.markdown("---")
    # Number of words for Experience
    exp_nos_words = st.sidebar.slider(":black[**Experience**: Pick max number of tokens/words]", 0, 300,115)

    # Copy and paste Skills from your existing CV
    skills_past = st.text_area(''':blue[**Write or Copy and Paste your Skills Section from your old cv here**]''', value=skill_default,height=150)
    # Number of words for Skills
    skills_nos_words = st.sidebar.slider(":black[**Skills**: Pick max number of tokens/words for description of each skill]", 0, 100,15)
    st.markdown("---")

    # Copy and paste education from your existing CV
    edu_past = st.text_area(''':blue[**Write or Copy and Paste your Education Section from your old cv here**]''',value=edu_default ,height=150)
    # # Number of words for education
    edu_nos_words = 50 #st.sidebar.slider(":black[**Education**: Pick max number of tokens/words]", 0, 500,75)
    st.markdown("---")

    # Copy and paste Projects from your existing CV
    projects_past = st.text_area(''':blue[**Write or Copy and Paste your Projects Section from your old cv here**]''',value=project_default ,height=150)
    # Number of words for Skills
    projects_nos_words = st.sidebar.slider(":black[**Projects**: Pick max number of tokens/words]", 0, 150,25)
    st.markdown("---")

    # Copy and paste Achievements/Awards from your existing CV
    awards_past = st.text_area(''':blue[**Write or Copy and Paste your Awards Section from your old cv here**]''',value=awards_default, height=150)
    # Number of words for Skills
    awards_nos_words = st.sidebar.slider(":black[**Awards**: Pick max number of tokens/words]", 0, 100,25)
    st.markdown("---")

    # Initialize button state
    submit_clicked = st.button("Submit All Sections")

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
        st.warning("Please click Submit All button before proceeding.")


# Note:
# Add default value to the text areas to generate default CV.
# Add space between respective text areas.
# add a section for probable interview questions based on Resume.
# topics to prepare
