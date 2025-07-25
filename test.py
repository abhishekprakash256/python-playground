import numpy as np

# 1. Load the CSV file as strings


# Load data (as string because of mixed types)
data = np.genfromtxt("iris_full_numpy.csv", delimiter=",", dtype=str, skip_header=1)

#data = np.loadtxt("iris_full_numpy.csv", delimiter=",", dtype=str , skip_row=1)

#6.1
x = data[:, 1:4].astype(float)

# Subset the last column into yStr (species names)
yStr = data[:, -1]


#6.2 

print(yStr)

unique_vals , y = np.unique(yStr, return_inverse = True)


#6.3
y = y.reshape(150,1)

combinedArr = np.concatenate((x, y), axis=1)


#6.4 
num_samples = x.shape[0]  # total number of samples

# Step 1: Create an array of shuffled indices
indices = np.arange(num_samples)

np.random.shuffle(indices)

# Step 2: Split the indices into 70% train and 30% test
split_point = int(0.7 * num_samples)

train_indices = indices[:split_point]

test_indices = indices[split_point:]

# Step 3: Use the indices to split x and y
xTrain = x[train_indices]

xTest = x[test_indices]

yTrain = y[train_indices]

yTest = y[test_indices]


#6.5 

# 1. Mean of each column 
column_means = np.mean(xTest, axis=0)

# 2. Max value of each row 
row_maxes = np.max(xTest, axis=1)




#5 --

arr = np.array([15,12,2,43,12,6,6,15,8,2])

#get the unique soln
unique_vals, counts = np.unique(arr, return_counts=True)


duplicate_vals = []

for val,freq in zip(unique_vals,counts) :

    if freq > 1 :

        duplicate_vals.append(val)


print(duplicate_vals)



