'''
Задание: "Универсальный функционал для объектов"
Представь, что ты создаешь приложение для 
управления различными типами пользователей: 
Студент, Преподаватель и Администратор. 
У каждого из них есть уникальное поведение, но также 
есть общие действия, которые можно добавить через миксины.
'''

class LoggingMixin:
    def log_action(self, message:str):
        print(f"[LOG]: {message}")


class ProfileMixin:
    def update_username(self, name:str):
        self.name = name
        print(f"Имя обновлено на: {self.name}")

    def update_password(self, password:str):
        self.password = password
        print(f"Пароль успешно обновлен!")

    def display_profile(self):
        print(f"Имя: {self.name}, Email: {self.email}")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.password = 'any_password'


class Student(User, LoggingMixin, ProfileMixin):
    def __init__(self, name, email, courses = None):
        super(). __init__(name, email)
        self.courses = courses or []

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f'{course_name} added')
        
        else:
            print(f"Student is already enrolled in {course_name}")

    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{course_name} removed")
        
        else:
            print(f"Student is not enrolled in {course_name}")

    def view_courses(self):
        """Displays the list of enrolled courses."""
        if self.courses:
            print(f"Enrolled courses: {', '.join(self.courses)}")
        else:
            print("No courses enrolled yet.")


student = Student(name="Alice", email="alice@example.com")
student.update_username("Alice Johnson")

student.add_course("Math")
student.add_course("Science")
student.view_courses()  # Should list "Math, Science"

student.remove_course("Math")
student.view_courses()  # Should list "Science"

student.log_action("Viewed courses")



# class Teacher(User, LoggingMixin, ProfileMixin):
#     def __init__(self, name, email, courses=None):
#         super().__init__(name, email)
#         self.courses = courses or []

#     def add_course(self, course_name):
#         if course_name not in self.courses:
#             self.courses.append(course_name)
#             print(f"Course '{course_name}' has been added.")

#         else:
#             print(f"Course '{course_name}' already exists.")

        
#     def remove_course(self, course_name):
#         if course_name in self.courses:
#             self.courses.remove(course_name)
#             print(f"Course '{course_name}' has been removed.")

#         else:
#             print(f"Course '{course_name}' not found.")

        
    
#     def enroll_student(self, course_name, student_name):
#         if course_name in self.courses:
#             if student_name not in self.courses[course_name]:
#                 self.courses[course_name].append(student_name)
#                 print(f"Student '{student_name}' enrolled in '{course_name}'.")
#             else:
#                 print(f"Student '{student_name}' is already enrolled in '{course_name}'.")

#         else:
#             print(f"Course '{course_name}' does not exist.")

    
#     def assign_grade(self, course_name, student_name, grade):
#         if course_name in self.courses and student_name in self.courses[course_name]:
#             print(f'Grade {grade} is assigned to {student_name} in {course_name}')

#         else:
#             print(f"Cannot assign grade. Either course or student not found.")




# teacher = Teacher(name="Mr. Smith", email="smith@sexample.com")

# teacher.add_course("Math")
# teacher.add_course("Science")


# teacher.enroll_student("Math", "Alice")
# teacher.enroll_student("Math", "Bob")


# teacher.assign_grade("Math", "Alice", "A")
# teacher.assign_grade("Math", "Charlie", "B")    #  show an error

# teacher.remove_course("Science")
