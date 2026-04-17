r=5
n=r-1
for i in range(r): #to get reverse pyramid here we can write (r-1,-1,-1)
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()