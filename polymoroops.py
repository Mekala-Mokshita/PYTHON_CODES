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



        
