sets = {1,3,4,6}

# print(type(sets))

print(sets)

sets.add(7)

print(sets)

sets.remove(6)
print(sets)

s1 = {1,23,67,45,90}
s2 = {2,23,65,67,97,98}
print("union:",s1.union(s2))

print("Intersection: ",s1.intersection(s2))

print("Diffrence: ",s1.difference(s2))

print({23,90}.issubset(s1))
print({23,90}<=s1) # Shoctcut for checking the subset


