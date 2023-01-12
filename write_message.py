# write_messages.py

from jinja2 import Environment, FileSystemLoader
import school

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100, "date": "2021.10.10"},
    {"name": "Gergeley", "score": 87, "date": "2022.12.10"},
    {"name": "Frieda", "score": 92, "date": "2022.06.07"},
    {"name": "Elena", "score": 92, "date": "2023.01.07"},

]

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("results.html")

for student in school.students:
    filename = f"message_{student['name'].lower()}.txt"
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")

results_filename = "students_results.html"
results_template = environment.get_template("results.html")
context = {
    "students": students,
    "test_name": test_name,
    "max_score": max_score,
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")