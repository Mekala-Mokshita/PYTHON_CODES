#bsa
arr=[10,12,20,32,50,55,65,80,99]
target=65
left=0
right=len(arr)-1

while left<=right:
    mid=(left+right)//2   #becoz for every loop mid changes/updates
    if arr[mid]<target:
        left=mid+1
    elif arr[mid]>target:
        right=mid-1
    elif arr[mid]==target:
        print("ele found:",mid)
        break
else:
    print("not found")
