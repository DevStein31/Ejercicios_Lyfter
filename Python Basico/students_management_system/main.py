from menu import get_menu_option
from actions import register_student, list_students


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
            case _:
                print("This option is not implemented yet.")