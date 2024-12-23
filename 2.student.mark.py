class Student:
    def __init__(self, student_id, name, dob): #__init__ to create a new object, __ is to protect the in4(encapsulation)
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self): #create function get_id to get the id of student(input the in4 from keyboard)
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, DoB: {self.__dob}"


class Course:#create class Course
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def __str__(self):# the function __str__ is to show the in4 of course and student, I use the same function in both class Student and Course, but it is not the same effect(polymorphism)
        return f"ID: {self.__course_id}, Name: {self.__name}"


class Mark:
    def __init__(self):
        self.__marks = {}

    def add_mark(self, course_id, student_id, mark):
        if course_id not in self.__marks:
            self.__marks[course_id] = {}
        self.__marks[course_id][student_id] = mark

    def get_marks(self, course_id):
        return self.__marks.get(course_id, {})


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students): #range is to create numvers from 0 to -1, for _ in is not using the value of variable
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth: ")
            self.students.append(Student(student_id, name, dob)) #append is to add the student which has been input to the last position of the row
            print("Student added successfully\n")

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))
            print("Course added successfully\n")

    def input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        if not any(course.get_id() == course_id for course in self.courses):
            print("Course not found\n")
            return

        for student in self.students:
            mark = float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
            self.marks.add_mark(course_id, student.get_id(), mark)
        print("Marks added successfully\n")

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(course)

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(student)

    def show_marks(self):
        course_id = input("Enter the course ID to view marks: ")
        marks = self.marks.get_marks(course_id)
        if not marks:
            print("No marks found for this course\n")
            return

        course_name = next((course.get_name() for course in self.courses if course.get_id() == course_id), "Unknown")
        print(f"Marks for course: {course_name}")
        for student in self.students:
            mark = marks.get(student.get_id(), "N/A")
            print(f"{student.get_name()} (ID: {student.get_id()}): {mark}")

    def main(self):
        while True:
            print("\nStudent Mark Management System")
            print("1. Input student information")
            print("2. Input course information")
            print("3. Input marks for a course")
            print("4. List all courses")
            print("5. List all students")
            print("6. Show student marks for a course")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                self.show_marks()
            elif choice == "7":
                print("Exiting the system. Thanks for using.")
                break
            else:
                print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    manage = StudentMarkManagement()
    manage.main()
