# write_messages.py

from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import school

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100, "pdate": "2021.10.01"},
    {"name": "Gergeley", "score": 87, "pdate": "2022.12.09"},
    {"name": "Frieda", "score": 92, "pdate": "2015.06.07"},
    {"name": "Elena", "score": 92, "pdate": "2023.01.07"},
    {"name": "foo", "score": 92, "pdate": "2023.01.12"},

]




environment = Environment(loader=FileSystemLoader("./templates/"))
template = environment.get_template("results.html")


for student in school.students:

    results_filename = "./web/students_results.html"
    results_template = environment.get_template("results.html")
    context = {
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")