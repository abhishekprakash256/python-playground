import numpy as np

# 1. Load the CSV file as strings


# Load data (as string because of mixed types)
data = np.genfromtxt("iris_full_numpy.csv", delimiter=",", dtype=str, skip_header=1)

#6.1
x = data[:, 1:4].astype(float)

# Subset the last column into yStr (species names)
yStr = data[:, -1]