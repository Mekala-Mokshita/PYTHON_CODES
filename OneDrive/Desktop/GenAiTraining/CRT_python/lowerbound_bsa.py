arr=[3,5,8,15,19]
target=4
ans=len(arr)
low=0 #low
high=len(arr)-1 #high

while low<=high:
    mid=(low+high)//2   #becoz for every loop mid changes/updates
    if arr[mid]>=target:
        ans=mid
        high=mid-1    #moves right side of mid
    else:
        low=mid+1  
print(ans)