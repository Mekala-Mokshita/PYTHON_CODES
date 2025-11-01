#Inheritance:-----
class Student:  #student class
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage 
    
    
    def student_details(self): #method
        print(f"{self.name} is  in class {self.grade},with {self.percentage}%")
student1=Student("mokshi",11,96)
student2=Student("arjun",12,99)

#child class
class GraduateStudent(Student): #inherit prop and methods from student parent class
    
    def __init__(self,name,grade,percentage,stream):#parameters frpm parent and new in child
        super().__init__(name,grade,percentage) #calling parent(__init__)
        self.stream=stream#new in child
        
    def student_details(self):
        super().student_details() #method inherit from parent class
        print(f'Stream is {self.stream}')
        
#object        
Grad_Student1=GraduateStudent('Kingkonk',12,95,'PCM')
#print(Grad_Student1.stream)
Grad_Student1.student_details()

        