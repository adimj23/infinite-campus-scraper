class Student:
    def __init__(self, first="", last=""):
        self.first_name = first
        self.last_name = last
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses
    
    def get_course_names(self):
        course_names = []
        for i in self.courses:
            course_names.append(i.get_name())
        return course_names


class Course:
    def __init__(self, name=""):
        self.course_name = name
        self.course_grades = []
    
    def get_name(self):
        return self.course_name

    def set_name(self, new_name):
        self.course_name = new_name
    
    def get_grade(self, index):
        if (index >= len(self.course_grades)):
            return None

        return self.course_grades[index]

    def add_grade(self, new_grade):
        self.course_grades.append(new_grade)
    
    def remove_recent_grade(self):
        self.course_grades.pop(-1)

class Grade:
    def __init__(self, date, decimal=0.0):
        self.date = date
        self.score = decimal
    
    def get_date(self):
        return self.date

    def set_date(self, new_date):
        self.date = new_date

    def get_score(self):
        return self.date

    def set_score(self, new_decimal):
        self.score = new_decimal
