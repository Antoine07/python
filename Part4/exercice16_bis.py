# Exercice 16_bis

"""
@Author: Antoine07
@Contributor: yukii
Dessiner un damier avec contour version optimisée
"""
N = 80
SEPARATOR_MOTIF = "X"
FIRST_MOTIF = "#"
SECOND_MOTIF = "O"

for l in range(N):
    for c in range(N):
        if l == 0 or l == (N-1) or (c == 0 or c == (N-1)):
            sym = SEPARATOR_MOTIF
        else:
            sym = SECOND_MOTIF if (l + c) % 2 else  FIRST_MOTIF
        print(sym, end="")
    print()