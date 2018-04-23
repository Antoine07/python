while True:
    try:
        x = int(input("Entrez un nombre :"))
        break
    except ValueError:
        print("Désolé ceci n'est pas un nombre ...")


class EmptyNumberListError(Exception):
    pass 


# test avec une liste vide 
l = []

# on essaye le code 
try :
    # raise sera lancée si la liste est vide
    if not l:
        raise EmptyNumberListError("Votre liste de nombre est vide")

except EmptyNumberListError as e:
    print(type(e)) # <class '__main__.EmptyNumberListError'>
    print(e)

