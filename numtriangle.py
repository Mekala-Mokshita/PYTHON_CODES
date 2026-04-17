#num pramid :-
n = 5
num = 1                      # starting number
for i in range(1, n+1):      # rows
    for j in range(n-i):     # spaces
        print(" ", end="")
    for j in range(1, i+1):  # numbers
        print(num, end=" ")
        num += 1             # increase after every print
    print()


'''
#num pyramid:-
n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")  # print numbers from 1 to i+1
    print()  # move to the next line after each row
    
'''

