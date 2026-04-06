arr=[1,2,4,7]
target=6
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
arr.insert(ans, target)
print(arr)