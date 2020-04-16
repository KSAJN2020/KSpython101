frozen_set1 = frozenset(["e", "f", "g", "a", "b"])
print(len(frozen_set1))
for x in frozen_set1:
    print(x)
frozen_set1.clear()

set1 = {'a', 'b', 'c'}
print(len(set1))
for y in set1:
    print(y)
set1.clear()

print(frozen_set1.issuperset(set1))
print(set1.issubset(frozen_set1))
# sets are not traversed sequentially
