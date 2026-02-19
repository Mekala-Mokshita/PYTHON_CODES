arr=list(map(int,input().split()))
left=0
right=len(arr)-1
while left<right:
    if arr[left]!=arr[right]:
        print("Not Palindrome")
        break
    left+=1
    right-=1
else:
    print("palindrome")
    