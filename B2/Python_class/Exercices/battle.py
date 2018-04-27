# programme principal
class Game:

    def __init__(self, data):
        self.data = data 
        self.players = []

    def player(self, name):

        # raise leve une exception et donc stop les script
        if len(self.players) == 2:
            raise "Vous ne pouvez plus ajouter de joueur"

        self.players.append({'name' : name, 'score' : 0})

    
    def run(self):
        if len(self.players) != 2:
            raise  f"Vous ne pouvez pas commencer le jeu, il faut deux joueurs,({len(self.players)}"

        for data in self.data[1:]:
            d = data.split(' ')
            d1 = int(d[0])
            d2 = int(d[1])
            if d1 == d2:
                continue 
            if d1 > d2 :
                self.players[0]['score'] += 1
            else:
                self.players[1]['score'] += 1

    def __str__(self):

        p1, p2  = self.players[0], self.players[1]

        if p1['score'] > p2['score']:
            return f"Le gagnant est {p1['name']} avec le score : {p1['score']}"
        elif  p1['score'] < p2['score']:
            return f"Le gagnant est {p2['name']} avec le score : {p2['score']}"
        else:
            return "Exaequo"

# bootstrap 

battle = [
    '19', '3 10', '1 2', '2 6', '1 2', '10 1', '8 5', '8 3', '9 7', '3 4',
    '5 9', '3 7', '3 6', '2 6', '6 10', '7 4', '1 10', '4 1', '9 1', '6 2',
]

game = Game(battle)
game.player('Alan')
game.player('Albert')

# run du jeu 
game.run()

print(game)

print(game.players)

