
def xrange():
    count = 0
    while True:
       count += 1
       yield count # retourne un élément à chaque appel

# fonction itérable
# signature : <generator object xrange at 0x7f0b1d82c518>
print(xrange())

for x in xrange():
    if x > 2:
        break
    print(x)

class Iterateur:

    def __init__(self, data):
        self.data = data
        self.count = -1
        self.len = len(data) - 1

    def __iter__(self):
       return self 

    def __next__(self):

        if self.len == self.count :
            raise StopIteration

        self.count += 1

        return self.data[self.count]


Iterable = Iterateur([1,2,3])

for elem in Iterable:
    print('premier passage' , elem)

# pas de deuxième passage
# print(next(Iterable)) # renverra StopIteration => fin
for elem in Iterable:
    print('deuxième passage', elem)


