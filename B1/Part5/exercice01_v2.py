"""
Manière séquentielle de recherche 
"""
l = [1,2,3,4,5,6,77]
a = 77
i = 0 

# Notez l'utilisation du test paresseux
# 6 < 7, l[6] 
while i < len(l) and l[i] != a:
    i = i + 1
    print(i)

if i < len(l):
    print("Trouvé")
else:
    print("Pas trouvé")

