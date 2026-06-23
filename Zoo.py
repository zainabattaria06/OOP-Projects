from abc import ABC, abstractmethod
class Animal(ABC):
    zoo_name="The Python Zoo"

    def __init__(self,name,species):
        self.name=name
        self.species=species

    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, species="Lion")
    def make_sound(self):
        return f"{self.name} roars: Roar!"
    def eat(self):
        return f"{self.name} eats a large piece of meat."

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, species="Monkey")
    def make_sound(self):
        return f"{self.name} chatters: Ooh ooh aah aah!"
    def eat(self):
        return f"{self.name} peels and eats a banana."
    
class Penguin(Animal):
    def __init__(self, name):
        super().__init__(name, species="Penguin")
    def make_sound(self):
        return f"{self.name} honk: Honk!"
    def eat(self):
        return f"{self.name} eats some fish."
    def slide(self):
        return f"{self.name} slides on its belly!"

class Zookeeper:
    def __init__(self, name):
        self.name=name
        import random 
        random_number=(random.randint(1000,9999))
        self._employee_id=random_number
        self.__salary=45000
        
    def feed_animals(self, animals_list):
        print("\n---Feeding Animals---")
        for animal in animals_list:
            print(animal.eat())

leo=Lion("Leo")
momo=Monkey("Momo")
pingu=Penguin("Pingu")
animals=[leo,momo,pingu]
zookeeper=Zookeeper("Hamza")

for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    print(f"{animal.name} lives at {animal.zoo_name}.") 
    print()

leo.favorite_toy="Big red ball"   
print(f"Leo favorite toy is {leo.favorite_toy}")
print()

print(zookeeper._employee_id)
print(zookeeper._Zookeeper__salary)
zookeeper.feed_animals(animals)