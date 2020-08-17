# all() return True if all iterables are true or if the data it is empty (in boolean 0 is false)

print(all([1,2,3,4,5]))
print(all([0,1,2,3,4,5]))
print(all("oi"))
print(all([]))

# any() return Trye if any of the iterables are True

print(any([0,1,2,3,4]))
print(any([0]))
