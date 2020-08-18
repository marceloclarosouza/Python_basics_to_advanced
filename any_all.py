# all() return True if all iterables are true or if the data it is empty (in boolean 0 is false)

print(all([1,2,3,4,5]))
print(all([0,1,2,3,4,5]))
print(all("oi"))
print(all([]))

nomes = ["Carlos", "Camile", "Cado", "Caio"]
print(all([nome[0] == 'C' for nome in nomes]))
print(all([nome[1] =='v' for nome in nomes]))

print(all([num%2 ==0 for num in [2,4,6,8,10]]))
#print(all([num for num in [2,4,6,8] if num % 2 != 0]))  tem alguma coisa errada
print(all([num%2 !=0 for num in [2,4,6,8,10]]))








# any() return Trye if any of the iterables are True

#print(any([0,1,2,3,4]))
#print(any([0]))
