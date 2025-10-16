class Student:  #student class
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.__percentage=percentage #double underscore limits access to get access we the function/method
    #encapsulation  
    def get_percentage(self):
        return self.__percentage
    
    def student_details(self): #method
        print(f"{self.name} is  in class {self.grade},with {self.percentage}%")
student1=Student("mokshi",11,96)
student2=Student("arjun",12,99)
#print(student1.__percentage()):-eror
#print(student1.percentage()):-error
print(student1.get_percentage())
