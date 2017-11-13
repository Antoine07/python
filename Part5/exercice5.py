# Constantes et variables
U0 = 5
A = 2
B = 7
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# codes utiles
def gen_key(u0,a,b):
    vectKey = []
    vectKey.append(u0)
    u = u0
    while True:
        u = (a*u + b) % 26
        if u in vectKey:
            break
        vectKey.append(u)

    return vectKey

# crypto
# le paramètre sens est facultatif car on lui assigne une valeur par défaut
# on peut écraser cette valeur en appelant la fonction
def cryp_message(message, key, sens = 1):
    message_crypt = ''
    length_key = len(key)
    i = 0
    for ch in message:
        if ch == ' ':
            message_crypt += ' '
            continue # permet d'aller à l'itération suivante

        pos = ( LETTERS.index(ch) + sens*key[i % length_key] ) % 26
        message_crypt +=  LETTERS[pos] 

        i += 1

    return message_crypt

# code principal
key = gen_key(U0,A,B) # clé de codage

print(key)

message = "HELLO WORLD"
message_cryp = cryp_message(message, key) 
print(message_cryp)

print(cryp_message(message_cryp, key, -1))