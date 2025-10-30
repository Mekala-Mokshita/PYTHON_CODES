#Valid Anagram:--
s = input()
t = input()

if len(s) != len(t):
    print("False")
else:
    if sorted(s) == sorted(t):
        print("True")
    else:
        print("False")