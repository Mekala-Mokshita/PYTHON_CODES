num = [1, 2, 3, 4, 5,6,7]
temp1 = num[0]
temp2=num[1]
temp3=num[2]
for i in range(len(num) - 1):
    num[i] = num[i + 1]
for i in range(len(num) - 1):
    num[i] = num[i + 1]
for i in range(len(num) - 1):
    num[i] = num[i + 1]

num[len(num) - 1] = temp3
num[len(num) - 2] = temp2
num[len(num) - 3] = temp1


print(num)