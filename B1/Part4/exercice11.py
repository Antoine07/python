# Exercice 11
"""
Retourner les nombres inférieur à 100 et multiple de 7
"""
N = 100
d = 7
result = []
while d < N:

    if d % 7 == 0:
        result.append(d)

    d = d + 1

print(result)
    
"""
Une autre version possible est de calculer tous les multiples de 7 inférieur à 100
"""
N = 100
d = 7
result = []
while d < N:
    result.append(d)

    d = d + 7