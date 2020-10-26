class Character():
    name = "Link"
    sex = "Male"
    max_hit_points = 50
    current_hit_points = 50
    max_speed = 10

def display_character(my_character):
    print(my_character.name, my_character.sex, my_character.max_hit_points, my_character.current_hit_points)

my_dude = Character()

my_dude.name = "Bob"
my_dude.sex = "Male" 
my_dude.max_hit_points = 60

display_character(my_dude)



class Person:
    name = ""
    money = 0 

def display_person(my_person):
    print("His name is", my_person.name, "and he has",my_person.money, "in his wallet")
bob = Person()
bob.name = "BOB"
bob.money = 1000 

display_person(bob)


class Boat():
    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.is_docked = True
 
    def dock(self):
        if self.is_docked:
            print("You are already docked.")
        else:
            self.is_docked = True
            print("Docking")
 
    def undock(self):
        if not self.is_docked:
            print("You aren't docked.")
        else:
            self.is_docked = False
            print("Undocking")


b = Boat()
 
b.dock()
b.undock()
b.undock()
b.dock()
b.dock()



