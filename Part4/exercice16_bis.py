# Exercice 16

"""
Dessiner un damier avec contour 

"""
N = 25

for l in range(N):
    for c in range(N):
        if l == 0 or l == (N-1) or (c == 0 or c == (N-1)):
            sym = "X"
        elif (l + c) % 2 == 0:
                sym = "#"
            else:
                sym = "0"
        print(sym, end="")
    print()

