<<<<<<< HEAD
#3rd max number:-
nums=list(map(int, input("Enter numbers: ").split()))
nums=set(nums) #set do not accept indexing
if len(nums)<3:
    print (max(nums))
else:
    nums.remove(max(nums))
    nums.remove(max(nums))
=======
#3rd max number:-
nums=list(map(int, input("Enter numbers: ").split()))
nums=set(nums) #set do not accept indexing
if len(nums)<3:
    print (max(nums))
else:
    nums.remove(max(nums))
    nums.remove(max(nums))
>>>>>>> 43005180bed9657c65125617087e9739afc3082c
    print(max(nums))