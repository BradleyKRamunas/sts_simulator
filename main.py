from enum import Enum
import random

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

    ##NON-STATUS CARD EFFECTS##
    DEFEND = 99 # Gain armor equivalent to n
    DRAW = 100 #

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
        for condit in self.conditions:
            if condition.status == condit.status:
                condit.value += condition.value
                return
        self.conditions.append(condition)

    def decrement_status_conditions(self):
        conditions_to_remove = []
        for condition in self.conditions:
            if not condition.static:
                condition.value -= 1
            if condition.value == 0:
                conditions_to_remove.append(condition)
        for condition in conditions_to_remove:
            self.conditions.remove(condition)

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

class CombatDeck:
    def __init__(self, deck):
        self.draw_pile = random.shuffle(deck)
        self.hand = []
        self.discard_pile = []
        self.exhaust_pile = []

    def draw_card(self):
        if len(hand) < 12:
            if len(self.draw_pile) == 0:
                if len(self.discard_pile) != 0:
                    self.draw_pile = random.shuffle(self.discard_pile)
                    self.discard_pile = []
            hand.append(self.draw_pile.pop())

    def discard_hand(self):
        discard_pile.extend(self.hand)
        self.hand = []

    def use_card(self, card, target):
        self.hand.remove(card)
        card.apply(target)
        if card.exhaust:
            self.exhaust_pile.append(card)
        else:
            self.discard_pile.append(card)




class Card:
    def __init__(self, cost, status_condition, target_type, exhaust):
        self.cost = cost
        self.status_condition = status_condition
        self.target_type = target_type
        self.exhaust = exhaust

    def apply(self, target):
        if self.target_type == TARGET.SELF:

        elif self.target_type == TARGET.SINGLE:

        elif self.target_type == TARGET.ALL:

        elif self.target_type == TARGET.RANDOM:



def generate_default_deck():
    deck = Deck()
    bash = deck.add_card(Card(2, StatusCondition(Status.VULNERABLE, 2, False), Target.SINGLE, False))
    strike = Card(1, None, Target.SINGLE, False)
    for i in range(5): deck.add_card(strike)
    defend = Card(1, StatusCondition(Status.DEFEND, 1, False), Target.SELF, False)
    for i in range(4) : deck.add_card(defend)
    return deck
