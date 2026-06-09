
""" ================ Deep Copy Shallow Copy ================= """
import copy

# deep copy

original = [[1, 2], [3, 4], [5, 6]]
print(original)
copied = copy.deepcopy(
original)
print(copied)
original [0][0] = 100
print(original)
print(copied)


# shallow copy

original = [[1, 2], [3, 4], [5, 6]]
print(original)
copied = copy.copy(
original)
print(copied)
original [0][0] = 100
print(original)
print(copied)
