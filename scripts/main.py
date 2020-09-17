import resume_gui as rg
import resume_generater as r_gen

student_info = rg.student_details()

candidate_details = rg.json_details(student_info)

r_gen.generate_resume(candidate_details)