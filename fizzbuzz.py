<<<<<<< HEAD
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
=======
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
>>>>>>> 43005180bed9657c65125617087e9739afc3082c
print(result)