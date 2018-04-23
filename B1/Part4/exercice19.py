# Exercice 19
import random

count = 1
number_search = random.randint(0,100)

# print(number_search) # debug 

number = int( input("Choisir un nombre entre 0 et 100 \n") )

while number != number_search :

    if number > number_search:
        print("C'est trop grand réessayer")
    else:
        print("C'est trop petit réessayer")

    number = int( input("Choisir un nombre entre 0 et 100 \n"))
        
    count = count + 1


print("Vous avez trouve le nombre", number_search, "en ", count, "coup(s)")

    