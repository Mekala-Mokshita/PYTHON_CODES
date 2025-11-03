nums = list(map(int, input("Enter numbers: ").split()))
nn = []
total = 0
for n in nums:
    total += n
    nn.append(total)
print(nn)
