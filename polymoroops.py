#polymorphism:-- allows methods in diff class to have same name but different behaviour
class Student: 
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage 
    
    def student_details(self): #method
        print(f"{self.name} is  in class {self.grade},with {self.percentage}%")
student1=Student("manohar",11,93)
student2=Student("arjun",12,99)

#child class
class GraduateStudent(Student): 
    def __init__(self,name,grade,percentage,stream):
        super().__init__(name,grade,percentage) 
        self.stream=stream
        
    def student_details(self):
        print(f'{self.name} is in class {self.grade},with {self.percentage}% and from stream {self.stream}')

#object-Student class
student1=Student("manohar",11,93)
#object-GraduateStudent class     
Grad_Student1=GraduateStudent('Kingkonk',12,95,'PCM')
student1.student_details()
Grad_Student1.student_details()

        
