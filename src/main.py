import numpy as np
from scipy.optimize import linear_sum_assignment

def combinations_fixed_sum_limits(fixed_sum, length_of_list, minimum, maximum, lst=[]):
  if length_of_list == 1:
    lst += [fixed_sum]
    if fixed_sum >= minimum[-length_of_list] and fixed_sum <= maximum[-length_of_list]:
      yield lst
  else:
    for i in range(min(fixed_sum, maximum[-length_of_list]), minimum[-length_of_list]-1, -1):
      yield from combinations_fixed_sum_limits(fixed_sum-i, length_of_list-1, minimum, maximum, lst + [i])


# np array
# [0:4 , 0:2 ] empty
# [4: , 0 ] index
# [4: , 1 ] additional info, eg name of people
# [0 ,  2: ] group info, eg name or index
# [1:4, 2: ] = groupsize
# [4: , 2:] = rawdata
inputdata = np.genfromtxt('data.csv', delimiter=';')
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


class Groups:
  def __init__(self, groupsizing, total):
    self.total = total
    self.min_lst = groupsizing[0, :]
    self.min_total = np.sum(self.min_lst)
    self.max_lst = groupsizing[1, :]
    self.max_total = np.sum(self.max_lst)
    if (self.min_total > total) or (self.max_total < total):
      raise ValueError('Please check your data, we cant solve your problem')
    self.current = groupsize[2, :]

    while sum(self.current) < total:
      i = 0
      while i < len(self.current) and sum(self.current) < total:
        if self.max_total[i] > self.current[i]:
          self.current[i] += 1
        i += 1

    while sum(self.current) > total:
      i = 0
      while i < len(self.current) and sum(self.current) > total:
        if self.min_total[i] < self.current[i]:
          self.current[i] -= 1
        i += 1

    self.current = self.min_lst.copy()

    for i in range(len(self.current)):
      while self.total > sum(self.current) and self.current[i] < self.max_lst[i]:
        self.current[i] += 1

    print(type(self.min_lst))
    self.combinations = combinations_fixed_sum_limits(self.total, len(self.current), self.min_lst, self.max_lst)

  def __iter__(self):
    return self

  def __next__(self):
    return next(self.combinations)


possible_groups = Groups(groupsize.astype(int), rawdata.shape[0])

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


