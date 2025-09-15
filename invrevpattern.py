#1.Inverted (Reverse) Number Triangle aligned to the Left:-
for i in range(5,0,-1):      #Controls the number of rows
    for j in range(i,0,-1):  #Prints numbers in each row.
        print(j,end=" ")     #Prints numbers in the same line with a space
    print()                  #Moves to the next line after finishing a row