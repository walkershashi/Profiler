import resume_gui as rg
import resume_generater as r_gen

values1 = rg.basic()

values2 = rg.proffesional()

values3 = rg.others()

candidate_details = rg.json_details(values1, values2, values3)

r_gen.generate_resume(candidate_details)