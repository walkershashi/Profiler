import json
import platform
import subprocess
import scripts.resume_generater as r_gen
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user/data", methods = ['GET', 'POST'])
def get_user_data():
    if request.method == 'POST':
        return render_template('user_data.html')

@app.route("/generate=true", methods = ['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        
        candidate_json = {
            'Personal Details': {
                'Name': request.form['fname'] + request.form['mname'] + request.form['lname'],
                'DOB': request.form['dob'],
                'Email': request.form['email'],
            },
            'Educational Qualifications': [
                {
                    'id': 0,
                    'Institute Name': request.form['edu_1_name'],
                    'Degree': request.form['edu_1_degree'],
                    'Duration': request.form['edu_1_dur'],
                    'Percentage': request.form['edu_1_percent']
                },
                {
                    'id': 1,
                    'Institute Name': request.form['edu_2_name'],
                    'Degree': request.form['edu_2_degree'],
                    'Duration': request.form['edu_2_dur'],
                    'Percentage': request.form['edu_2_percent']
                },
                {
                    'id': 2,
                    'Institute Name': request.form['edu_3_name'],
                    'Degree': request.form['edu_3_degree'],
                    'Duration': request.form['edu_3_dur'],
                    'Percentage': request.form['edu_3_percent']
                },
            ],
            'Skills': [request.form['skill_{}'.format(i)] for i in range(1, 6)],
            'Work Experience': [
                {
                    'id': 0,
                    'Company Name': request.form['work_1_cmp'],
                    'Role': request.form['work_1_role'],
                    'Duration': request.form['work_1_dur']
                },
                {
                    'id': 1,
                    'Company Name': request.form['work_2_cmp'],
                    'Role': request.form['work_2_role'],
                    'Duration': request.form['work_2_dur']
                },
                {
                    'id': 2,
                    'Company Name': request.form['work_3_cmp'],
                    'Role': request.form['work_3_role'],
                    'Duration': request.form['work_3_dur']
                }
            ],
            'Personal Projects': [
                {
                    'id': 0,
                    'Title': request.form['proj_1_name'], 
                    'Description': request.form['proj_1_des'],
                    'Link': request.form['proj_1_link'],
                    'Duration': request.form['proj_1_dur']
                },
                {
                    'id': 1,
                    'Title': request.form['proj_2_name'], 
                    'Description': request.form['proj_2_des'],
                    'Link': request.form['proj_2_link'],
                    'Duration': request.form['proj_2_dur']
                },
                {
                    'id': 2,
                    'Title': request.form['proj_3_name'], 
                    'Description': request.form['proj_3_des'],
                    'Link': request.form['proj_3_link'],
                    'Duration': request.form['proj_3_dur']
                },
                {
                    'id': 3,
                    'Title': request.form['proj_4_name'], 
                    'Description': request.form['proj_4_des'],
                    'Link': request.form['proj_3_link'],
                    'Duration': request.form['proj_4_dur']
                },
            ],
            'Training and Certifications': [
                {
                    'id': 0,
                    'Title': request.form['training_1_name'], 
                    'Link': request.form['training_1_link'],
                    'Duration': request.form['training_1_dur']
                },
                {
                    'id': 1,
                    'Title': request.form['training_2_name'], 
                    'Link': request.form['training_2_link'],
                    'Duration': request.form['training_2_dur']
                },
                {
                    'id': 2,
                    'Title': request.form['training_3_name'], 
                    'Link': request.form['training_3_link'],
                    'Duration': request.form['training_3_dur']
                },
                {
                    'id': 3,
                    'Title': request.form['training_4_name'], 
                    'Link': request.form['training_4_link'],
                    'Duration': request.form['training_4_dur']
                },
            ],
            'Academic Acheivements': [request.form['acad_{}'.format(i)] for i in range(1, 6)],
            'Volunteer Experience/Position of Responsibility': [
                {
                    'id': 0,
                    'Role': request.form['por_1_role'],
                    'Description': request.form['por_1_des'],
                    'Duration': request.form['por_1_dur']
                },
                {
                    'id': 1,
                    'Role': request.form['por_2_role'],
                    'Description': request.form['por_2_des'],
                    'Duration': request.form['por_2_dur']
                }
            ],
            'Hobbies & Interests' : [request.form['hobby_{}'.format(i)] for i in range(1, 6)]
        }

        # Generate the Resume
        r_gen.generate_resume(candidate_json)
        
        with open('templates/generated.html', 'w') as html_file:
            html_file.write('''
            <!DOCTYPE html>
            <html>
                <body>
                    <embed src={{ url_for('static', filename="pdf/Resume.pdf") }} width="1500px" height="2000px" />
                </body>
            </html>
            '''
            )

        return render_template('generated.html')

if __name__ == '__main__':
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        subprocess.run('pip3 install -r requirements.txt')
    
    elif platform.system() == 'Windows':
        subprocess.run('pip install -r requirements.txt')

    app.run(debug = True)
