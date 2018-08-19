import numpy as np
from scipy.optimize import linear_sum_assignment

import groups


# np array
# [0:4 , 0:2 ] empty
# [4: , 0 ] index
# [4: , 1 ] additional info, eg name of people
# [0 ,  2: ] group info, eg name or index
# [1:4, 2: ] = groupsize
# [4: , 2:] = rawdata
inputdata = np.genfromtxt('tests/data.csv', delimiter=';')
print(inputdata)

# np array
# containing data
# rows : people
# colums : groups
rawdata = inputdata[4: , 2:]
print(rawdata)

# np array
# column for each group
# [0, :] min
# [1, :] max
# [2, :] optimal
groupsize = inputdata[1:4, 2:]
print(groupsize)


possible_groups = groups.Groups(groupsize.astype(int), rawdata.shape[0])

for i in possible_groups:
  print(i, sum(i))

print(rawdata.shape)
dataset = np.empty(rawdata.shape)

print(dataset)

dataset = dataset - np.amin(dataset) + 1
dataset = dataset / np.amax(dataset)
dataset = - np.log(dataset)

# dataset = - (dataset - 1)

print(dataset)

# cost = np.array([[0, 0, 0.4, 0.6], [0.4, 0.6, 0, 0.8], [0.8, 0.6, 0.4, 0.8], [0, 0.4, 0.4, 0.2]])
# print(cost)

# row_ind, col_ind = linear_sum_assignment(cost)
# print(np.transpose(col_ind))


row_ind, col_ind = linear_sum_assignment(dataset)
print(col_ind)


