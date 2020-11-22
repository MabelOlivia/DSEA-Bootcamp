import numpy as np
import statistics

rang = np.random.randint(30, 70, size=6)

print("range is:", rang)

print("Maximum number is : ", max(rang))
print("Mean is:", statistics.mean(rang))
print("Median is:", statistics.median(rang))
print("Mode is:", statistics.mode(rang))

