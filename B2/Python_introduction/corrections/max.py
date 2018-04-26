
def max_with_indice(l):
    if not l:
        raise "Votre liste est vide"
   # unpacking 
    pos, candidate = 0, l[0]

    for i in range(1, len(l)):
        if candidate < l[i]:
            pos, candidate = i, l[i]

    return pos, candidate


# tester la fonction

print(max_with_indice([1,2,3,7,99,8,100,789,97]))

# leve une exception et donc arrete les script 

print(max_with_indice([]))