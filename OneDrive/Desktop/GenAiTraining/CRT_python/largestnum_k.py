arr=[50,30,23,12,9,21]#array
k=int(input())
first_lar=float('-inf')
second_lar=float('-inf')
third_lar=float('-inf')
for num in arr:
    if num > first_lar:
        third_lar = second_lar
        second_lar = first_lar
        first_lar = num
    elif num > second_lar:
        third_lar = second_lar
        second_lar = num
    elif num > third_lar:
        third_lar = num
print(third_lar) #print result