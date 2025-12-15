<<<<<<< HEAD
class Student:  #student class
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage
    def student_details(self): #method
        print(f"{self.name} is  in class {self.grade},with {self.percentage}%")
student1=Student("john",11,96)
student2=Student("sarkar",12,97)

#print(student1.__dict__)
#modify object property
print(student1.percentage)
student1.percentage=100
print(student1.percentage)
#delete object property
print(student1.__dict__)
del student1.percentage
print(student1.__dict__)
#delete object
del student1
=======
class Student:  #student class
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage
    def student_details(self): #method
        print(f"{self.name} is  in class {self.grade},with {self.percentage}%")
student1=Student("john",11,96)
student2=Student("sarkar",12,97)

#print(student1.__dict__)
#modify object property
print(student1.percentage)
student1.percentage=100
print(student1.percentage)
#delete object property
print(student1.__dict__)
del student1.percentage
print(student1.__dict__)
#delete object
del student1
>>>>>>> 43005180bed9657c65125617087e9739afc3082c
#print(student1.__dict__) :- it get as not defined