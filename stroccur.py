<<<<<<< HEAD
#count occurrences of each character in a string:-
word=input()
char_count={}
for char in word:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
for char,count in char_count.items():
=======
#count occurrences of each character in a string:-
word=input()
char_count={}
for char in word:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
for char,count in char_count.items():
>>>>>>> 43005180bed9657c65125617087e9739afc3082c
    print(char+":",count)