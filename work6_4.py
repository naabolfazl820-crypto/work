set_a={1,2,3,4,5}
set_b={4,5,6,7,8}
set_a.add(10)
print(set_a)
set_a.remove(10)
set_a.discard(100)
print(set_a)
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
smal_set={1,2}
print(smal_set.issubset(set_a))
poped_val= set_a.pop()
print(set_a)