import numpy as np
num=list(map(int,input("Enter numbers: ").split()))
arr1=np.array(num)
x=np.concatenate((arr1,arr1))
print(x)