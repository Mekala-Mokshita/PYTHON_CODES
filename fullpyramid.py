n = int(input())
for i in range(n): # loop starts from 0
    print(" " * (n - i - 1)+"*" * (2*i + 1) )

'''
n = int(input())

for i in range(1, n+1):   #loops starts from 1
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

'''
#full pyramid