nums=list(map(int,input().split()))
sum=0
count = {}
for i in nums:
    count[i] = count.get(i, 0) + 1
for i,v in count.items():
    if v==1:
        sum+=i
print(sum)
#for counting ele:
'''nums=list(map(int,input().split()))
arr=[]
sum=0
count = {}
for i in nums:
    count[i] = count.get(i, 0) + 1
for i,v in count.items():
    if v==1:
        sum+=i
print(sum) '''
    