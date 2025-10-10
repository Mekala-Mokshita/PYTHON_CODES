#odd numbers in particular interval
low=int(input())
high=int(input())    
total = high - low + 1
        
        # Half of them are odd
count = total // 2
        
        # If both low and high are odd, add 1 more
if low % 2 != 0 and high % 2 != 0:
    count += 1
print (count)