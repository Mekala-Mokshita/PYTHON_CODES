num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp= temp // 10  

if sum == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

