class Player:
    def __init__(self, deck, health, energy = 3):
        self.deck = deck
        self.health = health
        self.max_health = health
        self.max_energy = 3


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)


class Card:
    def __init__(self, name, cost, card_type, fx, target_type, exhaust):
        self.name = name
        self.cost = cost  # cost of the card in order to use (-1 is X, -2 is X+1...)
        self.card_type = card_type  # of type Card_Type
        self.fx = fx  # function that takes in (combat, target) and does something
        self.target_type = target_type  # of type Target
        self.exhaust = exhaust  # boolean indicating whether the card exhausts
        self.count = 0

    def apply(self, combat, target):
        self.fx(combat, target, self.count)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.card_type == other.card_type and self.count == other.count