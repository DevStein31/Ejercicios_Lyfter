import csv

def create_csv_file(output_file, students):

    if not students:
        print("No students registered yet.")
    else:
        with open(output_file, "w", encoding="utf-8", newline="") as file:
            
            headers = students[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students)

