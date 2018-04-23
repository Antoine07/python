# correction pour le premier exercice
N = int(lines[0]) # '2'
# afficher le gagnant soit A soit B print("A") ou un print("B")
countA = 0
countB = 0
for t in lines[1:]:
    t = t.split(" ") # ['1', '2'] int(t[0])
    if int(t[0]) > int(t[1]) :
        countA += 1
    elif int(t[0]) == int(t[1]):
        continue
    else: 
        countB += 1

if countA > countB:
    print("A")
else:
    print("B")