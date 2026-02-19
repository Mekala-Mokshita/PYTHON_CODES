arr=list(map(int,input().split()))
s=0
e=len(arr)-1
while s<e:
    arr[s],arr[e]=arr[e],arr[s]
    s+=1
    e-=1
for i in arr:
    print(i,end=" ")
