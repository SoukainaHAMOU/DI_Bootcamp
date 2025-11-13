#Exercise 1: Pets

class Pets:
    def __init__(self,animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True
    def __init__(self,name):
        self.name = name

    def walk(self):
        return f"{self.name}is walking around."
    
class Siamese(Cat):
    pass
class Chartreux(Cat):
    pass
class Bengal(Cat):
    pass

Bengal_cat = Bengal("Pedro")
Chartreux_cat = Chartreux("Alex")
Siamese_cat = Siamese("Caramelo")
all_cats = [Bengal_cat, Chartreux_cat, Siamese_cat]
sara_pets = Pets(all_cats)
sara_pets.walk()

#Exercise 2: Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name =  name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name}"
    def run_speed(self):
       # run_speed = 
        return self.weight / self.age * 10 #run_speed
    
    def fight(self, other_dog):
        strenght2 = other_dog.run_speed() * other_dog.weight
        strenght1= self.run_speed() * self.weight
        if strenght1 > strenght2:
            return f"{self.name} wins the fight."
        elif strenght2 > strenght1:
            return f"{other_dog.name} wins the fight."
        else :
            return f"It's a tie"
    
dog1 = Dog('Pop', 3, 50)            
dog2 = Dog('Jerimy', 5, 60)
dog3 = Dog('Lolo', 2, 30)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())
print(dog1.run_speed())
print(dog1.fight(dog3))


#Exercise 3: Dogs Domesticated
import random
class PetDog(Dog):
    
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        print(self.bark())
    
    def play(self, *args):
        dogs = [dog.name for dog in args ]
        string = ", ".join(dogs)
        print(f'{string} all play together') 
    
    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained:
            trick = random.choice(tricks)
            print(f'{self.name} {trick}')

my_dog = PetDog("Pop", 4, 30)
my_dog.train()
dog1 = PetDog("Buddy", 3, 20)
dog2 = PetDog("Max", 5, 25)
my_dog.play(dog1, dog2)
my_dog.do_a_trick()

#Exercise 4: Family and Person Classes
class Person:
    
    def __init__(self, first_name, age, last_name = ""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
        self.members = []

    def is_18(self):
        return self.age >= 18 

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)

    def check_majority(self,first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print('You are over 18, your parents Jane and John accept that you will go out with your friends')
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                    return 
                print('No family member found with that name')
    def family_presentation(self):
        print(f'familys last name is : {self.last_name}' )
        for i in self.members:
            print(f' {i.first_name}, age is {i.age} years old')

family1 = Family('Robenson')
family1.born("Luca", 1)
family1.born("Maya", 19)

family1.family_presentation()
family1.check_majority("Luca")
family1.check_majority("Maya")


            
