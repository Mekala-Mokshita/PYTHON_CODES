r=5
n=r-1
for i in range(r):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()