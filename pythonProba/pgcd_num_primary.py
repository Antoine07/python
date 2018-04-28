"""
En admettant que 

si b divise a alors pgcd(a,b) = b et si b ne divise pas a alors pgcd(a,b) = pgcd(b, a % b)
Ecrivez une fonction permettant de déterminer le pgcd de deux nombres a et b

calculer/simuler à l'aide de Python la probabilité de tirer deux nombres premiers entreux au hasard 

"""

import random as r

# Fonction permettant de calculer le pgcd de deux nombres
def pgcd(a,b):

    # on réordonne les paramètres si besoin
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b 
    else: 
        return pgcd(b, a%b)

def nb_primary(n, draw):
    i = 0
    number_primary = 0

    while i < draw:
        i += 1
        a = r.randint(1,n)
        b = r.randint(1,n)

        if pgcd(a,b) == 1:
            number_primary += 1

    return number_primary

# cette probabilité tend quand n tend vers l'infini vers 6/pi^2

n, draw = 100000, 1000000
print(nb_primary(n, draw)/draw)
