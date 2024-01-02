from docx import Document
from docx.shared import Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import json,yaml,time,os

def read_yaml(path):
    with open(path, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)


def get_full_path(section):
    
    # Define the relative path to the resume section files
    relative_path = "../section_yaml_files"
    # Create the full path to the output folder
    output_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
    section_file_path_yaml = f'{output_folder_path}/resume_{section}.yaml'
    return section_file_path_yaml


def main():
    # Create a new Word document instance
    document = Document()

    # This function has been defined here because the instance 'document' cannot be used from outside in a function 
    def add_heading(text, level, bold=True, color=(0, 0, 0),align=WD_ALIGN_PARAGRAPH.LEFT):
        heading = document.add_heading(text, level=level)
        heading.alignment =align
        run = heading.runs[0]
        run.bold = bold
        run.font.color.rgb = RGBColor(*color)
        return heading

    # Add a title and contact
    add_heading('YOUR NAME', level=0,bold=True, color=(255, 0, 0))
    add_heading('0422332233, email@gmail.com', level=9,bold=False,align=WD_ALIGN_PARAGRAPH.RIGHT)

    # Specify the yaml file path of all sections
    file_path_exp = get_full_path('experience')
    file_path_skill = get_full_path('skill')
    file_path_education = get_full_path('education')
    file_path_projects = get_full_path('projects')
    file_path_awards = get_full_path('awards')

    # Read the JSON file back into a dictionary
    exp_details = read_yaml(file_path_exp)
    skill_details = read_yaml(file_path_skill)
    education_details = read_yaml(file_path_education)
    projects_details = read_yaml(file_path_projects)
    awards_details = read_yaml(file_path_awards)

    # level 1 heading color
    level_1_heading_color=(255, 0, 0)

    # Add EXPERIENCE section heading
    exper=add_heading('EXPERIENCE', level=1, bold=True, color=level_1_heading_color)

    # Iterate through experience details
    for exp in exp_details[list(exp_details.keys())[0]]:
        for k,v in exp.items():

            if k.lower().strip() == 'employer':
                key = add_heading((k.upper()), level=3,color=(0, 32, 96))

                if isinstance(v,list):
                    for line in v:
                        document.add_paragraph(line,style='List Bullet')
                else:
                    run1= key.add_run(f'     {v}')
                    run1.bold = True
                    run1.font.color.rgb = RGBColor(0, 0, 0)
            else:
                key = add_heading((k.upper()), level=3, color=(0, 32, 96))

                if isinstance(v,list):
                    for line in v:
                        document.add_paragraph(line,style='List Bullet')
                else:
                    run1= key.add_run(f'     {v}')
                    run1.bold = False
                    run1.font.color.rgb = RGBColor(0, 0, 0)
                
        document.add_paragraph()   # to add empty line
    # document.add_page_break() # Add Page break after experience

    # Skill section
    skills = add_heading('SKILLS', level=1,bold=True, color=level_1_heading_color)
    skills.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for _,v in skill_details[list(skill_details.keys())[0]].items():
        document.add_paragraph(v,style='List Bullet')
    # document.add_paragraph()   # to add empty line after the section

    # Projects section
    projects = add_heading('PROJECTS', level=1,bold=True, color=level_1_heading_color)
    projects.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for _,v in projects_details[list(projects_details.keys())[0]].items():
        document.add_paragraph(v,style='List Bullet')
    # document.add_paragraph()   # to add empty line

    # Education section
    edu = add_heading('EDUCATION', level=1,bold=True, color=level_1_heading_color)
    edu.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for edu in education_details[list(education_details.keys())[0]]:
        for k,v in edu.items():
            key = add_heading((k.upper()), level=3,color=(0, 32, 96))
            key.alignment = WD_ALIGN_PARAGRAPH.LEFT
            if isinstance(v,list):
                for line in v:
                    document.add_paragraph(v,style='List Bullet')
            else:
                run1= key.add_run(f'     {v}')
                run1.bold = False
                run1.font.color.rgb = RGBColor(0, 0, 0)
    # document.add_paragraph()   # to add empty line

    # Awards section
    awards = add_heading('AWARDS', level=1,bold=True, color=level_1_heading_color)
    awards.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for _,v in awards_details[list(awards_details.keys())[0]].items():
        document.add_paragraph(v,style='List Bullet')
    # document.add_paragraph()   # to add empty line

    # Add footer
    footer = document.sections[0].footer
    paragraph = footer.paragraphs[0]
    run = paragraph.add_run()
    run.add_text('Resume - Your Name')
    run.font.size = Pt(8)

    # Get full output path
    # First note down relative path. .. is to go one level up from the script folder.
    relative_output_path = "../generated_output_files"
    # Create the full path to the output folder
    output_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_output_path)
    # generate doc at path
    document.save(f'{output_folder_path}/resume_test_msword_{time.time()}.docx')

    print('\nSuccessfully created word file')


if __name__ == '__main__':
    main()