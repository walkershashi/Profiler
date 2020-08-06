import json
import PySimpleGUI as GUI

GUI.theme('Purple')	# Add a touch of color

def basic():
    # All the stuff inside your window.

    layout = [
        [GUI.Button('Personal Details')],
        [
            GUI.Text('Name:'), GUI.InputText(), 
            GUI.Text('DOB:'), GUI.InputText(),
            GUI.Text('Email:'), GUI.InputText()
        ],
        [GUI.Button('Educational Qualifications')],
        [
            GUI.Text('Institue Name:'), GUI.InputText(), 
            GUI.Text('Degree:'), GUI.InputText(), 
            GUI.Text('From-To:'), GUI.InputText(), 
            GUI.Text('%:'), GUI.InputText()
        ],
        [
            GUI.Text('Institue Name:'), GUI.InputText(), 
            GUI.Text('Degree:'), GUI.InputText(), 
            GUI.Text('From-To:'), GUI.InputText(), 
            GUI.Text('%:'), GUI.InputText()
        ],
        [
            GUI.Text('Institue Name:'), GUI.InputText(), 
            GUI.Text('Degree:'), GUI.InputText(), 
            GUI.Text('From-To:'), GUI.InputText(), 
            GUI.Text('%:'), GUI.InputText()
        ],
        [GUI.Button('Skills')],
        [
            GUI.Text(''), GUI.InputText(), GUI.InputText(), GUI.InputText(), GUI.InputText() 
        ],
        [
            GUI.Text(''), GUI.InputText(), GUI.InputText(), GUI.InputText(), GUI.InputText()
        ],
        [
            GUI.Button('Ok'), GUI.Button('Cancel')
        ]
    ]

    window = GUI.Window('Resumer', layout)

    # Event Loop to process "events" and get the "values" of the inputs

    while True:
        event, values = window.read()

        if event == GUI.WIN_CLOSED or event == 'Cancel':
            break

        if event == 'Ok' and all(len(j) > 0 for j in values.values()):
            break
        
    window.close()
    return values


def proffesional():
    layout = [
        [GUI.Button('Work Experience')],
        [
            GUI.Text('Company Name:'), GUI.InputText(),
            GUI.Text('Role:'), GUI.InputText(),
            GUI.Text('From-To:'), GUI.InputText()
        ],
        [
            GUI.Text('Company Name:'), GUI.InputText(),
            GUI.Text('Role:'), GUI.InputText(),
            GUI.Text('From-To:'), GUI.InputText()
        ],
        [GUI.Button('Personal Projects')],
        [
            GUI.Text('Title:'), GUI.InputText(),
            GUI.Text('Description:'), GUI.InputText(),
            GUI.Text('Links:'), GUI.InputText(),
            GUI.Text('From-To:'), GUI.InputText()
        ],
        [
            GUI.Text('Title:'), GUI.InputText(),
            GUI.Text('Description:'), GUI.InputText(),
            GUI.Text('Links:'), GUI.InputText(),
            GUI.Text('From-To:'), GUI.InputText()
        ],
        [
            GUI.Text('Title:'), GUI.InputText(),
            GUI.Text('Description:'), GUI.InputText(),
            GUI.Text('Links:'), GUI.InputText(),
            GUI.Text('From-To:'), GUI.InputText()
        ],
        [
            GUI.Text('Title:'), GUI.InputText(),
            GUI.Text('Description:'), GUI.InputText(),
            GUI.Text('Links:'), GUI.InputText(),
            GUI.Text('From-To:'), GUI.InputText()
        ],
        [GUI.Button("Training and Certifications")],
        [
            GUI.Text('Title:'), GUI.InputText(), 
            GUI.Text('Certification Link:'), GUI.InputText(), 
            GUI.Text('Duration:'), GUI.InputText()
        ],
        [
            GUI.Text('Title:'), GUI.InputText(), 
            GUI.Text('Certification Link:'), GUI.InputText(), 
            GUI.Text('Duration:'), GUI.InputText()
        ],
        [
            GUI.Text('Title:'), GUI.InputText(), 
            GUI.Text('Certification Link:'), GUI.InputText(), 
            GUI.Text('Duration:'), GUI.InputText()
        ],
        [
            GUI.Text('Title:'), GUI.InputText(), 
            GUI.Text('Certification Link:'), GUI.InputText(), 
            GUI.Text('Duration:'), GUI.InputText()
        ],
        [
            GUI.Button('Ok'), GUI.Button('Cancel')
        ]
    ]

    # Create the Window
    window = GUI.Window('Resumer', layout)

    # Event Loop to process "events" and get the "values" of the inputs

    while True:
        event, values = window.read()

        if event == GUI.WIN_CLOSED or event == 'Cancel':
            break

        if event == 'Ok' and all(len(j) > 0 for j in values.values()):
            break
        
    window.close()
    return values

