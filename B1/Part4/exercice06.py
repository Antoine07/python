# Exercice 6
"""
On utilise la propriété max(a,b,c) = max(max(a,b),c), qui notez le pourrait s'appliquer à plus de 3 nombres :
max(max(max(a,b),c),d), etc
"""
a,b,c = 1000,1000001,1200

if a > b:
    m = a
else:
    m = b

if c > m:
    m = c

print("Le max est ", m)