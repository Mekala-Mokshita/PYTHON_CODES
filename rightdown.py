n=int(input())
for i in range(n,0,-1):
    print("  "*(n-i),"* "*i)  # we can also take in for loop(0,n+1) then "*"*n-i+" "*i