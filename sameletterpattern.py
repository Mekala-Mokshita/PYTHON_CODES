n=int(input())
for i in range(1,n+1):
    print((chr(64+i)+" ")*i)  #took 64 becoz loop taken from 1
    
#can take as ((65+i)+" ")*i+1 it will work when loop is for(n):-capital means with 65 or if small 97.

