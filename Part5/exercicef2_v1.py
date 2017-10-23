"""
Correction exercice f2 v1

"""

def add(a,b):
    return a + b

data = []
# tableau de message
messages = ["Donner la première valeur entière à additionner \n", "Donner la deuxième valeur entière à additionner \n"]

while len(data) != 2 :
    pos = len(data)
    # la longueur du tableau data donne la position du message à afficher
    choice = input(messages[pos])

    if choice.isdecimal() == False :
        print("Vous devez entrer un nombre")
    else:
        # ne pas oublier de forcer le type 
        choice = int(choice)
        data.append(choice)
    
    
print("Voici la somme des nombres que vous avez choisi : \n", add(data[0], data[1]))

