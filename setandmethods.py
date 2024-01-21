# Set stores the unique values and not in order

set1 = {1, 2, 3, 4, 5, 5, 5}
# print(set1)
set2 = {11, 22, 33, 4}

print(set1.union(set2))
print(set2.intersection(set1))

print(set1.pop())
print(set1)
