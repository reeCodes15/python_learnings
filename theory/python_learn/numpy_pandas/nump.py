import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

arr2d2 = np.array([[1,2],[2,3]])
# Element-wise addition
result = arr1d + 10

# Matrix multiplication
matrix_product = np.dot(arr2d, arr2d.T)

print("1D Array:", arr1d)
print("2D Array:", arr2d)
# print("2D Array:", arr2d2)
print("Result of Element-wise Addition:", result)
print("Matrix Product:", matrix_product)

print('printing traverse')
print(arr2d.T)