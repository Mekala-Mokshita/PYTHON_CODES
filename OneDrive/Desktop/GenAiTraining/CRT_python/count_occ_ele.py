arr=[1,2,2,3,3,2,4]
dic={}   #it automatically takes it as key-value pairs
for i in arr:
    if i in dic:
        dic[i]+=1   #increases the count of element that already present
    else:
        dic[i]=1    #when ele not in dict it adds it in dic
print(dic) 