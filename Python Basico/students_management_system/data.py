import csv
from pathlib import Path


def create_csv_file(output_file, students):
    project_folder = Path(__file__).parent
    if not students:
        print("No students registered yet.")
    else:
        csv_path = project_folder / output_file
        with open(csv_path, "w", encoding="utf-8", newline="") as file:
            
            headers = students[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students)

def import_csv_file(input_file, students):
    project_folder = Path(__file__).parent
    csv_path = project_folder / input_file
    with open(csv_path, "r", encoding="utf-8", newline="") as file:        
        reader = csv.DictReader(file)
        for student in reader:
            student["spanish_grade"] = float(student["spanish_grade"])
            student["english_grade"] = float(student["english_grade"])
            student["social_studies_grade"] = float(student["social_studies_grade"])
            student["science_grade"] = float(student["science_grade"])
            students.append(student)