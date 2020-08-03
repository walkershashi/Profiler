import resume_gui as rg
import resume_generater as r_gen

values = rg.displayGui()
candidate_details = rg.json_details(values)

r_gen.generate_resume(candidate_details)