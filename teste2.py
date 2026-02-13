class Dog:
    family = 'canine'

    def __init__(self, age):
        self.age = age


#-----MAIN

rex = Dog(5)
print(f'A idade do rex é {rex.age} anos e ele é da família {rex.family}')
caramelo = Dog(3)
print(f'A idade do caramelo é {caramelo.age} anos e ele é da família {caramelo.family}')

print(f'Rex e Caramelo pertencem ambos a família {Dog.family}')