# Program to count the number of smaller elements to the right of each element in the array
arr = [8,1,2,2,3]
count1 = []

for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if arr[j] < arr[i]:
            count += 1
    count1.append(count)

print(count1)