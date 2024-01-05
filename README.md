### 1.  You would need the openai api key to run the application

### 2.  To run the application locally: In the terminal                >> streamlit run app.py


##### Create a .env file to save OPENAI_API_KEY. Create .env file in same folder as that of script.
##### Section_Yaml_files folder has the section based yaml files, which are dynamically generated and are based on job requirements.

### Project Tree:

┣ 📂generated_output_files
┃ ┗ 📜resume_ideation_msword_1704410986.792585.docx
┣ 📂notebooks
┃ ┗ 📜MS_Word_CV_Formatter.ipynb
┣ 📂python_scripts
┃ ┣ 📜.env
┃ ┣ 📜app.py
┃ ┣ 📜job_reqmnt_based_resume_content.py
┃ ┗ 📜ms_word_cv_format_generator.py
┣ 📂section_yaml_files
┃ ┣ 📜resume_awards.yaml
┃ ┣ 📜resume_education.yaml
┃ ┣ 📜resume_experience.yaml
┃ ┣ 📜resume_projects.yaml
┃ ┗ 📜resume_skill.yaml
┣ 📜.gitignore
┣ 📜LICENSE
┣ 📜README.md
┗ 📜requirements.txt
┣ 📂images
┃ ┣ 📜confusion.png
┃ ┗ 📜pic_cv.png