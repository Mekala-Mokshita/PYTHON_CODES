arr=[1,2,3,4,5,7,8,9,10]
n=int(input())
total=0
sum=(n*(n+1))//2
for i in arr:
    total+=i
print(total)
print("missing value:",sum-total)