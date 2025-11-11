#Exercise 1: Cats

class Cat :
    #cats = []

    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

        
def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = cat1
    if cat2.age > oldest_cat.age :
        oldest_cat = cat2
            #print(f"{cat2.name} is the oldest and is {cat1.age} years old.")
    if cat3.age > oldest_cat.age :
            #print(f"{cat2.name} is the oldest and is {cat2.age} years old.")
        oldest_cat = cat3
    return oldest_cat


cat1 = Cat("Caramello", 3)
cat2 = Cat("Bella", 5)
cat3 = Cat("Alex", 2)

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"{oldest_cat.name} is the oldest and is {oldest_cat.age} years old.")

#Exercise 2 : Dogs
class Dog :
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self) :

        print(f"{self.name}  goes woof!")
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")
    def __str__(self):
        return f" Dog_name = {self.name}, height = {self.height}"
davids_dog = Dog("Henry", 15)
sarahs_dog = Dog('Pedro', 24)

davids_dog.bark()
davids_dog.jump()
def compare_size(dog1, dog2):
    biggest = dog1
    if biggest.height < dog2.height:
        biggest = dog2
    return biggest

biggest_dog = compare_size(davids_dog, sarahs_dog)
print(f"{biggest_dog.name} is the biggest")

#Exercise 3 : Who’s the song producer?
class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        lyrics_final = ""
        for lyric in self.lyrics :            
            lyrics_final = lyrics_final + ' ' + lyric 
        print(lyrics_final)
    
stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()

#Exercise 4 : Afternoon at the Zoo
# class Zoo():
#     def __init__(self, zoo_name):
#         self.zoo_name = zoo_name
#         self.animals = []

#     def add_animal(self,new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)
        
    
#     def get_animals(self):
#         print("Animals in the zoo:")
#         for animal in self.animals:
#             print(animal)
    
#     def sell_animal(self,animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
    
    
#     def sort_animals(self):
#         dictionary_animals = {}
#         sorted_animals = sorted(self.animals)
#         for animal in sorted_animals:
#             first_letter = animal[0].upper()
#             if first_letter not in dictionary_animals:
#                 dictionary_animals[first_letter] = []
#             dictionary_animals[first_letter].append(animal)
                        
#         return dictionary_animals
    
#     def get_groups(self) :
#         group = self.sort_animals()
#         for key, value in group.items():
#             print(f"{key} : {value}")
            
# brooklyn_safari = Zoo("Brooklyn Safari")

# brooklyn_safari.add_animal("Giraffe")
# brooklyn_safari.add_animal("Bear")
# brooklyn_safari.add_animal("Baboon")

# brooklyn_safari.get_animals()
# #brooklyn_safari.sell_animal("Bear")
# brooklyn_safari.get_animals()
# brooklyn_safari.sort_animals()
# brooklyn_safari.get_groups()        
