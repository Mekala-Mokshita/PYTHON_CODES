li=["python","js","java","c++"]
fav=input("enter your fav language:")
if fav in li:
    print(f"my fav language {fav} is present at {li.index(fav)}")
else:
    print(f"my fav language {fav} is not present at list")