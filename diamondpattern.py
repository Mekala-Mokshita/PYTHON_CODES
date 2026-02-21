n=int(input())
for i in range(1,n+1): #we will this loop in left side pyramid
    print(" "*(n-i),"* "*i)
for i in range(n-1,0,-1): #if we use n,0,-1 then in the middle we will get same no of stars in two lines
    print(" "*(n-i),"* "*i)

#we should two loops due to up and down 