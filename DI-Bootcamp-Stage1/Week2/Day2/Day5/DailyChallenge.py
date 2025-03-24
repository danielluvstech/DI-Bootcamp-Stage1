# Daily challenge: Old MacDonald’s Farm

class Farm:

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        self.animals[animal] = self.animals.get(animal, 0) + count

    def get_info(self):
        print(f"{self.name}'s farm\n")
        for animal, count in self.animals.items():
            print(f"{animal} : {count}")
        print("\n   E-I-E-I-O!")

# Expanding the farm        

    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        plural_animals = [animal + "s" if self.animals[animal] > 1 else animal for animal in animal_types]
        return f"{self.name}'s farm has {', '.join(plural_animals[:-1])} and {plural_animals[-1]}." if len(plural_animals) > 1 else f"{self.name}'s farm has {plural_animals[0]}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
print(macdonald.get_animal_types())
print(macdonald.get_short_info())


