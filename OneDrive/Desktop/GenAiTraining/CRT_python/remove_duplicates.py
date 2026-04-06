#remove duplicates from a list using two pointers
#if i!=j then i++ ; i==j (means we have duplicates)then j++
num=[1,1,2,2,3]
i=0
j=1
for j in range(len(num)):
    if num[i]!=num[j]:
        i+=1
        num[i]=num[j]
    if num[i]==num[j]:
        j+=1
print(num[:-2])



'''
num = [1,1,2,2,3]
result = []

for n in num:
    if n not in result:
        result.append(n)

print(result)
'''