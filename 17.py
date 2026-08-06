#deep copy
import copy

list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)

print(list1 == list2)
print(list1 is list2)