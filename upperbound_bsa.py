arr=[2,3,6,7,8,8,11,11,11,12]
target=8
ans=len(arr)
low=0 #low
high=len(arr)-1 #high

while low<=high:
    mid=(low+high)//2   #becoz for every loop mid changes/updates
    if arr[mid]>target:  #upperbound condition
        ans=mid          #updates ans
        high=mid-1    #moves right side of mid
    else:
        low=mid+1  
print(ans)