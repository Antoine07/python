# Exercice 16

"""
Dessiner un damier

"""

for l in range(10):
    for c in range(10):
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

