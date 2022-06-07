import numpy as np
import pandas as pd 
import os
import time
from numpy.random import randn


print(np.random.seed(101))

#dataframes are essentially a pandas series with a shared index
df = pd.DataFrame(randn(5,4), ["A","B","C","D","E"], ["W","X","Y","Z"])
print(df)

time.sleep(2)
os.system('cls')

#requests 2 columns from the data frame
print(df[["W","Z"]])

time.sleep(2)
os.system('cls')

#requests row A from the data frame
df.loc["A"]

time.sleep(2)
os.system('cls')

df.iloc[2]

time.sleep(2)
os.system('cls')

#makes a new column in the data frame
df['new'] = randn(5,1)
print(df)

time.sleep(2)
os.system('cls')

#deletes the W column off the data frame
#axis 1 means it will delete columns instead of rows
#axis 0 means it will delete rows instead of columns
#inplace means it will change the actual dataframe 
df.drop("new", axis=1,inplace=True)
print(df)

time.sleep(2)
os.system('cls')

#deletes the E row of the dataframe 
df.drop("E",inplace=True)
print(df)

#finds a specific piece of data in the data frame 
print(df.loc['B','Y'])

time.sleep(2)
os.system('cls')

print(df.loc[["A", "B"], ["W", "Y"]])
