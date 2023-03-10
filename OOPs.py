#OOPs 

class Person:
    def __init__(self,age,name,gen):
        self.age=age
        self.name=name
        self.gen=gen
    def eat(self):
        print(f"{self.name} ate the mango")
    def support(self):
        print(f"{self.age} plays football")
    def support(self):
        print(f"{self.age,self.gen} plays football")

features=Person(23,"Jan Kosgei","Gen Z")


features.support()


class Team:
    def __init__(self,name,country,position):
        self.name=name
        self.country=country
        self.position=position
    def win(self):
        print(f"{self.name} are Champions elect")
    
mabingwa=Team('Arsenal','England',1)

mabingwa.win()


class Item:
    pass

item1= Item()
print(item1)


class Phone:
    def revenue(self,m,n):
        return m*n
    
brand1=Phone()
brand1.name='Redmi'
brand1.quantity= 634
brand1.price= 1200

print(brand1.revenue(brand1.quantity, brand1.price))

class Students:
    def __init__(self,name,age,strength):
        self.name=name
        self.age=age
        self.strength=strength

student1=Students('Baraka',21,'Python')
student2=Students('Jack',23,'SQL')
student3=Students('Diana',19,'Excel')

print(student1.name)

