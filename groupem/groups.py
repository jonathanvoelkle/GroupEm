
import numpy as np

import combinations


class Groups:
  def __init__(self, groupsizing, total):
    self.total = total
    self.min_lst = groupsizing[0, :]
    self.min_total = np.sum(self.min_lst)
    self.max_lst = groupsizing[1, :]
    self.max_total = np.sum(self.max_lst)
    if (self.min_total > total) or (self.max_total < total):
      raise ValueError('Please check your data, we cant solve your problem')
    self.current = groupsizing[2, :]

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
    self.combinations = combinations.combinations_fixed_sum_limits(self.total, len(self.current), self.min_lst, self.max_lst)

  def __iter__(self):
    return self

  def __next__(self):
    return next(self.combinations)
