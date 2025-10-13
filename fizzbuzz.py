n=int(input())
result = []
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        result.append("github")
    elif i % 3 == 0:
        result.append("git")
    elif i % 5 == 0:
        result.append("hub")
    else:
        result.append(str(i))
print(result)