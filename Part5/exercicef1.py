"""
Correction exercice f1
"""
# définition de la fonction 
def add(a,b):
    return a + b

data = []

while len(data) != 2 :
    choice = int(input("saisir une valeur \n"))
    data.append(choice)
 
    
print("Voici la somme des nombres que vous avez choisi : ", add(data[0], data[1]))

