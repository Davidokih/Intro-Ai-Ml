import numpy as np

def multiply(a,b):
    return a * b

print(multiply(3,4))

arr = np.array([10,4,6,1,0,7],)
index = np.argmax(arr)

print(arr[index])