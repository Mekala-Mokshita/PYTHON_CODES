#equality operator(== !=)
#== is used for content comparision
print("2"==2)
print(2==2)
print(True==1)
print(False==0)
#comparision strings
print(ord("A"),ord("a")) #ord gives us ASCII values
print("Py"=="Py")
print("Py"=="py")
print("pYthon">="python")
 #logical operators
print(10 and 0)
print(0 and "")
print(" " and "py")
print(False and True)
#for non-boolean values in "and"(if a is true result is b value,if a is false result is a)
print([] and "js")
#for non-boolean values in "or"(if a is true result is a value,if a is false result is b)
print("" or "py")
print(True or "true")
#is operator
a=10
b=10
print(id(a),a)
print(id(b),b)
print(a is b)
b=50
print(a is b)
c1=10+5j
c2=10+10j
c3=c2
print(c2 is c3)
print (c2 is not c3)
#list
l1=[10,20]
l2=[10,20]
print(l1 is l2)
l2=l1
print(l1 is l2)
#we use membership operator(in,not in) check if the given object or element or value present in sequence
l=["python","js","java"]
print("js" in l)
print("c" in l)
print("c++" not in l)