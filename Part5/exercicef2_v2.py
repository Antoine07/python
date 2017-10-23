"""
Correction exercice f2 v2

Ici on utilise un try except structure Pyhton qui permet de gérer les exceptions rencontrées par le programme, int() va lancer une exception sur une chaîne de caractères que l'on traiter dans le bloc expect en nommant l'exception ici ValueError

"""

def add(a,b):
    return a + b

data = []
messages = ["Donner la première valeur entière à additionner \n", "Donner la deuxième valeur entière à additionner \n"]

while len(data) != 2 :
    try:
        pos = len(data)
        choice = int(input(messages[pos]))
        data.append(choice)
    except ValueError:
        print("Attention vous devez entrer un entier \n")
    
print("Voici la somme des nombres que vous avez choisi : ", add(data[0], data[1]))

