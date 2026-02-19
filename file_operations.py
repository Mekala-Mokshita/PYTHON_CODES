#file operations

#read operations:----
#first way to open file:-
file_obj=open("text.txt","r")
print(file_obj) #it returns io text wrapper(we cant read that)
file_data=file_obj.read(2) #2 is no.of bytes if nothing we get all the data 
print(file_data)
file_obj.close() #we should manually close

#Second way:-(best way)
with open("text.txt","r") as file_obj:
   #file_data =file_obj.readline() #means it reads only first line
   file_data =file_obj.readlines() #means reads all lines
   print(file_data)

#write operation:-----
with open("text.txt","w") as file_obj:
   file_data = file_obj.write
   ("DataScience")
l=["python\n","js\n","c\n"]
with open("text.txt","w") as file_obj:
   file_obj.writelines(l)

#append:------
with open("text.txt","a") as file_obj:
   file_obj.write("\n welcome to mru")


#import csv
#with open("s.csv","r") as file_obj:
#csv.reader()