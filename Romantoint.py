#convert from roman to integer
s=input() #MIVII
roman_map = {'I': 1, 'V': 5, 'X': 10, 
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total = 0 #its the value of string
prev = 0  #updates the value by the 
for char in s:
    curr = roman_map[char]
    if curr > prev:
        total += curr - 2 * prev
    else:
        total += curr
        prev = curr
print(total)