USTH ICT 2024 Advanced Programming with Python
=====================================================

Students are expected to:
* Fork this repository to your github account
* Push your commits regularly, with **proper** commit messages

students = [] #list tuple of students, which a list contains name, id, dob
courses = [] #tuple contains courses id, name
marks = {} #tuple using dictionary to save all marks of student, func: student_id: mark
#enter in4 of students
def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students): #range is create a list num from 0 to num_student - 1
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth: ")
        students.append((student_id, name, dob)) #add student into the list(tuple)
        print("Students added successfully\n")

#enter in4 of courses       
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append((course_id, name))
        print("Courses added successfully\n")

#enter marks for student in a course
def input_marks():
    course_id = input("Enter the course ID to input marks: ")
    if not any(course[0] == course_id for course in courses):
        print("Course not found\n")
        return

#create dictionary to save marks for course
    course_marks = {}
    for student in students:
        student_id, name, _ = student #create tuple
        mark = float(input(f"Enter mark for {name} (ID: {student_id}): "))
        course_marks[student_id] = mark
    marks[course_id] = course_marks
    print("Marks added successfully\n")

#list all the courses
def list_courses():
    print("Courses: ")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")
        print()

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")
        print()

#show all marks of students in a course
def show_marks():
    course_id = input("Enter the course ID to view mark: ")
    #check if it is not exist
    if course_id not in marks:
        print("No marks found for this course \n")
        return
    course_name = next(course[1] for course in courses if course[0] == course_id) #next use to run the values back to the 1st one
    print(f"Marks for course: {course_name}")
    for student in students:
        student_id, name, _ = student #_ is the DoB that not use
        mark = marks[course_id].get(student_id, "N/A") #access to the marks of student in course_id, "mark = marks[course_id]" is dictionary
        print(f"{name} (ID: {student_id}): {mark}")
    print()

def main():
#Main menu of program
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
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            print("Exiting the system. Thanks for using.")
            break
        else:
            print("Invalid choice, please try again.\n")
          
if __name__ == "__main__":
    main()


Student Info
=========================

* Student Name: Dao Vu Minh Khang
* Student ID: 23BI14210
* Email: khangdvm.23bi14210@usth.edu.vn

