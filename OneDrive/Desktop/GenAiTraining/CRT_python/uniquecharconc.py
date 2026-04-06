s=input()
count = {}
sub=""
for i in s:
    count[i] = count.get(i, 0) + 1
for i,v in count.items():
    if v==1:
        sub+=i
print(sub)

    