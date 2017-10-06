# Exercice 17

import math, random

r = 2 # rayon du cercle

impacts = 0
N = 1000000

for _ in range(N):
    # un tire
    fire_x = random.randint(-10,10)
    fire_y = random.randint(-10,10)
    # calcul de la distance
    d = math.sqrt(fire_x**2 + fire_y**2)
    if d <= r:
	    impacts = impacts + 1
    

print(impacts/N)