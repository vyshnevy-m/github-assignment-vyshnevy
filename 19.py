#shallow copy
import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.copy(list1)

print(list1 == list2)
print(list1 is list2)
print(list1[0] is list2[0])