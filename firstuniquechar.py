#enumerate can use instead of range
'''count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1'''
s = input()

def first_unique(s):
    arr = [0]*26

    # count frequency
    for i in range(len(s)):
        arr[ord(s[i]) - ord('a')] += 1

    # find first unique
    for i in range(len(s)):
        if arr[ord(s[i]) - ord('a')] == 1:
            return i

    return -1

print(first_unique(s))


