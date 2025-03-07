#!/usr/bin/env python3
# Author ID: brroque

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    def displayStudent(self):
        print(f'Student Name: {self.name}')
        print(f'Student Number: {self.number}')

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0:
            print(f'GPA of student {self.name} is not available (no courses taken).')
            return
        gpa = sum(self.courses.values()) / len(self.courses)
        print(f'GPA of student {self.name} is {gpa:.2f}')

# Create a student instance
student1 = Student('Bryan', '025969102')

# Add grades
student1.addGrade('Math', 90)
student1.addGrade('Science', 85)

# Display student information and GPA
student1.displayStudent()
student1.displayGPA()