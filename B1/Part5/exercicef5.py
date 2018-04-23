"""
Correction exercice f5
"""
# fonction utile
def search_pos(char, text):
	pos = 0
	for c in text:
		if c == char:
			return pos 
		pos = pos + 1

	return None 

# programme principale
char = "A"
text = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
search = search_pos(char, text)

if search != None:
	print("La position du caractères", char, " est :", search)
else:
	print("Le caractère ", char, " n'a pas été trouvé")

