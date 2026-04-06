s=input()
t=input()
def result(s,t):
    arr=[0]*26
    if len(s) != len(t):
        return False   
    for i in range(len(s)):
        arr[ord(s[i])-ord('a')] +=1
        arr[ord(t[i])-ord('a')] -=1
    for ch in arr:
        if ch >0:
            return False
    return True

print(result(s,t))
