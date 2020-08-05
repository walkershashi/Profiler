import json
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image

def build_table(info, table_title):
    keys = list(info[table_title][0].keys())
    
    try:
        keys.remove('id')
    except:
        pass
    
    table_details = [keys]

    for i in info[table_title]:
        row_i = []
        for val in keys:
            if val != 'id':
                if len(i[val]) > 35:
                    row_i.append(i[val][:15])
                else:
                    row_i.append(i[val])

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

    styles = getSampleStyleSheet()
    
    name, dob, email = details['Personal Details'].values()
    
    detail_title = Paragraph('Personal Details', styles['h1'])
    detail_table = Table(
        data = [[key, val] for key, val in details['Personal Details'].items()],
        hAlign = 'CENTER'
    )

    edu_title = Paragraph('<br/>Educational Details<br/>', styles['h1'])
    edu_table = build_table(details, 'Educational Qualifications')
    
    work_title = Paragraph('<br/>Work Experience<br/>', styles['h1'])
    work_table = build_table(details, 'Work Experience')

    skills_title = Paragraph('<br/>Skills', styles['h1'])
    skills_table = list_table(details['Skills'])

    project_title = Paragraph('<br/>Personal Projects<br/>', styles['h1'])
    project_table = build_table(details, 'Personal Projects')

    training_title = Paragraph('<br/><br/><br/>Training and Certifications', styles['h1'])
    training_table = build_table(details, 'Training and Certifications')

    volunteer_title = Paragraph('<br/>Volunteer Experience/Position of Responsibility', styles['h1'])
    volunteer_table = build_table(details, 'Volunteer Experience/Position of Responsibility')

    acad_title = Paragraph('<br/>Academic Acheivements', styles['h1'])
    acad_table = list_table(details['Academic Acheivements'])

    hobi_title = Paragraph('<br/>Hobbies & Interests', styles['h1'])
    hobi_table = list_table(details['Hobbies & Interests'])

    report.build([detail_title, detail_table, edu_title, edu_table, work_title, work_table, skills_title, skills_table, project_title, project_table, training_title, training_table, volunteer_title, volunteer_table, acad_title, acad_table, hobi_title, hobi_table])

with open('candidate_details.json', 'r') as json_file:
    json_data = json.load(json_file)

generate_resume(json_data)