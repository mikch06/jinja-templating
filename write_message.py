# write_messages.py

from jinja2 import Environment, FileSystemLoader
import school

max_score = 100
test_name = "Python Challenge"


environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("message.html")

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
