
def combinations_fixed_sum(fixed_sum, length_of_list, lst=[]):
  if length_of_list == 1:
    lst += [fixed_sum]
    yield lst
  else:
    for i in range(fixed_sum+1):
      yield from combinations_fixed_sum(i, length_of_list-1, lst + [fixed_sum-i])

def combinations_fixed_sum_limits(fixed_sum, length_of_list, minimum, maximum, lst=[]):
  if length_of_list == 1:
    lst += [fixed_sum]
    if fixed_sum >= minimum[-length_of_list] and fixed_sum <= maximum[-length_of_list]:
      yield lst
  else:
    for i in range(min(fixed_sum, maximum[-length_of_list]), minimum[-length_of_list]-1, -1):
      yield from combinations_fixed_sum_limits(fixed_sum-i, length_of_list-1, minimum, maximum, lst + [i])
