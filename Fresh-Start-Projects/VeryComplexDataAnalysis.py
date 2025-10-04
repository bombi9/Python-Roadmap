from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

file = 'myStolenFiles/temperatures.csv'

# We use genfromtxt when we are not sure if all the elements are missing:
setOfFiles = np.genfromtxt(file, delimiter=',', skip_header=1, dtype='float32')
# We use loadtxt as a simple and straight forward solution
setOfFilesTwo = np.loadtxt(file, delimiter=',',skiprows=1, dtype='float32')

setOfFiles, setOfFilesTwo = setOfFiles[:,1:], setOfFilesTwo[:,1:]
mean = np.mean(setOfFiles, axis=0)
normalized = (setOfFiles - setOfFiles.min()) / (setOfFiles.max() - setOfFiles.min())

for n in range(setOfFiles.shape[1]):
    print(f"The mean of city{n+1} is {mean[n]:.2f}")
    print(f"The normalization of the city {n+1}: \n{normalized[:, n]}")

plt.title("Temperatues")
plt.plot(range(len(setOfFiles[:,0])), setOfFiles[:,0], label="City01", color="Red")
plt.plot(range(len(setOfFiles[:,1])), setOfFiles[:,1], label="City02", color="blue")
plt.plot(range(len(setOfFiles[:,2])), setOfFiles[:,2], label="City03", color="green")
plt.legend()
plt.show()
