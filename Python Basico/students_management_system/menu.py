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
