import numpy as np
import time

array = np.array([1,2,3,4,5])

# print(type(array))

revenues = [2000, 5000, 3000, 65000, 7200, 31000, 26550, 1900, 3020, 5100, 41000]

initial_time = time.time()

sum = 0
for i in revenues:
    sum += i

# print(sum)
termination_time = time.time()

# print("Execution Time", termination_time - initial_time)

array = np.array(revenues)

initial_time = time.time()

sum = array.sum()
# print(sum)

termination_time = time.time()
# print("Execution Time", termination_time - initial_time)

x = ["Ben", 500, "Jake", "Lie", 6000]

# for i in x:
#     print(type(i))

arrayx = np.array(x)
# print(arrayx)

# for i in arrayx:
#     print(type(i))

array2 = np.array([[1,2,3], [4,5,6]])
print(array2)

# the numpy ndim method is use to check the dimension of an array
print(array2.ndim)

# the numpy shape method is use to check how many element the array as in each row

print(array2.shape)

# to calculate the number of values an array as we use the numpy size method

print(array2.size)