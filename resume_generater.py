import json
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image

styles = getSampleStyleSheet()

def build_table(info, table_title):
    keys = list(info[table_title][0].keys())

    try:
        keys.remove('id')
    except:
        pass
    table_details = []

    '''for i in keys:
        if i != 'id' or i != 'Link' or i != 'CertificationLink':
            table_details.append(i)'''
    
    table_details.append(keys)
    
    for i in info[table_title]:
        row_i = []
        for val in keys:
            if val == 'Link' or val == 'CertificationLink':
                link = '<link href="{}">{}</link>'.format(i[val], i['Title'])
                row_i.append(Paragraph(link, ParagraphStyle('body')))
            else:
                row_i.append(Paragraph(str(i[val]), styles['BodyText']))

        table_details.append(row_i)
    
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.blueviolet)]
    
    table_ = Table(
        data = table_details,
        style = table_style,
        hAlign = 'LEFT'
    )

    return table_

def list_table(list_):
    table_data = []
    
    for ind, sk in enumerate(list_):
        table_data.append([ind + 1, sk])
    
    skill_table = Table(
        data = table_data,
        hAlign = 'LEFT'
    )

    return skill_table

def generate_resume(details):
    report = SimpleDocTemplate('Resume.pdf')
    
    name, dob, email = details['Personal Details'].values()
    
    detail_title = Paragraph('<bullet>&bull;</bullet>Personal Details', styles['h1'])
    
    detail_table = Table(
        data = [[key, val] for key, val in details['Personal Details'].items()],
        hAlign = 'CENTER'
    )

    edu_title = Paragraph('<bullet>&bull;</bullet>Educational Details', styles['h1'])
    edu_table = build_table(details, 'Educational Qualifications')
    
    work_title = Paragraph('<bullet>&bull;</bullet>Work Experience', styles['h1'])
    work_table = build_table(details, 'Work Experience')

    skills_title = Paragraph('<bullet>&bull;</bullet>Skills', styles['h1'])
    skills_table = list_table(details['Skills'])

    project_title = Paragraph('<bullet>&bull;</bullet>Personal Projects', styles['h1'])
    project_table = build_table(details, 'Personal Projects')

    training_title = Paragraph('<bullet>&bull;</bullet>Training and Certifications', styles['h1'])
    training_table = build_table(details, 'Training and Certifications')

    volunteer_title = Paragraph('<bullet>&bull;</bullet>Volunteer Experience/Position of Responsibility', styles['h1'])
    volunteer_table = build_table(details, 'Volunteer Experience/Position of Responsibility')

    acad_title = Paragraph('<bullet>&bull;</bullet>Academic Acheivements', styles['h1'])
    acad_table = list_table(details['Academic Acheivements'])

    hobi_title = Paragraph('<bullet>&bull;</bullet>Hobbies & Interests', styles['h1'])
    hobi_table = list_table(details['Hobbies & Interests'])

    report.build([detail_title, detail_table, edu_title, edu_table, work_title, work_table, skills_title, skills_table, project_title, project_table, training_title, training_table, volunteer_title, volunteer_table, acad_title, acad_table, hobi_title, hobi_table])


with open('candidate_details.json', 'r') as json_file:
    json_data = json.load(json_file)

generate_resume(json_data)