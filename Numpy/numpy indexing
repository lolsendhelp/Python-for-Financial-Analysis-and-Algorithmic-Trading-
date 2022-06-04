import numpy as np 


arr = np.arange(0,10)
#grabs the index of the particular item 
print(arr[8])
#prints the items in the array from index 0 to index 6
print(arr[0:6])
#prints the items in the array from the beginning to index 6
print(arr[:6])
#prints the items in the array from index 3 to the end 
print(arr[3:])
#makes the first 4 indexes all equal to 100 is known as broadcasting
arr[0:5] = 100
print(arr)
#resetting array to normal values 
arr = np.arange(0,10)

#will change the first 5 parts of the original array to 99
slice_of_arr = arr[0:6]
print(slice_of_arr)
#since the slice of array variable is equal to the original array it will also change the original array 
slice_of_arr[:] = 99
print(arr)

#will not change original array and is now its own array and not linked to other array
arr_copy = arr.copy()
arr_copy[:] = 200
print(arr_copy)
print(arr)


mat = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(mat)

#since it has 3 different arrays the indexing will grab the index you require from all 3 arrays
mat[0]

#gets 25 
#will output 25 since 25 is at index row 1 (indexing starts at 0) and row index 1
print(mat[1,1])
print(mat[0,2])
#will print everything from beginning excluding row 3 because of indexing rules and everything starting from column 1 
print(mat[:2, 1:])
print(mat[1:, :2])

#CONDITIONAL SELECTION ****
arr = np.arange(1,11)
#shows us where the parts of the array are greater than 4 
#if the item in the array is smaller than 4 it will show False and vice versa for if the item is larger than 4
print(arr > 4)
#will find the items that are true in the bool_array variable
print(arr[arr > 4])
print(arr[arr <= 9])
