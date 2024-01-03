from docx import Document
from docx.shared import Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import json,yaml,time,os

class FormatMSword():

    def __init__(self) -> None:
        self.document=Document()
 
    def read_yaml(self,path):
        with open(path, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)

    def get_full_path(self,section):
        # Define the relative path to the resume section files
        relative_path = "../section_yaml_files"
        # Create the full path to the output folder
        output_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
        section_file_path_yaml = f'{output_folder_path}/resume_{section}.yaml'
        return section_file_path_yaml

    def heading(self,text, level, bold=True, color=(0, 0, 0),align=WD_ALIGN_PARAGRAPH.LEFT):
        '''Re-writing add_heading function of Document() for 
            our requirements.'''
        heading_added = self.document.add_heading(text, level=level)
        heading_added.alignment =align
        run = heading_added.runs[0]
        run.bold = bold
        run.font.color.rgb = RGBColor(*color)
        return heading_added


def main():
    # Create a new Word document instance
    doc=FormatMSword()

    # Add a title and contact
    doc.heading('YOUR NAME', level=0,bold=True, color=(255, 0, 0))
    doc.heading('0422332233, email@gmail.com', level=9,bold=False,align=WD_ALIGN_PARAGRAPH.RIGHT)

    # Specify the yaml file path of all sections
    file_path_exp = doc.get_full_path('experience')
    file_path_skill = doc.get_full_path('skill')
    file_path_education = doc.get_full_path('education')
    file_path_projects = doc.get_full_path('projects')
    file_path_awards = doc.get_full_path('awards')

    # Read the JSON file back into a dictionary
    exp_details = doc.read_yaml(file_path_exp)
    skill_details = doc.read_yaml(file_path_skill)
    education_details = doc.read_yaml(file_path_education)
    projects_details = doc.read_yaml(file_path_projects)
    awards_details = doc.read_yaml(file_path_awards)

    # level 1 heading color
    level_1_heading_color=(255, 0, 0)

    # Add EXPERIENCE section heading
    doc.heading('EXPERIENCE', level=1, bold=True, color=level_1_heading_color)

    # Iterate through experience details
    for exp in exp_details[list(exp_details.keys())[0]]:
        for k,v in exp.items():

            if k.lower().strip() == 'employer':
                key = doc.heading((k.upper()), level=3,color=(0, 32, 96))

                if isinstance(v,list):
                    for line in v:
                        doc.document.add_paragraph(line,style='List Bullet')
                else:
                    run= key.add_run(f'     {v}')
                    run.bold = True
                    run.font.color.rgb = RGBColor(0, 0, 0)
            else:
                key = doc.heading((k.upper()), level=3, color=(0, 32, 96))

                if isinstance(v,list):
                    for line in v:
                        doc.document.add_paragraph(line,style='List Bullet')
                else:
                    run= key.add_run(f'     {v}')
                    run.bold = False
                    run.font.color.rgb = RGBColor(0, 0, 0)
                
        doc.document.add_paragraph()   # to add empty line
    # doc.document.add_page_break() # Add Page break after experience

    # Skill section
    skills = doc.heading('SKILLS', level=1,bold=True, color=level_1_heading_color)
    skills.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for _,v in skill_details[list(skill_details.keys())[0]].items():
        doc.document.add_paragraph(v,style='List Bullet')
    # doc.document.add_paragraph()   # to add empty line after the section

    # Projects section
    projects = doc.heading('PROJECTS', level=1,bold=True, color=level_1_heading_color)
    projects.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for _,v in projects_details[list(projects_details.keys())[0]].items():
        doc.document.add_paragraph(v,style='List Bullet')
    # doc.document.add_paragraph()   # to add empty line

    # Education section
    edu = doc.heading('EDUCATION', level=1,bold=True, color=level_1_heading_color)
    edu.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for edu in education_details[list(education_details.keys())[0]]:
        for k,v in edu.items():
            key = doc.heading((k.upper()), level=3,color=(0, 32, 96))
            key.alignment = WD_ALIGN_PARAGRAPH.LEFT
            if isinstance(v,list):
                for line in v:
                    doc.document.add_paragraph(v,style='List Bullet')
            else:
                run= key.add_run(f'     {v}')
                run.bold = False
                run.font.color.rgb = RGBColor(0, 0, 0)
    # doc.document.add_paragraph()   # to add empty line

    # Awards section
    awards = doc.heading('AWARDS', level=1,bold=True, color=level_1_heading_color)
    awards.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for _,v in awards_details[list(awards_details.keys())[0]].items():
        doc.document.add_paragraph(v,style='List Bullet')
    # doc.document.add_paragraph()   # to add empty line

    # Add footer
    footer = doc.document.sections[0].footer
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
    doc.document.save(f'{output_folder_path}/resume_test_msword_{time.time()}.docx')

    print('\nSuccessfully created word file')


if __name__ == '__main__':
    main()