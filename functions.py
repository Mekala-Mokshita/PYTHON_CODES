#A function is 
def greetings():
    print("welcome to functions concept")
#calling function
greetings()
print(greetings())
#with prameters
def greetings(name,age):
    print(f"{name} is {age} old")
greetings("python",40)

#keyword arguments
def sum(a,b):
    return a+b
result=sum(5,10)
print(result)
#key arguments
result_2 =sum(b=100,a=10)
print(result_2)
#print(result_2(a=10,c=20))
#print(sum()) like this can keep when we have default arguments in parameters

#variable length arguments(*)
def sum(a,b,*c):
    return f"{a+b} and unused values are {c}"
print(sum(10,20,30))
print(sum(10,20,30,40,50))

#keyword length arguments(**):-** this make as key value pairs(dict)
def welcome(name,**temp):
    print(f"{name} welcome to datascience")
    print(temp)
welcome("ravi",id=101,age=55)
#higher order function:-2 types, takes arguments as other function and takess it own args(js)
#lambda function:- it is a function without a name and one time use
#syntax lambda arguments: action
n=int(input("enter n value: "))
d=lambda x:x*x
d(n) #calling func
 
 #largest num of 2
result=lambda a,b:f"{a} is largest number"if a>b else f"{b} is largest number"
print(result(5,10))
#map is used apply some function to each and every elements in sequence
# map(function,sequence)
l=[5,10,15,20]
#without map
r=[]
for i in l:
    r.append(i*5)
print(l,r)
result=map(lambda x:x*5,l)
print(result)

#filter function:It is used to filter sequence elements based on condition filter(function,sequence)
even= list(filter(lambda x:x%2 ==0,l))
print(even)

#to reduce we have to use module
#import functools functools.reduce() (#first way)-it imports all so takes 
from functools import reduce #second way
sum=reduce(lambda x,y:x+y,l)
print(sum)
 


