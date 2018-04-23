"""
Exemple de contexte Manager 
"""
import time as t 

class CalculTime:
    def __enter__(self):
        self.start = t.time()

        return self 

    def __exit__(self, *args):
        duration = t.time() - self.start
        print(f" durée lorsqu'on sort du with  : {duration} ")

        # permet de faire remonter les exceptions à défaut elle est catché par la structure with
        # bonne pratique mettre False
        return False 

    def between(self):
        duration = t.time() - self.start

        return f"Between time : {duration}"

with CalculTime() as c:
    count = 0
    while True:
        if count > 100000:
            break
        count += 1
    print('durée du premier bloc ', c.between())

    # si on fait ici une exception on sortira du code 
    # 1/0 seul la première durée sera affichée
    count = 0
    while True:
        if count > 100000:
            break
        count += 1



