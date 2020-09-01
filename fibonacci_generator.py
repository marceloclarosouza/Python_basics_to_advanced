#fibonacci sem generator

def fibo_pythonic(max):
    nums = []
    a,b = 0,1
    while len(nums)<=max:
        nums.append(b)
        a,b = b, a+b#a recebe b, e b recebe a+b        
    return nums

for n in fibo_pythonic(7):#print a number per line
    print(n)
    
print("\n")
print(fibo_pythonic(7))#print a LIST
print("\n\n")

#fibonacci com generator consome 150vezes menos memória !!!

def fibo_generator(max):
    a,b, contador = 0,1,0
    contador = 1
    while contador<max:
        yield b
        a,b =b, a+b
        contador += 1
        
for n in fibo_generator(7):
    print (n)
print("\n")
print(fibo_generator(7))##generator
print(list(fibo_generator(7)))##convertendo o generator em LIST
