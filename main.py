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

    DEFEND = 99 # Not a real status; used for defence cards

class StatusCondition:
    def __init__(self, status, value, static):
        self.status = status # type Status
        self.value = 0 # determines either how many turns a debuff will exist, or initial value
        self.static = static # true if value will never change, false is value decrements/changes per turn

class Player:
    def __init__(self, deck, health):
        self.conditions = []
        self.deck = deck
        self.health = health

    def apply_status_condition(self, condition):
        #TODO: Check if condition already exists; if it does, add to currently exisiting condition

class Enemy:
    def __init__(self, health):
        self.conditions = []
        self.health = health

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

class Card:
    def __init__(self, cost, status_condition, target_type, exhaust):
        self.cost = cost
        self.status_condition = status_condition
        self.target_type = target_type
        self.exhaust = exhaust

def generate_default_deck():
    deck = Deck()
    bash = deck.add_card(Card(2, StatusCondition(Status.VULNERABLE, 2, False), Target.SINGLE, False))
    strike = Card(1, None, Target.SINGLE, False)
    for i in range(5): deck.add_card(strike)
    defend = Card(1, StatusCondition(Status.DEFEND, 1, False), Target.SELF, False)
    for i in range(4) : deck.add_card(defend)
    
    return deck
