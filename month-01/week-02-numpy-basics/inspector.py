import numpy as np

matrix = np.ones((3, 4), dtype=float)
vector = np.arange(5, 20)

summary = f"""
--- Matrix Analysis ---
{matrix}
Shape: {matrix.shape}
Dimensions: {matrix.ndim}
Data Type: {matrix.dtype}

--- Vector Analysis ---
{vector}
Shape: {vector.shape}
Dimensions: {vector.ndim}
Data Type: {vector.dtype}
"""

print(summary)