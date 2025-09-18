student_grades = {}

# Add
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a marks {grade}")


def display_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("no students found\addede")        


# Update
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} not found! ")

# Delete
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been sucessfully deleted ")
    else:
        print(f"{name} not found! ")




def main():
    while True:

        print("\n student grade magement system....")
        print("1. Add ")
        print("2. View ")
        print("3. Update ")
        print("4. Delete ")
        print("5. Exit ")

        choice = int(input("enter your choice: "))

        if choice == 1:
            name = input("Enter Student Name: ")
            grade = int(input("Enter Student grades: "))
            add_student(name, grade)

        elif choice == 2:
            display_student()

        elif choice == 3:
            name = input("Enter Student Name: ")
            grade = int(input("Enter Student grades: "))
            update_student(name, grade)

        elif choice == 4:
            name = input("Enter Student Name: ")
            delete_student(name)

        elif choice == 5:
            print("Closing the program")
            break
        else:
            print("Invalid Choice ")
    

if __name__ == "__main__":
    main()



    