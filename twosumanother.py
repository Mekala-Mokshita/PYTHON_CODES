numbers = [1,2,3,4]#list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print([i + 1, j + 1])
            break
