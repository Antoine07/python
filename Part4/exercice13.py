# Exercice 13

fibonacci = []
N = 100
u0 = 1
u1 = 1
fibonacci.append(u0)
fibonacci.append(u1)

for _ in range(0, N):

    u = u0 + u1
    fibonacci.append(u)

    u0 = u1
    u1 = u

print(fibonacci)