class A:
    def my_method(self, m):
        self.m = m 

    def other_method(self):
        return "Une autre méthode de la super classe"

class C(A):
    def my_method(self, m):
        self.m = m.lower() 

c = C()

c.my_method("Hello world !")
print(vars(c))  # {'m': 'hello world !'}

# Vous pouvez accéder à la méthode de la super classe

print(c.other_method())

# class A:
#     pass

# print(A.__bases__) # (<class 'object'>,)


class SuperA:
    pass 

class SuperB:
    pass 

class A(SuperA, SuperB):
    pass 

# [<class '__main__.A'>, <class '__main__.SuperA'>, <class '__main__.SuperB'>, <class 'object'>]
print(A.mro())

class B(SuperB, SuperA):
    pass

# [<class '__main__.B'>, <class '__main__.SuperB'>, <class '__main__.SuperA'>, <class 'object'>]
print(B.mro())