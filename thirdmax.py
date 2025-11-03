#3rd max number:-
nums=list(map(int, input("Enter numbers: ").split()))
nums=set(nums) #set do not accept indexing
if len(nums)<3:
    print (max(nums))
else:
    nums.remove(max(nums))
    nums.remove(max(nums))
    print(max(nums))