class Model:
    a = 1
    def __init__(self, info):
        self.info = "une information"

    def __len__(self):
        return len(self.info)

    # in "une" in m est contenu dans ?
    def __contains__(self, str):

        return str in self.info 

    def __str__(self):

        return "J'ai fait un print sur l'objet"

    # self c'est la référence à l'instance nécessaire pour définir
    # une méthode que l'on souhaite applée à partir de l'objet
    def hello(self, message):
        print( f'Hello {message} !')

# initialisation de la classe 
m = Model('Une information')

m.hello('World !')

# accéder à la valeur de l'attribut
print(m.info)

print(m.a)
print(Model.a) 

print(len(m))
print(m)

print("une" in m)