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

print(f"""1. Overall Sum:
{experiment_data.sum()}
""")

print(f"""2. Overall Average:
{experiment_data.mean()}
""")

print(f"""3. Sum of each Column:
{experiment_data.sum(axis=0)}
""")

print(f"""4. Maximum value of each Row:
{experiment_data.max(axis=1)}
""")
