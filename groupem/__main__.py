import numpy as np
from scipy.optimize import linear_sum_assignment

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
inputdata = np.genfromtxt('data/data.csv', dtype='|U8', delimiter=';')

# np array
# containing data
# rows : people
# colums : groups
choice = inputdata[4: , 2:].astype(int)

# np array
# column for each group
# [0, :] min
# [1, :] max
# [2, :] optimal
groupsize = inputdata[1:4, 2:].astype(int)

names = inputdata[4: , 1 ]
groupnames = inputdata[0, 2:]


'''
transforming data
'''
transformed_choice = choice - np.amin(choice) + 1
transformed_choice = transformed_choice / np.amax(transformed_choice)
transformed_choice = - np.log(transformed_choice)


'''
group combinations
'''
possible_groups = groups.Groups(groupsize.astype(int), choice.shape[0])


'''
match linear_sum_assignment to original group
'''
def output_solution(choice_interval, col_ind):
  assigned_group = []
  for val in col_ind:
    assigned_group.append(next(x[0] for x in enumerate(choice_interval) if x[1] > val))
  return assigned_group


'''
calculate the overall choice satisfaction
'''
def rate_assigned_groups(assigned_groups, transformed_choice):
  rating = 0
  for i, gr in enumerate(assigned_groups):
    rating += transformed_choice[i][gr]
  return rating


'''
find the best best match in all possible_groups
'''
best_solution = []
best_solution_rating = np.amax(transformed_choice) * choice.shape[0]

for i in possible_groups:
  transformed_choice_spread = np.repeat(transformed_choice, i, axis=1)
  row_ind, col_ind = linear_sum_assignment(transformed_choice_spread)
  choice_interval = np.cumsum(i)
  current_assigned_groups = output_solution(choice_interval, col_ind)

  rating = rate_assigned_groups(current_assigned_groups, transformed_choice)
  if rating < best_solution_rating:
    best_solution = current_assigned_groups
    best_solution_rating = rating


'''
print the best match
'''
for j, val in enumerate(best_solution):
  print('{:8}  {:8}  {:4}'.format(names[j], groupnames[val], ('(b) ' if (choice[j][val] == np.amax(choice[j])) else '(nb)')))
