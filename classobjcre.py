class Student:  #student class
    def __init__(self,name,grade):#__init__ method is constructor ,value initialize
        self.name=name
        self.grade=grade
#object-instance of class
student1=Student("mokshi",11)
print(student1.name,student1.grade)
student2=Student("arjun",12)
print(student2.name,student2.grade)