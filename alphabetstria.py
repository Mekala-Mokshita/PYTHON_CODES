# Program to print the pattern of alphabets in a triangular form
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=" ")