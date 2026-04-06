arr=[3,4,13,13,13,20,40]
target=13
left=0
right=len(arr)-1
ans=-1  #not found, so it stores element
while left<=right:
    mid=(left+right)//2   #becoz for every loop mid changes/updates
    if arr[mid]<target:
        left=mid+1
    elif arr[mid]>target:
        right=mid-1
    elif arr[mid]==target:
        ans=mid
        right=mid-1    #ele on left side so -1 ,#for last occurrence right=mid+1
print("first occ:",ans)
