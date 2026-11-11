from actions import register_student, list_students, top_three_students, overall_average, export_students, import_students, failing_grades, delete_student

def show_menu():
    print("""===== STUDENT MANAGEMENT SYSTEM =====

    1. Register students
    2. List all students
    3. Show top 3 students
    4. Show overall average
    5. Export students to CSV
    6. Import students from CSV
    7. Show students with failing grades
    8. Delete a student
    0. Exit""")


def get_menu_option():
    while True:
        show_menu()
        try:
            option = int(input("Select an option: "))
            if 0 <= option <= 8:
                return option
            else:
                print("Please enter a valid option. It must be a number from 0 to 8.")
        except ValueError:
            print("Please enter a valid option. It must be a number from 0 to 8.")


def run_menu(students):
    while True:
        option = get_menu_option()
        match option:
            case 0:
                print("Thank you, see you later!")
                break
            case 1:
                register_student(students)
            case 2:
                list_students(students)
            case 3:
                top_three_students(students)
            case 4:
                overall_average(students)
            case 5:
                export_students(students)
            case 6:
                import_students(students)
            case 7:
                failing_grades(students)
            case 8:
                delete_student(students)
            case _:
                print("This option is not implemented yet.")
