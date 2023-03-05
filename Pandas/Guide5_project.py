import numpy as np
import pandas as pd

last_year = pd.read_csv("employee_revenue_lastyear.csv")
print(last_year.head(8))
print(last_year.tail(6))

# the info method returns the number of columns dataypes and more that is present in file

print(last_year.info())

last_year["year"] = 2022
print(last_year)

names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
call_numbers =  [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]    
average_deal_sizes = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]

dictionary = {
    "name":names,
    "calls":call_numbers,
    "avg_deal_size":average_deal_sizes,
    "revenue":revenues
}

current_year = pd.DataFrame(dictionary)
print(current_year.head())

current_year["year"] = 2023
print(current_year.head())

current_year.columns = last_year.columns

all_data = pd.concat([last_year, current_year])

print(all_data)

# the reset_inde() method Reset the index of the DataFrame, and use the default one instead. If the DataFrame has a MultiIndex, this method can remove one or more levels.

all_data.reset_index(drop=True, inplace=True)

print(all_data)

# isna() method check if the dataframes as any value with NaN
print(all_data.isna().any())

# filln() method replace the value with NaN with a value
all_data.fillna(value=np.mean(all_data), inplace=True)

print(all_data)

# drop_duplicates() method Return DataFrame with duplicate rows removed.
all_data.drop_duplicates(inplace=True)
print(all_data)

all_data.reset_index(drop=True)

print(all_data)

print(all_data.describe())

all_data[all_data["year"] == 2022].describe()
all_data[all_data["year"] == 2023].describe()

print(all_data.sort_values(by="Revenue"))

print(all_data[all_data["year"] == 2023].sort_values(by="Revenue"))

print(all_data["Name"].value_counts())
