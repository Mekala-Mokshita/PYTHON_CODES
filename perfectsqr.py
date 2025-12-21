#number is perfect square or not
n=int(input("Enter a number: "))
i=1
is_perfect_square=False
while i*i<=n:
    if i*i==n:
        is_perfect_square=True
        break
    i+=1
if is_perfect_square:
    print("perfect square")
else:
    print("not perfect square")