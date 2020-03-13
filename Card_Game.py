# DEFINING PLAYER

class Player:
    """
    Player class used for tracking user progress.
    """
    def __init__(self):
        self.hp = 10
        self.mana = 3

    def get_hp(self):
        return self.hp

    def get_mana(self):
        return self.mana

    def __str__(self):
        return "Current health: " + str(get_hp(self)) + " | Current mana: " + str(get_mana(self))

player = Player()



# DEFINING ENEMIES

names = (
    "Bob",
    "Frank",
    "Dick",
    "Dave",
    "Rick",
    "Vito",
    "Chester",
    "Chad"
    )

species_list = (
    "Skeleton",
    "Minotaur",
    "Magician"
    )

class Enemy():
    """
    Enemy class used for encounters.
    """
    def __init__(self, level):
        self.level = level
        self.name = random.choice(names_list)
        self.species = random.choice(species_list)



# DEFINING CARDS

class Card():
    def __init__(self, mana_cost):
        self.mana_cost = mana_cost
