import numpy as np
from scipy.optimize import linear_sum_assignment
np.set_printoptions(threshold=np.nan, linewidth=310)

import groups


'''
splicing data
'''
# np array
# [0:4 , 0:2 ] empty
# [4: , 0 ] index
# [4: , 1 ] additional info, eg name of people
# [0 ,  2: ] group info, eg name or index
# [1:4, 2: ] = groupsize
# [4: , 2:] = choice
inputdata = np.genfromtxt('data/data.csv', dtype='|U5', delimiter=';')
print(inputdata)

# np array
# containing data
# rows : people
# colums : groups
choice = inputdata[4: , 2:].astype(int)
print(choice)

# np array
# column for each group
# [0, :] min
# [1, :] max
# [2, :] optimal
groupsize = inputdata[1:4, 2:].astype(int)
print(groupsize)

names = inputdata[4: , 1 ]

print(choice.shape)


'''
transforming data
'''
data = choice - np.amin(choice) + 1
data = data / np.amax(data)
data = - np.log(data)

print(data)


'''
group combinations
'''
possible_groups = groups.Groups(groupsize.astype(int), choice.shape[0])

def output_solution(names, choice_interval, col_ind):
  assigned_group = []
  for val in col_ind:
    assigned_group.append(next(x[0] for x in enumerate(choice_interval) if x[1] > val))
  return assigned_group



solutions = []

for i in possible_groups:
  data_spread = np.repeat(data, i, axis=1)
  choice_interval = np.cumsum(i)
  row_ind, col_ind = linear_sum_assignment(data_spread)
  # print('choice', choice_interval)
  # print('names', names)
  # print('another solution')
  # print('solved', col_ind)

  solutions.append(output_solution(names, choice_interval, col_ind))


print(solutions)







