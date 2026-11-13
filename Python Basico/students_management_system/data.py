import csv
from actions import is_duplicated_student
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


def export_students(students):
    export_csv_name = input("Please enter the CSV file name: ")
    create_csv_file(export_csv_name, students)

            
def import_csv_file(input_file, students):
    project_folder = Path(__file__).parent
    csv_path = project_folder / input_file

    with open(csv_path, "r", encoding="utf-8", newline="") as file:        
        reader = csv.DictReader(file)

        required_columns = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_studies_grade",
            "science_grade"
        ]

        if not reader.fieldnames or not all(column in reader.fieldnames for column in required_columns):
            raise ValueError("Invalid CSV structure.")

        imported_students = []
        for student in reader:
            student["spanish_grade"] = float(student["spanish_grade"])
            student["english_grade"] = float(student["english_grade"])
            student["social_studies_grade"] = float(student["social_studies_grade"])
            student["science_grade"] = float(student["science_grade"])

            grades = [
                student["spanish_grade"],
                student["english_grade"],
                student["social_studies_grade"],
                student["science_grade"]
            ]

            if not all(0 <= grade <= 100 for grade in grades):
                raise ValueError("Grades must be between 0 and 100.")

            
            if not is_duplicated_student(students + imported_students, student["name"], student["section"]):
                imported_students.append(student)

        students.extend(imported_students)


def import_students(students):
    while True:
        try:
            import_csv_name = input("Please enter the CSV file name: ")
            import_csv_file(import_csv_name, students)
            break
        except FileNotFoundError:
            print("CSV file not found.")
        except ValueError as error:
            print(f"Invalid CSV file: {error}")