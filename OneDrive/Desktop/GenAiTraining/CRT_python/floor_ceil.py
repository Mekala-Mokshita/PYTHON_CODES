arr=[10,20,30,40,50]
target=25
left=0 #low
right=len(arr)-1 #high
floor=-1
ceil=-1
while left<=right:
    mid=(left+right)//2   #becoz for every loop mid changes/updates
    if arr[mid]==target:
        floor=arr[mid]
        ceil=arr[mid]
    if arr[mid]<=target:
        floor = arr[mid]      # possible floor
        left = mid + 1  
    if arr[mid]>=target:
        ceil = arr[mid]      # possible floor
        right = mid - 1
print([floor,ceil])