def others():
    layout = [
        [GUI.Button('Acadamic Acheivements')],
        [
            GUI.Text(''), GUI.InputText(), GUI.InputText(), GUI.InputText(), GUI.InputText() 
        ],
        [GUI.Button('Volunteer Experience/Position of Responsibility')],
        [
            GUI.Text('Role:'), GUI.InputText(),
            GUI.Text('Description:'), GUI.InputText(),
            GUI.Text('From-To:'), GUI.InputText()
        ],
        [
            GUI.Text('Role:'), GUI.InputText(),
            GUI.Text('Description:'), GUI.InputText(),
            GUI.Text('From-To:'), GUI.InputText()
        ],
        [GUI.Button('Hobbies & Interests')],
        [
            GUI.Text(''), GUI.InputText(), GUI.InputText(), GUI.InputText() 
        ],
        [
            GUI.Text(''), GUI.InputText(), GUI.InputText(), GUI.InputText()
        ],
        [
            GUI.Button('Ok'), GUI.Button('Cancel')
        ]
    ]

    # Create the Window
    window = GUI.Window('Resumer', layout)

    # Event Loop to process "events" and get the "values" of the inputs

    while True:
        event, values = window.read()

        if event == GUI.WIN_CLOSED or event == 'Cancel':
            break

        if event == 'Ok' and all(len(j) > 0 for j in values.values()):
            break
        
    window.close()
    return values


def json_details(candidate_details1, candidate_details2, candidate_details3):

    candidate_json = {
        'Personal Details': {
            'Name': candidate_details1[0],
            'DOB': candidate_details1[1], 
            'Email': candidate_details1[2]
        },
        'Educational Qualifications': [
            {
                'id': 0,
                'Institute Name': candidate_details1[3],
                'Degree': candidate_details1[4],
                'Duration': candidate_details1[5],
                'Percentage': candidate_details1[6]
            },
            {
                'id': 1,
                'Institute Name': candidate_details1[7],
                'Degree': candidate_details1[8],
                'Duration': candidate_details1[9],
                'Percentage': candidate_details1[10]
            },
            {
                'id': 2,
                'Institute Name': candidate_details1[11],
                'Degree': candidate_details1[12],
                'Duration': candidate_details1[13],
                'Percentage': candidate_details1[14]
            },
        ],
        'Skills': [candidate_details1[i] for i in range(15, 23)],
        'Work Experience': [
            {
                'id': 0,
                'Company Name': candidate_details2[0],
                'Role': candidate_details2[1],
                'Duration': candidate_details2[2]
            },
            {
                'id': 1,
                'Company Name': candidate_details2[3],
                'Role': candidate_details2[4],
                'Duration': candidate_details2[5]
            }
        ],
        'Personal Projects': [
            {
                'id': 0,
                'Title': candidate_details2[6], 
                'Description': candidate_details2[7],
                'Link': candidate_details2[8],
                'Duration': candidate_details2[9]
            },
            {
                'id': 1,
                'Title': candidate_details2[10], 
                'Description': candidate_details2[11],
                'Link': candidate_details2[12],
                'Duration': candidate_details2[13]
            },
            {
                'id': 2,
                'Title': candidate_details2[14], 
                'Description': candidate_details2[15],
                'Link': candidate_details2[16],
                'Duration': candidate_details2[17]
            },
            {
                'id': 3,
                'Title': candidate_details2[18], 
                'Description': candidate_details2[19],
                'Link': candidate_details2[20],
                'Duration': candidate_details2[21]
            },
        ],
        'Training and Certifications': [
            {
                'id': 0,
                'Title': candidate_details2[22], 
                'CertificationLink': candidate_details2[23],
                'Duration': candidate_details2[24]
            },
            {
                'id': 1,
                'Title': candidate_details2[25], 
                'CertificationLink': candidate_details2[26],
                'Duration': candidate_details2[27]
            },
            {
                'id': 2,
                'Title': candidate_details2[28], 
                'CertificationLink': candidate_details2[29],
                'Duration': candidate_details2[30]
            },
            {
                'id': 3,
                'Title': candidate_details2[31], 
                'CertificationLink': candidate_details2[32],
                'Duration': candidate_details2[33]
            },
        ],
        'Academic Acheivements': [candidate_details3[i] for i in range(4)],
        'Volunteer Experience/Position of Responsibility': [
            {
                'id': 0,
                'Role': candidate_details3[4],
                'Description': candidate_details3[5],
                'Duration': candidate_details3[6]
            },
            {
                'id': 1,
                'Role': candidate_details3[7],
                'Description': candidate_details3[8],
                'Duration': candidate_details3[9]
            }
        ],
        'Hobbies & Interests' : [candidate_details3[i] for i in range(10, 16)]
    }
    

    return candidate_json
