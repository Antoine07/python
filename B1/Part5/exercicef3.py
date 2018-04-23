"""
Correction exercice f3
"""
# Exercice f3
# les fonctions utiles
# fonction pour faire la somme d'entiers dans un tableau
def total(a):
	s = 0
	for e in a:
		s = s + e

	return s

# programme principal

data = []

while True:
    # compter le nombre d'éléments dans le tableau
	count = len(data)
	print("Saisir la valeur ", count + 1, " numérique \n")
	choice = input()

	if choice == 's' or choice == 'stop':
		break

	 # une valeur numérique 
	if choice.isdecimal() == True:
	    data.append(int(choice))
	else:
	 	print("Vous devez rentrer une valeur numérique")


print("La somme des/la valeur(s) saisie(s) est :", total(data))