import numpy as np
import pandas as pd 

labels = ['a', 'b', 'c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b':20, 'c':30}

#will match the lists and lables to the corresponding values and output the datatype 
print(pd.Series(my_list, index=labels))
#will match the items in the array with their corresponding index values
print(pd.Series(arr))
#will match the items with the values set beside it in the dictionary
print(pd.Series(d))

country_series = pd.Series([1,2,3,4], index = ["CANADA", "USA", "CHINA", "RUSSIA"])
country_series2 = pd.Series([1,2,3,4], index = ["CANADA", "CHINA", "JAPAN", "RUSSIA"])
print(country_series)

#will print out the other value associated with what is put in
print(country_series["CANADA"], country_series[2])

#will add only where there is a match in the series
#if there is no match it will not return a value
print(country_series + country_series2)
