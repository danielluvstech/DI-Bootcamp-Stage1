# Exercise 1: Cats

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# def find_oldest_cat(cats):
#     return max(cats, key=lambda cat: cat.age)

# # Instantiate three Cat objects
# first_cat = Cat("Fluffy", 2)
# second_cat = Cat("Mitzy", 6)
# third_cat = Cat("Sneakers", 4)

# oldest_cat = find_oldest_cat([first_cat, second_cat, third_cat])

# print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")

# Exercise 2: Dogs

# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")

# # Create instances outside the class
# davids_dog = Dog("Rex", 50)
# print(f"David's dog is called {davids_dog.name} and is {davids_dog.height} cm tall.")
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(f"Sarah's dog is called {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
# sarahs_dog.bark()
# sarahs_dog.jump()

# # The bigger dog
# if davids_dog.height > sarahs_dog.height:
#     print(f"The bigger dog is {davids_dog.name}.")
# else:
#     print(f"The bigger dog is {sarahs_dog.name}.")

#  Exercise 3 : Who’s the song producer?
    
# class Song:

#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)   

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])     

# stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo

# class Zoo:

#     def __init__(self, zoo_name):
#         self.name = zoo_name
#         self.animals = []

#     def add_animal(self, new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)

#     def get_animals(self):
#         print("All of the animals in the zoo:")
#         for animal in self.animals:
#             print(animal)

#     def sell_animal(self, animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold) 

#     def sort_animals(self):
#         sorted_animals = sorted(self.animals)   
#         group_animals = {}

#         for animal in sorted_animals:
#             first_letter = animal[0].upper()
#             if first_letter not in group_animals:
#                 group_animals[first_letter] = []
#             group_animals[first_letter].append(animal)
        
#         return group_animals

#     def get_groups(self):
#         group_animals = self.sort_animals()
#         for letter, group in group_animals.items():
#             print(f"{letter}: {group}")

# new_york_zoo = Zoo("New York Zoo")

# # Add animals
# new_york_zoo.add_animal("Lion")
# new_york_zoo.add_animal("Baboon")
# new_york_zoo.add_animal("Bear")
# new_york_zoo.add_animal("Cougar")
# new_york_zoo.add_animal("Cat")
# new_york_zoo.add_animal("Emu")
# new_york_zoo.add_animal("Eel")
# new_york_zoo.add_animal("Ape")

# # Get animals
# new_york_zoo.get_animals()

# # Sell animal
# new_york_zoo.sell_animal("Lion")

# # Get new(updated) list on animals
# new_york_zoo.get_animals()

# # Sorted groups
# new_york_zoo.get_groups()

