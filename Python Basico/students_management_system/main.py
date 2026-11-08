from menu import get_menu_option
from actions import register_student, list_students, top_three_students, overall_average, export_students, import_students


students = []


if __name__ == "__main__":
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
            case _:
                print("This option is not implemented yet.")