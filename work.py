1.
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

2.
grades = {}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Display All")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade: ")
            grades[name] = grade
        else:
            print("Student not found.")
    elif choice == '3':
        for name, grade in grades.items():
            print(f"{name}: {grade}")
    elif choice == '4':
        break
    else:
        print("Invalid choice")

3.
with open("python.txt", "w") as file:
    file.write("My name is Jatin.\n")
    file.write("Python file write operation successful.")

4.
with open("python.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

