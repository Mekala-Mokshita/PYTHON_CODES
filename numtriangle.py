#num pramid triangle:-
n = 5
num = 1                      # starting number
for i in range(1, n+1):      # rows
    for j in range(n-i):     # spaces
        print(" ", end="")
    for j in range(1, i+1):  # numbers
        print(num, end=" ")
        num += 1             # increase after every print
    print()

