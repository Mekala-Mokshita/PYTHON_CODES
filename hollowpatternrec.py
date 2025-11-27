rows=int(input())
cols=int(input())
for i in range(0,rows):
    for j in range(0,cols):
        if i==0 or i==(rows-1) or j==0 or j==(cols-1):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()
#rectanglar hollow pattern