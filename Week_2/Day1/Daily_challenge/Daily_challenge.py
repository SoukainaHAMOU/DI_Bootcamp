#Daily challenge Old MacDonald’s Farm
class Farm :
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}
    
    # def add_animal(self, animal_type, count = 1):
    #     if animal_type in self.animals:
    #         self.animals[animal_type] += count
    #     else:
    #         self.animals[animal_type] = count 
    def add_animal(self, **kwargs):
        for animal, count in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += count
            else:
                self.animals[animal] = count

    def get_info(self):
        printed = f"{self.farm_name}'s farm \n"
        for animal, count in self.animals.items():
            printed += f'{animal} : {count}\n'
        printed += 'E-I-E-I-0!'
        return printed
        #print('E-I-E-I-0!')
        
    def get_animal_types(self):
        sorted_list = sorted(self.animals.keys())
        return sorted_list
    
    def get_short_info(self):
        animal_list = self.get_animal_types()
        animal_phrases = []
        for animal in animal_list:
            name = animal + "s" if self.animals[animal] > 1 else animal
            animal_phrases.append(name)
        if len(animal_phrases) == 1:
            animals_str = animal_phrases[0]
        else:
            animals_str = ", ".join(animal_phrases[:-1]) + " and " + animal_phrases[-1]

        return f"{self.farm_name}'s farm has {animals_str}."
        
macdonald = Farm("McDonald")

macdonald = Farm("McDonald's")
macdonald.add_animal(cow=5, sheep=2, goat=12)

print(macdonald.animals)
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
print(macdonald.get_info())
macdonald.get_animal_types()



    