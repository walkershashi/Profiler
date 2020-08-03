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


def generate_resume(details):
    report = SimpleDocTemplate('Resume.pdf')

    styles = getSampleStyleSheet()
    
    name, dob, age = details['Personal Details'].values()
    report_title = Paragraph('Personal Details', styles['h1'])
    report_subtitle = Paragraph(name, styles['h3'])
    
    edu_title = Paragraph('Educational Details', styles['h1'])
    edu_table = build_table(details, 'Educational Qualifications')
    
    work_title = Paragraph('Work Experience', styles['h1'])
    work_table = build_table(details, 'Work Experience')

    project_title = Paragraph('Personal Projects', styles['h1'])
    project_table = build_table(details, 'Personal Projects')

    training_title = Paragraph('Training and Certifications', styles['h1'])
    training_table = build_table(details, 'Training and Certifications')

    volunteer_title = Paragraph('Volunteer Experience/Position of Responsibility', styles['h1'])
    volunteer_table = build_table(details, 'Volunteer Experience/Position of Responsibility')

    report.build([report_title, report_subtitle, edu_title, edu_table, work_title, work_table, project_title, project_table, training_title, training_table, volunteer_title, volunteer_table])
