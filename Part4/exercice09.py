# Exercice 8

"""
Supposons que la liste est une liste d'entiers positifs
"""

l = [1,120,45,89,235600,12,4587,125,6,88,10235]

m = 0 # comme la liste est une liste de nombre positif on prend m = 0 comme premier élément

for elem in l:

    if elem > m :
        m = elem


print("Max de la liste", m)

"""
Voici une autre version possible, dans ce cas la liste peut être une liste quelconque de nombre 
"""

m = l[0] # on prend le premier élément de la liste
N = len(l) 
for pos in range(1, N):

    if l[pos] > m:
        m = l[pos]

print("Max de la liste", m)