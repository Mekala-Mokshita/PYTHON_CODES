#zeros at last
arr=[2,0,3,5,0,0,10,11]
first_arr=[]#list1
second_arr=[]#list2
for i in arr:
    if i==0:
        second_arr.append(i) #if 0
    else:
        first_arr.append(i)
print(first_arr+second_arr)