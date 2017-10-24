
# Exercice f4

a = 5
n = 2

def power(a,n):
	if n < 0:
		return "Impossible"
	b = 1 
	for _ in range(n):
		b = a * b # a*1, a*b <=> a*a, a*a*a, ...
	return b

# tests
print(power(2,3))
print(power(2,0))
print(power(2,1))
print(power(2,8))
print(power(2,-1))