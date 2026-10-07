# STUDENT MANAGEMENT SYSTEM
# Created by Gobinda Bogati (Student ID: 1900155)

# Store students in a list
students = []

# here by using while loop we use to Keep displaying the menu until the user chooses Exit
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #  creating condition to Add new Student
    if choice == "1":

        name = input("Enter student name: ")
        mark = int(input("Enter student mark: "))
        
        

        # using the grade system to  Categorise the student's grade
        if mark >= 85:
            grade = "HD"
        elif mark >= 75:
            grade = "D"
        elif mark >= 65:
            grade = "C"
        elif mark >= 50:
            grade = "P"
        else:
            grade = "F"

        # this will Store student name and grade
        students.append((name, grade))

        print("Student added successfully.")
        # this will display  name and grade of student. 
        print("Name:", name)
        print("Grade:", grade)

    # logic to Remove Student
    elif choice == "2":

        name = input("Enter student name to remove: ")

        for student in students:
            if student[0] == name:
                students.remove(student) #this wiill remove the studnet record. 
                print("Student removed successfully.")
                break
        else:
            print("Student not found.")

    #  creating the menu and conditions for Viewing  Students details.
    elif choice == "3":

        if len(students) == 0:
            print("No students available.")
        else:
            print("\n===== STUDENT LIST =====")

            for student in students:
                print("Name:", student[0], "| Grade:", student[1])

    # Exit
    elif choice == "4":

        print("Exiting Student Management System.")
        break

    #  if the choice is Invalid it will display the msg to select the valid choice
    else:

        print("Invalid choice. Please select 1, 2, 3 or 4.")