def get_name_student():
    while True: 
        name = input("Enter the student's full name: ")
        if name.strip() == "" or any(letter.isdigit() for letter in name):
            print("Invalid name. Please enter student's full name.")
        else:
            name = name.strip()
            break
    return name


def get_section_student():
    while True:
        section = input("Enter student's section: ")
        if len(section) == 3 and section[0].isdigit() and section[1].isdigit() and section[2].isalpha():
            section = section.upper()
            break
        else:
            print("""Invalid section. Please enter a valid section.
            It must be 2 numbers and 1 letter.
            For example: 10A, 05B, 12S""")
    return section


def is_duplicated_student(students, name, section):
        for student in students:
            if student["name"] == name and student["section"] == section:
                return True
        return False


def get_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the {subject} grade: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Please enter a valid option. It must be a number from 0 to 100.")
        except ValueError:
            print("Please enter a valid option. It must be a number from 0 to 100.")


def register_student(students):
    while True:
        name = get_name_student()
        section = get_section_student()
        duplicate_found = is_duplicated_student(students, name, section)
        
        if duplicate_found:
            print ("This student is already registered. Please enter a different student.")
        else:
            break

    spanish_grade = get_grade("Spanish")
    english_grade = get_grade("English")
    social_studies_grade = get_grade("Social Studies")
    science_grade = get_grade("Science")

    student = {}
    student["name"] = name
    student["section"] = section
    student["spanish_grade"] = spanish_grade
    student["english_grade"] = english_grade
    student["social_studies_grade"] = social_studies_grade
    student["science_grade"] = science_grade

    students.append(student)
    print("Student registered successfully!")

def list_students(students):
    if not students:
        print("No students registered yet.")
    else:
        for student in students:
            print("================================")
            print(f"Name: {student['name']}")
            print(f"Section: {student['section']}")
            print("______________Grades______________")
            print(f"Spanish: {student['spanish_grade']}")
            print(f"English: {student['english_grade']}")
            print(f"Social Studies: {student['social_studies_grade']}")
            print(f"Science: {student['science_grade']}")
            print("================================")


def get_average(student):
        average = (student["spanish_grade"] + student["english_grade"] + student["social_studies_grade"] + student["science_grade"])/4
        return average

def top_three_students(students):
    if not students:
        print("No students registered yet.")
    else:
        sort_average_students = sorted(students, key=get_average, reverse=True)
        top_students = sort_average_students[:3]
        for student in top_students:
            print(f"Student: {student['name']} - Section: {student['section']} - Average: {get_average(student)}")

def overall_average(students):
    total_average = 0
    student_count = 0

    if not students:
        print("No students registered yet.")
    else:
        for student in students:
            average = get_average(student)
            total_average += average
            student_count += 1
        print(f"Average grade of all students: {round(total_average/student_count, 2)}")



