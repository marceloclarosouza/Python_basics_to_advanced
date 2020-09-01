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

#fibonacci com generator