# Задание 2: Курс и студенты

class Student:
    def __init__(self, name):
        self.name = name
        self.courses: list = []  #courses
    
    def get_courses(self):
        if not self.courses:
            print(f"{self.name} is not enrolled in any courses.")
        else:
            print(f"{self.name}: ", end="")
            for i, course in enumerate(self.courses):
                if i < len(self.courses) - 1:
                    print(course.course_name, end=", ")
                else:
                    print(course.course_name)  # Print the last course without a comma

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students: list = []  
        
    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)  #connecting get_couses with get_students
        print(f"{student.name} добавлена в {self.course_name}!")
    
    def get_students(self):
        print(f"Students in {self.course_name}:")
        if not self.students:
            print("No students enrolled.")
        else:
            for student in self.students:
                print(student.name)


course1 = Course("Python Programming")
course2 = Course("Data Science")


student1 = Student("Emma")
student2 = Student("Liam")


course1.add_student(student1)
course1.add_student(student2)
course2.add_student(student1)

# Display students in each course
course1.get_students()  # Get students for Python Programming
course2.get_students()  # Get students for Data Science

# Display courses for each student
student1.get_courses()  # Get courses for Emma
student2.get_courses()  # Get courses for Liam