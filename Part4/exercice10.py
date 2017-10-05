# Exercice 10

str = "En Python une chaine de caractere est un objet bien que l on ne puisse pas encore definir exactement cette notion retenez qu un objet possede des methodes Elles sont en Python egalement iterable Soit donc la chaine de caracteres de l enonce de notre exercice compter le nombre de fois qu apparait la lettre e"

count = 0

for c in str:
    if c == 'e' or c == 'E':
        count = count + 1

print(count)

print(str.count('e') + str.count('E'))