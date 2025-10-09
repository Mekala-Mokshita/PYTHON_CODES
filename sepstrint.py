#seperating str and int from the list:-
names=[]
numbers=[]
list=["vedh","krish",337,458,"devi",667]
for i in list:
    if type(i)==str:
        names.append(i)
    if type(i)==int:
        numbers.append(i)
print("names:",names)

print("numbers:",numbers)

print("Hello")
