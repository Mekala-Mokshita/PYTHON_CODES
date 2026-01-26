listnums=list(map(int,input().split()))
seen = set()
for i in listnums:
    if i in seen:
        print("True")
        break
    seen.add(i)
else:
    print("False")
        
