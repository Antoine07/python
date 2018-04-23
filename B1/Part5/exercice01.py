
"""
Manière séquentielle de recherche
"""
l = [1,2,3,4,5,6,77]

a = 5
flag = False

for i,e in enumerate(l):
    if e == a:
        flag = True
        break

if flag:
    print("Trouvé", i)
else:
    print("Pas trouvé", i)