# Exercice 16

"""
Dessiner un damier avec contour 

"""
N = 25

for l in range(N):
    for c in range(N):
        if l == 0 or l == (N-1) or (c == 0 or c == (N-1)):
            sym = "X"
        else:
            if l % 2 == 0:
                sym = "#"
                if c % 2 == 0:
                    sym = "0"
            else:
                sym = "0"
                if c % 2 == 0:
                    sym  = "#"
        print(sym, end="")
    print()

