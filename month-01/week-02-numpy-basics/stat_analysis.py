import numpy as np

# Data from 3 trials, with 4 sensor readings each
experiment_data = np.array([
    [12, 15, 11, 14],
    [20, 22, 19, 21],
    [8,  10, 11, 9]
])

print("Original Experiment Data:")
print(experiment_data)
print("-" * 25)

sum = experiment_data.sum()
print(sum)