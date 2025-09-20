import numpy as np

# Variables:
rng = np.random.default_rng()
my_3D_Array = np.array([[[1, 2, 3], [4, 5, 6]] ,[[7 ,8 ,9], [10 ,11 ,67]]], dtype="int16")
my1DArray = np.array(range(1, 6), dtype="int16")
myZeors = np.zeros((3, 3), dtype="int16")
myrandoms = rng.random([2, 2, 2], dtype="float32")*20

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