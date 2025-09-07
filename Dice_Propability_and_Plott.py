import matplotlib.pyplot as plt
import random
import numpy as np

# Defining Variables:
randounies = np.array([random.randint(1, 6) for x in range(100)])
diceFaces = np.unique(randounies, return_counts=True)[0]
diceOccurences = np.unique(randounies, return_counts=True)[1]

# Print the occurrences of each dice face
for face, count in zip(diceFaces, diceOccurences):
    print(f"The Number {face} appears {count} times.")
    print(f"The Probability of {face}: {count/face:.2f}%")

# Plotting:
plot, ax = plt.subplots()
ax.plot(diceFaces, diceOccurences)

plt.title('Random Dice Rolls')
plt.xlabel('Dice Face')
plt.ylabel('Frequency')

plt.show()