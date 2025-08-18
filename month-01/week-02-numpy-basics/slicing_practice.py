import numpy as np

# Create a 5x5 array with numbers from 0 to 24
data = np.arange(25).reshape(5, 5)

# test = data[2,3]
# print(test)

print("Original 5x5 Array:")
print(data)
print("-" * 20)

# # Get a single element: Select the element in the 3rd row (index 2) and 4th column (index 3).
print(f"""1. Single Element at (2, 3):
{data[2,3]}
""")

# # Get a full row: Select the entire 2nd row (index 1).
print(f"""2. Entire Second Row (index 1):
{data[1, :]}
""")

# # Get a full column: Select the entire 3rd column (index 2).
print(f"""3. Entire Third Column (index 2):
{data[:, 2]}
""")  

# # Get a sub-region: Select the 2x2 square from the top-right corner of the data array.
print(f"""4. Top-Right 2x2 Sub-region:
{data[:2, 3:]}
""")     

selected_row = data[2, :]
condition = selected_row > 12
selected_numbers = selected_row[condition]

# # Get elements based on a condition: Select all numbers in the 3rd row (index 2) that are greater than 12.
print(f"""5. Elements in Row 2 > 12:
{selected_numbers}
""")