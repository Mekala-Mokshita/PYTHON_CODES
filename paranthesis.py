s=input("Enter a string of parentheses: ")
while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
if s == "":
    print("True")
else:
    print("False")
        
       