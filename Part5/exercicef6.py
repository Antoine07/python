"""
Correction exercice f6
"""
# fonctions utiles
def remove_elem(elem_search, l):
	new_list = []

	for e in l:
		if elem_search != e:
			new_list.append(e)

	return new_list

l = [1,2,3,4,5,6,8]
l = remove_elem(4, l) #  on écrase la liste précédente 
print(l)
