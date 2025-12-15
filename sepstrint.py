<<<<<<< HEAD
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
=======
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
>>>>>>> 43005180bed9657c65125617087e9739afc3082c
print("numbers:",numbers)