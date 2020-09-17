import json
import PySimpleGUI as GUI

GUI.theme('Purple')	# Add a touch of color

def student_details():
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
    print(values)
    return values

def json_details(candidate_details):

    candidate_json = {
        'Personal Details': {
            'Name': candidate_details[0],
            'DOB': candidate_details[1], 
            'Email': candidate_details[2]
        },
        'Educational Qualifications': [
            {
                'id': 0,
                'Institute Name': candidate_details[3],
                'Degree': candidate_details[4],
                'Duration': candidate_details[5],
                'Percentage': candidate_details[6]
            },
            {
                'id': 1,
                'Institute Name': candidate_details[7],
                'Degree': candidate_details[8],
                'Duration': candidate_details[9],
                'Percentage': candidate_details[10]
            },
            {
                'id': 2,
                'Institute Name': candidate_details[11],
                'Degree': candidate_details[12],
                'Duration': candidate_details[13],
                'Percentage': candidate_details[14]
            },
        ],
        'Skills': [candidate_details[i] for i in range(15, 23)],
        'Work Experience': [
            {
                'id': 0,
                'Company Name': candidate_details[23],
                'Role': candidate_details[24],
                'Duration': candidate_details[25]
            },
            {
                'id': 1,
                'Company Name': candidate_details[26],
                'Role': candidate_details[27],
                'Duration': candidate_details[28]
            }
        ],
        'Personal Projects': [
            {
                'id': 0,
                'Title': candidate_details[29], 
                'Description': candidate_details[30],
                'Link': candidate_details[31],
                'Duration': candidate_details[32]
            },
            {
                'id': 1,
                'Title': candidate_details[33], 
                'Description': candidate_details[34],
                'Link': candidate_details[35],
                'Duration': candidate_details[36]
            },
            {
                'id': 2,
                'Title': candidate_details[37], 
                'Description': candidate_details[38],
                'Link': candidate_details[39],
                'Duration': candidate_details[40]
            },
            {
                'id': 3,
                'Title': candidate_details[41], 
                'Description': candidate_details[42],
                'Link': candidate_details[43],
                'Duration': candidate_details[44]
            },
        ],
        'Training and Certifications': [
            {
                'id': 0,
                'Title': candidate_details[45], 
                'Link': candidate_details[46],
                'Duration': candidate_details[47]
            },
            {
                'id': 1,
                'Title': candidate_details[48], 
                'Link': candidate_details[49],
                'Duration': candidate_details[50]
            },
            {
                'id': 2,
                'Title': candidate_details[51], 
                'Link': candidate_details[52],
                'Duration': candidate_details[53]
            },
            {
                'id': 3,
                'Title': candidate_details[54], 
                'Link': candidate_details[55],
                'Duration': candidate_details[56]
            },
        ],
        'Academic Acheivements': [candidate_details[i] for i in range(57, 61)],
        'Volunteer Experience/Position of Responsibility': [
            {
                'id': 0,
                'Role': candidate_details[61],
                'Description': candidate_details[62],
                'Duration': candidate_details[63]
            },
            {
                'id': 1,
                'Role': candidate_details[64],
                'Description': candidate_details[65],
                'Duration': candidate_details[66]
            }
        ],
        'Hobbies & Interests' : [candidate_details[i] for i in range(67, 73)]
    }
    
    return candidate_json
