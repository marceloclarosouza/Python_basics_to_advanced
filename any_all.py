# all() return True if all iterables are true or if the data it is empty (in boolean 0 is false)

print(all([1,2,3,4,5]))
print(all([0,1,2,3,4,5]))
print(all("oi"))
print(all([]))

nomes = ["Carlos", "Camile", "Cado", "Caio"]
print(all([nome[0] == 'C' for nome in nomes]))
print(all([nome[1] =='v' for nome in nomes]))

print(all([num%2 ==0 for num in [2,4,6,8,10]]))
print(all([num%2 ==0 for num in [3,4,6,8]]))
print(all([num%2 !=0 for num in [2,4,6,8,10]]))


#any() return Trye if any of the iterables are True

print(any([0,1,2,3,4]))
print(any([0]))

print(any([num%2 ==0 for num in [1,3,5,7]]))
