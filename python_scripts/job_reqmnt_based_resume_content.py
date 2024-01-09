from openai import OpenAI
from dotenv import load_dotenv
import json
import time,yaml,os
import streamlit as st

# Convert SQL to English sentences 
def resume_part_prompt(job_reqmnt,section,words=200,specific_instructions=''):

    prompt = f""" Please create a {section} section/Part of a Sample Resume, for the Job Requirements given below.

    Required Output: 
    - Output should be less than {words} words. 
    - {specific_instructions}


    {job_reqmnt}

    """

    return prompt

def prompt_employment(job_reqmnt,exp_old,words=225):

    prompt = f"""Please fill in the required information creatively as a Resume Expert, for an Experience section of a Resume. It should be done 
    in step by step. First step is to read the Job requirement given below. Second step is to read the existing content 
    about Experience section from old Resume. Third Step, enhance the Experience section from old Resume based on the job requirements.
    Description of Experience should also include some impact with some quantification.
    Final output should be in Json format.
   
    Output should be strictly less than {words} tokens.

    Required Keys and value types for Json output for the Experience section of the resume are given below. Candidate may have experience in more than one companies.:
    
    Experience:
        employer: text
        title: text
        location: text
        dates: text
        description: list 
    

    {job_reqmnt}


    Experience Section from Old Resume:
    {exp_old}


    """

    return prompt


def prompt_skill(job_reqmnt,skill_old,words=200):

    prompt = f"""Please fill in the required information creatively as a Resume Expert, for an Skills section of a Resume. This work should be done 
    in step by step manner. First step is to read the Job requirement given below. Second step is to read the existing content 
    about Skills section from old Resume. Third Step, enhance the Skills section from old Resume based on the job requirements.
    Final output should be in Json format.

    Required Keys for Json output for the Experience section of the resume are given below. Candidate can have more skills than mentioned below:
    
    Skills:
        ['skill_Name': text,'skill_Description': text]
        ['skill_Name': text,'skill_Description': text]
        ['skill_Name': text,'skill_Description': text]
        ['skill_Name': text,'skill_Description': text]
        ['skill_Name': text,'skill_Description': text]
        ['skill_Name': text,'skill_Description': text]
        ['skill_Name': text,'skill_Description': text]
        ['skill_Name': text,'skill_Description': text]
    

    Please note that Each Skill in the list should have skill name and skill description for each skill in the list. Atleast 6 key skills should be there. Output should be less than {words} tokens.
    Skill section should not mention about professional degree.

    {job_reqmnt}


    Skills Section from Old Resume:
    {skill_old}

    """

    return prompt


def prompt_education(job_reqmnt,education_old,words=75):

    prompt = f"""Please fill in the required information creatively as a Resume Expert, for an Education section of a Resume. This work should be done 
    in step by step manner. First step is to read the Job requirement given below. Second step is to read the existing content 
    about Education section from old Resume. Third Step, enhance the Education section from old Resume based on the job requirements.
    Final output should be in Json format.

    Required Key and value type for Json output for the Education section of the resume is given below. Candidate may have more than one degree:
    
    Education:
        'Institution Name': text
        'Degree Name': text
        'Year': Numeric

    
    Please note that Education should only include only the name of last University attended, degree name , and the year in which it was attended.
    Certifications or other coursework should NOT be mentioned here. Output should be less than {words} tokens.


    {job_reqmnt}


    Education Section from Old Resume:
    {education_old}

    """

    return prompt


def prompt_projects(job_reqmnt,project_old,words=100):

    prompt = f"""Please fill in the required information creatively as a Resume Expert, for an Projects section of a Resume. This work should be done 
    in step by step manner. First step is to read the Job requirement given below. Second step is to read the existing content 
    about Projects section from old Resume. Third Step, enhance the Projects section from old Resume based on the job requirements.
    Final output should be in Json format.

    Required Key and value type for Json output for the Projects section of the resume is given below:
    
    Projects:
        'Project 1': text
        'Project 2': text
        'Project 3': text
    
    Project description should be limited to one or two lines only.  Output should be strictly less than {words} tokens.


    {job_reqmnt}


    Projects Section from Old Resume:
    {project_old}

    """

    return prompt


def prompt_awards(job_reqmnt,awards_old,words=100):

    prompt = f"""Please fill in the required information creatively as a Resume Expert, for an Awards section of a Resume. This work should be done 
    in step by step manner. First step is to read the Job requirement given below. Second step is to read the existing content 
    about Awards section from old Resume. Third Step, enhance the Awards section from old Resume based on the job requirements.
    Final output should be in Json format.

    Required Key and value type for Json output for the Awards section of the resume is given below:
    
    Awards:
        'Award 1': text
        'Award 2': text
    
    Each Award description should be limited to one line or less only. Output should be less than {words} tokens.


    {job_reqmnt}


    Awards Section from Old Resume:
    {awards_old}

    """

    return prompt


