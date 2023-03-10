import numpy as np
import pandas as pd

my_series = pd.Series([10, 21, 12, 41, 5])

# the pandas .size() print the total lenght of element in a series
print(my_series.size)
# the pandas .ndim() print the number of array present
print(my_series.ndim)

# the pandas .head() print the first five element in an array or you specify the number of value to be prented out
print(my_series.head(2))
# the pandas .tail() print the last five element in an array or you specify the number of value to be prented out
print(my_series.tail(2))
print(my_series[2])
print(my_series[1:4])

numbers = [[1,2,39,67,90], [1,2,39,67,90]]

# the pandas .DataFrame() returns the value of an array in a table format
df = pd.DataFrame(numbers)

print(df)

arr = np.array([[1,2,39,67,90], [8,12,45,12,8], [2,8,34,90,102]])
# array2 = np.array([[1,2,3], [4,5,6]])

df = pd.DataFrame(arr)

print(df.describe())

# Adding the T to describe method convert it to rows instead of column

print(df.describe().T)
