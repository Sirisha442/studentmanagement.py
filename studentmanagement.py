# python program using  methods in class


class Student:
    def __init__(self, rollnumber, name, age, DOB, address, course, fee, collegename):
        self.rollnumber = rollnumber
        self.name = name
        self.age = age
        self.DOB = DOB
        self.address = address
        self.course = course
        self.fee = fee
        self.collegename = collegename

    def __str__(self):
        return (f"Roll Number: {self.rollnumber}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"DOB: {self.DOB}\n"
                f"Address: {self.address}\n"
                f"Course: {self.course}\n"
                f"Fee: {self.fee}\n"
                f"College: {self.collegename}\n")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, rollnumber, name, age, DOB, address, course, fee, collegename):
        if rollnumber in self.students:
            print("Error: Roll Number already exists.")
        else:
            student = Student(rollnumber, name, age, DOB, address, course, fee, collegename)
            self.students[rollnumber] = student
            print(f"Student {name} added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for rollnumber, student in self.students.items():
                print(student)

    def update_student(self, rollnumber, name=None, age=None, DOB=None, address=None, course=None, fee=None, collegename=None):
        if rollnumber not in self.students:
            print(f"Error: Student with Roll Number {rollnumber} not found.")
        else:
            student = self.students[rollnumber]
            if name: student.name = name
            if age: student.age = age
            if DOB: student.DOB = DOB
            if address: student.address = address
            if course: student.course = course
            if fee: student.fee = fee
            if collegename: student.collegename = collegename
            print(f"Student {rollnumber} updated successfully.")

    def delete_student(self, rollnumber):
        if rollnumber in self.students:
            del self.students[rollnumber]
            print(f"Student with Roll Number {rollnumber} deleted successfully.")
        else:
            print(f"Error: Student with Roll Number {rollnumber} not found.")

    def search_student(self, rollnumber):
        if rollnumber in self.students:
            print(self.students[rollnumber])
        else:
            print(f"Error: Student with Roll Number {rollnumber} not found.")


# Main Function (UI for interacting with the system)
def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            rollnumber = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            DOB = input("Enter Date of Birth (YYYY-MM-DD): ")
            address = input("Enter Address: ")
            course = input("Enter Course: ")
            fee = float(input("Enter Fee: "))
            collegename = input("Enter College Name: ")
            system.add_student(rollnumber, name, age, DOB, address, course, fee, collegename)

        elif choice == '2':
            system.view_students()

        elif choice == '3':
            rollnumber = input("Enter Roll Number to update: ")
            name = input("Enter new Name (leave blank to keep current): ")
            age = input("Enter new Age (leave blank to keep current): ")
            DOB = input("Enter new DOB (leave blank to keep current): ")
            address = input("Enter new Address (leave blank to keep current): ")
            course = input("Enter new Course (leave blank to keep current): ")
            fee = input("Enter new Fee (leave blank to keep current): ")
            collegename = input("Enter new College Name (leave blank to keep current): ")

            system.update_student(
                rollnumber,
                name if name else None,
                int(age) if age else None,
                DOB if DOB else None,
                address if address else None,
                course if course else None,
                float(fee) if fee else None,
                collegename if collegename else None
            )

        elif choice == '4':
            rollnumber = input("Enter Roll Number to delete: ")
            system.delete_student(rollnumber)

        elif choice == '5':
            rollnumber = input("Enter Roll Number to search: ")
            system.search_student(rollnumber)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