# @st.cache_data  # Caching data because there is an api call. Thus if there is no change, then the there is no point calling API again.
def create_content_yaml(exp_old,exp_words,skills_old,skills_words,education_old,education_words,awards_old,awards_words,projects_old,projects_words,job_requirement=''):

    # Load environment variables from .env file. 
    # NOTE: '.env' file should be saved in same folder level as script.
    load_dotenv()

    # Access environment variables
    api_key_openai = os.getenv("OPENAI_API_KEY")

    # Create an instance for OpenAI
    client = OpenAI(api_key=api_key_openai)

    # job_reqmnt=''' '''

    if len(job_requirement)==0:
        job_reqmnt='''Job Requirements: 
            Qualifications & Experience:
            - A degree in a related discipline is preferred.
            - Hands-on data engineering expertise. Experience in building a data ingestion, transformation, and egress framework will be highly advantageous
            - Knowledge of best practices for data warehousing, data management and architecture, with significant experience in data pipelines, frameworks, tools and technologies and their use in business contexts
            - Exposure to developing technical designs, including data profiling, cataloguing, and mapping exercises
            - Experience in the design and build of APIs (REST/SOAP) to push and pull data from various data systems and platforms
            - Familiar working with DevSecOps tools, methodologies such as CI/CD with GitHub, and Azure DevOps
            - Ideally you will have good knowledge of the Azure Data platform (Azure Synapse, Data Factory, Data Bricks, Data Lake, Power BI) and Azure cloud data technologies (Spark, ADLS2, CosmosDB, AKS, AEH).
            - Strong SQL background particularly with capability to write performant queries and troubleshoot performance'''
    else:
        job_reqmnt=f'''Job Requirements:
        {job_requirement}'''


    # create prompts for each section
    experience_prompt=prompt_employment(job_reqmnt,exp_old,words=exp_words)
    skill_prompt=prompt_skill(job_reqmnt,skills_old,words=skills_words)
    education_prompt=prompt_education(job_reqmnt,education_old,words=education_words)
    projects_prompt=prompt_projects(job_reqmnt,projects_old,words=projects_words)
    awards_prompt=prompt_awards(job_reqmnt,awards_old,words=awards_words)

    # Get the output from OpenAI using propmts for each section
    experience = client.chat.completions.create(
        model="gpt-3.5-turbo-1106", #gpt-4-0613
        messages=[
        {"role": "system", "content": "You are an expert in Resume Building, skilled in creation of resume based on job requirements and output results in form of JSON format."},
        {"role": "user", "content": experience_prompt}
        ],
        response_format={ "type": "json_object" },
        max_tokens=1000,
        temperature=0.3
    )

    # time.sleep(5)

    skill = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
        {"role": "system", "content": "You are an expert in Resume Building, skilled in creation of resume based on job requirements and output results in form of JSON format."},
        {"role": "user", "content": skill_prompt}
        ],
        max_tokens=400,
        temperature=0.3
    )

    # time.sleep(5)

    education = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
        {"role": "system", "content": "You are an expert in Resume Building, skilled in creation of resume based on job requirements and output results in form of JSON format."},
        {"role": "user", "content": education_prompt}
        ],
        max_tokens=400,
        temperature=0.3
    )

    # time.sleep(5)

    projects = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
        {"role": "system", "content": "You are an expert in Resume Building, skilled in creation of resume based on job requirements and output results in form of JSON format."},
        {"role": "user", "content": projects_prompt}
        ],
        max_tokens=700,
        temperature=0.3
    )

    # time.sleep(5)

    awards = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
        {"role": "system", "content": "You are an expert in Resume Building, skilled in creation of resume based on job requirements and output results in form of JSON format."},
        {"role": "user", "content": awards_prompt}
        ],
        response_format={ "type": "json_object" },
        max_tokens=400,
        temperature=0.3
    )

    # assign names to each json objects returned from openai api. Assigning key values as below.
    section_dict={'experience':experience,'skill':skill,'education':education,'projects':projects,'awards':awards}
    
    # we can use this to combine all json putputs , if reqd. Currently not used
    # section_details={}

    # iterate through each key val in section_dict
    for section,var in section_dict.items():
        json_text = json.loads(var.choices[0].message.content)
        # print(f"\n{section}:\n{json_text}\n")

        # Specify the file path
        # Define the relative path to the yaml output folder
        relative_path = "section_yaml_files"
        # Create the full path to the output folder
        # output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
        file_path_yaml = f'{relative_path}/resume_{section}.yaml'
        # file_path_yaml = f'{output_folder}/resume_{section}.yaml'

        # # write the dict file  into a json
        # with open(file_path, 'w') as json_file:
        #     json.dump(json_text, json_file)

        # write the dict file  into a yaml
        with open(file_path_yaml, 'w') as yaml_file:
            yaml.dump(json_text, yaml_file,default_flow_style=False, indent=4,sort_keys=False)


if __name__ == '__main__':
    create_content_yaml()