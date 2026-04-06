t=int(input())
for _i in range(t):
    x,y=map(int,input().split())
    if x>y:
        print((x-y)+1)
    