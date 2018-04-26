

def max_with_indice(l):

    # not l <=> vérifier que la liste est vide
    if not l:
        raise "Votre liste est vide ..."

    # le premier élément numérique de la liste est considé comme étant le plus 
    # grand de manière arbitraire.
    pos, candidate = 0, l[0]

    for i in range(1, len(l)):
        if candidate < l[i]:
             pos, candidate = i, l[i]

    return pos, candidate