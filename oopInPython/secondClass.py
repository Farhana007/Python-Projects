
#creating multiple Class In(OOP)


class Student:
  def __init__(self,name,age,grade):
    self.name = name
    self.age  = age
    self.grade = grade  #0-100


  def get_grade(self):
    return self.grade  
  


class Course:
  def __init__(self,name,max_student):
    self.name = name
    self.max_student = max_student
    self.students = []  # we are creating  a empty list to add student in Course 










      