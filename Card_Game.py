import random

# DEFINING GAME MECHANICS

def deal_dmg(attack, target):
    """
    Function used for dealing damage to a target.
    attack:  int, Value of the base attack
    target:  class instance, Target of the attack
    Modifies target's hp attribute based on its armor.
    """
    damage = attack - target.armor
    if damage < 0:
        damage = 0
    
    target.hp -= damage

def add_armor(armor, target):
    """
    Function used to add armor to target.
    armor:   int, Armor value to be added
    target:  class instance, Target of the addition
    """
    target.armor += armor

# DEFINING PLAYER

class Player:
    """
    Player class used for tracking user progress.
    hp:         int, Health Points
    mana:       int, Renewable resource spent to play cards
    armor:      int, Armor value
    hand_size:  int, Number of cards drawn each turn
    """
    def __init__(self, hand_size):
        self.hp = 10
        self.mana = 3
        self.armor = 0
        self.hand_size = hand_size

    def get_hp(self):
        return self.hp

    def get_mana(self):
        return self.mana

    def get_armor(self):
        return self.armor

    def get_hand_size(self):
        return self.hand_size

    def __str__(self):
        return "\n --- Player Status ---\n" + "Current health: " + str(self.get_hp()) + " | Current mana: " + str(self.get_mana())

# SETTING CARDS MECHANICS

class Card():
    """
    Card class used to create various cards to be used by the player.
    quantity:  int, Number of card copies to be added to player's deck
        Attributes defined in class instances:
    name:      str, Name of the card to be displayed on card front.
    mana_cost: int, Cost of playing the card in Mana.
    """
    def __init__(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return "This is a blank card."

class Magic_Bolt(Card):
    """
    Deals 5 damage to the opponent.
    """
    def __init__(self, quantity):
        self.quantity = quantity
        self.name = "Magic Bolt"
        self.mana_cost = 2

    def play(self, target):
        deal_dmg(5, target)
    
    def __str__(self):
        return "Deals 5 damage to the opponent."

class Arcane_Chainmail(Card):
    """
    Accumulates 2 Armor on caster.
    """
    def __init__(self, quantity):
        self.quantity = quantity
        self.name = "Arcane Chainmail"
        self.mana_cost = 2

    def play(self, target):
        add_armor(2, target)
    
    def __str__(self):
        return "Accumulates 2 Armor on caster."

# DEFINING ENEMIES

names_list = (
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
        self.hp = level * 12

    def get_hp(self):
        return self.hp

    def __str__(self):
        return "\n --- " + self.species + " ---\n" + "Current health: " + str(self.get_hp())



# DECK BUILDER

magic_bolts = Magic_Bolt(10)
arcane_chainmails = Arcane_Chainmail(10)

def update_deck():
    deck = []
    for number in range(magic_bolts.get_quantity()):
        deck.append("Magic Bolt")
    for number in range(arcane_chainmails.get_quantity()):
        deck.append("Arcane Chainmail")

    return deck

update_deck()



def deal_hand(hand_size, deck):
    hand = []

    for number in range(hand_size):
        hand.append(random.choice(deck))

    return hand



def read_hand(hand):
    print("\nYou've been dealt the following cards:")
    
    for card in hand:
        print(card)



def play_card(hand, deck):
    
    while True:
        card = input("Please type in name of the card to be played (or pass): ")

        if card in hand:
            hand -= card
            deck -= card
            if card == "Magic Bolt":
                card.play(monster)
            elif card == "Arcane Chainmail":
                card.play(player)



# TEST AREA

player = Player(3)
deck = update_deck()
hand = deal_hand(player.get_hand_size(), deck)
read_hand(hand)

monster = Enemy(1)

print(player)
print(monster)

play_card(hand, deck)
