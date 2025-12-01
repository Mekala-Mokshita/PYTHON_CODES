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
#count occurrences of each character in a string:-
word=input()
char_count={}
for char in word:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
for char,count in char_count.items():
    print(char+":",count)