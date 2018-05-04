from enum import Enum

class Target(Enum):
    SELF = 1 # Card targets the user
    SINGLE = 2 # Card targets a single enemy
    ALL = 3 # Card targets all enemies
    RANDOM = 4 # Card targets a random enemy

class Status(Enum):
    POISON = 1 # Deal n damage, decrease to (n-1) for next turn
    WEAK = 2 # Deal 25% less damage
    VULNERABLE = 3 # Take 50% more damage
    FRAIL = 4 # Reduce armor gain by 25%
    DRAW_REDUCTION = 5 # Decrease card draw by n
    CONFUSED = 6 # Randomizes card costs
    STRENGTH = 7 # Increases damage by 1
    DEXTERITY = 8 # Increases defence gain by 1
    ARTIFACT = 9 # Prevents debuff
    REGENERATION = 10 # Heal 4 hp per turn for 5 turns
    THORNS = 11 # Deal n damage to any attacker

class Player:
    def __init__(self, deck):
        self.statuses = []
        self.deck = deck


class Deck:
    def __init__(self):
        self.cards = []

class Card:
