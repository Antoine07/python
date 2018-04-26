

def is_upper_list(l):

    if not l:
        raise "La liste est vide"

    return all(ord(ch) in range(65,91) for ch in l)

l1 = ['A','B', 'C', 'D']
l2 = ['A','B', 'c', 'D']

print(is_upper_list(l1))
print(is_upper_list(l2))

print( sum(x**2 for x in range(10)) )

print( [(x,y) for x in range(10) for y in range(10)] )

def verify(x):
    if x % 2 == 0:
        return True 
    else:
        return True

print( [x for x in range(10) if verify(x)])