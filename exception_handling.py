#exception handling
#syntax error:- ex:-print("hello
#logical error:-
#runtime error:-10/0(zero division error)
try:
    #a=10
   #b=0
   a=int(input("enter a value:"))
   b=int(input("enter another value:"))
   print(a/b)
# except ZeroDivisionError as err:#for single error
except(ZeroDivisionError,ValueError) as err:#for multiple error
    print(err)
#to handle all the exceptions
except Exception as err:
    print(err)
else:
    print("no error")
finally:
    print("end")
