def get_name_student():
    while True: 
        name = input("Enter the student's full name: ")
        if name.strip() == "" or any(letter.isdigit() for letter in name):
            print("Invalid name. Please enter student's full name.")
        else:
            name = " ".join(name.split())
            break
    return name


def get_section_student():
    while True:
        section = input("Enter student's section: ")
        if len(section) == 3 and section[0].isdigit() and section[1].isdigit() and section[2].isalpha():
            section = section.upper()
            break
        else:
            print("Invalid section. Please enter a valid section")
            print("It must be 2 numbers and 1 letter.")
            print("For example: 10A, 05B, 12S")
    return section


def is_duplicated_student(students, name, section):
    for student in students:
        if student["name"].lower() == name.lower() and student["section"] == section:
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
        try:
            students_count = int(input("How many students do you want to register? "))
            if students_count <= 0:
                print("The number of students must be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    for _ in range(students_count):
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
        print("")


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
            print(f"Student: {student['name']} - Section: {student['section']} - Average: {get_average(student):.2f}")


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


def get_failing_grades(student):
    failed_subjects = []
        
    for subject, grade in student.items():
        if subject.endswith("_grade"):
            if grade < 60: 
                failed_subjects.append(f"{subject.replace('_grade', '').replace('_', ' ').title()}: {grade}")
    return failed_subjects


def failing_grades(students):
    if not students:
        print("No students registered yet.")
    else:
        has_failing_students = False
        for student in students:
            failed_subjects = get_failing_grades(student)
            
            if failed_subjects:
                print("================================")
                print(f"Name: {student['name']}")
                print(f"Section: {student['section']}")
                print("Failed subjects:")
                has_failing_students = True
                
                for grade in failed_subjects:
                    print(grade)

                print("================================")
        if not has_failing_students:
            print("No failing students found")


def delete_student(students):
    if not students:
        print("No students registered yet.")
    else:
        student_name = get_name_student()
        student_section = get_section_student()

        for student in students:
            if student["name"].lower() == student_name.lower() and student["section"] ==student_section:
                confirmation = input("Are you sure you want to delete this student? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    students.remove(student)
                    print("Student deleted successfully.")
                else:
                    print("Student deletion cancelled.")
                break
        else:
            print("Student not found!")

