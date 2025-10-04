import numpy as np

myArray = np.random.randint(0, 100, (2, 6))
myReshapedArray = myArray.reshape(6, 2)

myFirstRowFlipped = myArray[0, :]
myFirstRowFlipped = myFirstRowFlipped.reshape(6, 1)
mySecondRowFlipped = myArray[1, :]
mySecondRowFlipped = mySecondRowFlipped.reshape(6, 1)

print("My Array:\n", myArray)
print("My Reshaped Array:\n",myReshapedArray)
myArrayCustom = np.concatenate((myFirstRowFlipped, mySecondRowFlipped), axis=1)
print("My Custom Array:\n", myArrayCustom)

print("My Custom Array's median:\n", np.median(myArrayCustom))
print("My Custom Array's mean:\n", np.mean(myArrayCustom))

fakeArray = myArray[myArray > 53]
print("Numbers Over 53:\n", fakeArray)

superFakeArray = np.where(fakeArray == 55, 999, fakeArray)
print(superFakeArray)

# Array Manipulation Playground:
# Description: Create a program that performs various array operations to explore NumPy’s core features.

# Tasks:
#   Generate a 1D array of random integers and reshape it into a 2D matrix.
#   Perform slicing to extract specific rows, columns, or submatrices.
#   Use np.where to replace values based on a condition (e.g., replace all numbers > 50 with 0).
#   Compute basic statistics (mean, median, min, max) using np.mean, np.median, etc.

# NumPy Skills:
#  Array creation (np.array, np.random), reshaping (np.reshape), indexing/slicing, conditional operations (np.where), 
#  and statistical functions.

# What i learned:
#   Concatenation is not broadcasted so when working with it you have to use equivalent axis dimention