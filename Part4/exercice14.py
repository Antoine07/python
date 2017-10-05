# Exercice 14

"""
Trouvez tous couples de deux valeurs (a,b) qui sont égale à 10
"""

a = 10
result = []

while a >= 0:

    for num in range(0, 11):

        if a + num == 10:
            result.append([a,num])

    a = a - 1

print(result)