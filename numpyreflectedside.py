n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(i+1,0,-1):
        print(k, end="")
    for l in range(2,i+2):
        print(l, end="")
    print()