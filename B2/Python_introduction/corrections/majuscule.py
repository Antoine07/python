def is_upper_list(l):

    if not l:
        raise "La liste est vide"
    
    return all(ord(ch) in range(65,91) for ch in l)

l1 = ['A','B', 'C', 'D']
l2 = ['A','B', 'c', 'D']

print(is_upper_list(l1))
print(is_upper_list(l2))