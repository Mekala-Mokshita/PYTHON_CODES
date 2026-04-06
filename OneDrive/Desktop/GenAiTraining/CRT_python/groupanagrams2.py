from collections import defaultdict
def groupAnagrams(self, strs):
    freq={}
    arr=[0]*26
    ana_list=defaultdict(list)
    for i in strs:
        for j in i:
            arr[ord(j) - ord('a')] += 1
        key = ana_list[tuple(arr)]
        freq[key].append(i)
    print(ana_list)
            