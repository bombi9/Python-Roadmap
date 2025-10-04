import numpy as np

# Variables:
sixSeven = np.full((2, 3), 67, dtype="int16")
anderBilder = np.full_like(sixSeven, "Ander bilder", dtype="int16")
my_3D_Array = np.array([[[1, 2, 3], [4, 5, 6]] ,[[7 ,8 ,9], [10 ,11 ,67]]], dtype="int16")
my1DArray = np.array(range(1, 6), dtype="int16")
myZeors = np.zeros((3, 3), dtype="int16")
myrandoms = np.random.random([2, 2, 2], dtype="float32")*20
fourVfour = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], dtype="int8")
fVf = np.array([[0, 3, 5, 9], [51, 22, 67, 81], [91, 110, 1, 2], [7, 4, 35, 69]], dtype="int8")

# Some built-in attributes:
print("Number of dimentions:", my_3D_Array.ndim)
print("shape:", my_3D_Array.shape)
print("size:", my_3D_Array.size)
print("data type:", my_3D_Array.dtype)

print("My 1D array:")
print("shape:", my1DArray.shape)
print("size:", my1DArray.size)
print("data type:", my1DArray.dtype)

print("My 2D zeros array:")
print("shape:", myZeors.shape)
print("size:", myZeors.size)
print("data type:", myZeors.dtype)

print("My 2D randoms array:")
print("shape:", myrandoms.shape)
print("size:", myrandoms.size)
print("data type:", myrandoms.dtype)

# Accessing the first two rows and last two collumns:
print("first two rows and last two collumns:")
print(fourVfour[-2:, 0:2]) #We specify the collumn first

# Basic math operations:
print(f"Sunbstraction: \n{fVf - fourVfour}")
print(f"Addition: \n{fVf + fourVfour}")
print(f"Multiplication: \n{fVf * fourVfour}")
print(f"Division: \n{fVf / fourVfour}")

# Axis attribute:
print("The Max function:", fourVfour.max())
print("The Max function specifying axis0 (rows):\n", fourVfour.max(axis=0))
print("The Max function specifying axis1 (collumns):\n", fourVfour.max(axis=1))

# Advanced indexing and boolean masking:
print(fourVfour)
print("indexing collumns using a list of elements: fourVfour([1, 0, 3], :)\n", fourVfour[[1, 0, 3], :])
print("indexing rows using a list of elements: fourVfour(:, [2, 3, 0], :)\n", fourVfour[[2, 3, 0], :])

print(fourVfour[fourVfour%2 == 0])


a = np.zeros((5, 5), dtype="int8")
a[:, [0, -1]], a[[0, -1], :], a[2:-2, 2:-2] = 1, 1, 9
print(a)

# Broadcasting:
# In order to broadcast the dimentions have to be equal or one of them has to be 1
arr1 = np.array([[1, 2, 3, 4, 5, 6]])   #(1, 6)
arr2 = np.array([[4], [2], [7], [12]])  #(4, 1) they are compatible
print(arr1 + arr2)

# Linear Algebra:
# multiplication:
np.matmul(fourVfour, fVf) # (4, 4) x (4, 4) will generate a (4, 4) matrix
np.matmul(fourVfour, np.identity(4)) # (4, 4) multiplied by the identity matrix will simply give us the same matrix

# Determinant:
np.linalg.det(fourVfour)

# Reading from text