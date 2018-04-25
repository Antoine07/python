"""
La logique du jeu est placé dans la classe ci-dessous
"""

class Battle_Number:

    def __init__(self, data):
        self.data = data
        # les données sont placées dans un dictionnaire
        self.players = { 'player1' : {'name' : '', 'score' : 0} ,  'player2' : {'name' : '', 'score' : 0} } 

    """
    cette méthode est une méthode spéciale qui permet récupérer/assigner une valeur à notre objet 
    game['player1'] = 'Alan' 
    la clé key est donnée par player1 ici et name est la valeur, codez le code permettant d'assigner le bon nom au 
    bon name dans le dictionnaire self.players de la classe 
    """
    def __setitem__(self, key, name):
        pass 

    """
    Logique du jeu vous devez parser les données data '5 6' correspond joueur 1 et 2 ici c'est le deuxième joueur 
    qui gagne car 6 > 5, si égalité c'est 0 et 0 pour tout le monde. 
    Un joueur qui gagne remporte + 1 dans son score.

    """

    def __run(self):
        pass

    def __str__(self):

        self.__run()

    def reset():
        self.data = []
        self.players = []

battle = [
    '19', '3 10', '1 2', '2 6', '1 2', '10 1', '8 5', '8 3', '9 7', '3 4',
    '5 9', '3 7', '3 6', '2 6', '6 10', '7 4', '1 10', '4 1', '9 1', '6 2',
]

game = Battle_Number(battle)

game['player1'] = 'Alan'
game['player2'] = 'Albert'

# afficher le gagnant 
print(game)