'''a=[1,2,3,4,5]
a=[a[-1]]+a[:-1]
print(a)'''

num = [1, 2, 3, 4, 5]
temp = num[0]
for i in range(len(num) - 1):
    num[i] = num[i + 1]
num[len(num) - 1] = temp

print(num)