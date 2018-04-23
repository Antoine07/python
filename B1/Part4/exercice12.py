# Exercice 12:
import matplotlib.pyplot as plt

N  = 1458758458758
syracuse = []

while N != 1:

    if N % 2 == 0:
        N = N // 2
    else:
        N = 3*N + 1

    syracuse.append(N)

print(max(syracuse))

plt.plot(syracuse)
plt.show()