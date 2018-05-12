from enum import Enum
from collections import deque
import random
import cards
import math


class GoblinAI:
    def __init__(self):
        self.counter = 0
        self.sequence = deque([Intent.ATTACK])
        self.attack = 6
        self.defend = 0
        self.buff = 0
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.popleft()
        self.sequence.append(move)
        return (move, self.attack)


class Intent(Enum):
    ATTACK = 1
    DEFEND = 2
    BUFF = 3
    DEBUFF = 4


class Target(Enum):
    SELF = 1  # Card targets the user
    SINGLE = 2  # Card targets a single enemy
    ALL = 3  # Card targets all enemies
    RANDOM = 4  # Card targets a random enemy


class Status(Enum):
    POISON = 1  # Deal n damage, decrease to (n-1) for next turn
    WEAK = 2  # Deal 25% less damage
    VULNERABLE = 3  # Take 50% more damage
    FRAIL = 4  # Reduce armor gain by 25%
    DRAW_REDUCTION = 5  # Decrease card draw by n
    CONFUSED = 6  # Randomizes card costs
    STRENGTH = 7  # Increases damage by n
    DEXTERITY = 8  # Increases block gain by n
    ARTIFACT = 9  # Prevents n debuffs
    REGENERATION = 10  # Heal 4 hp per turn for 5 turns
    THORNS = 11  # Deal n damage to any attacker

    FLEX = 100  # Gain n strength immediately, lose n strength at the END of the turn
    NO_DRAW = 101  # Can no longer draw cards until the END of the turn
    COMBUST = 102  # Lose n HP at END of turn, 5n DAMAGE to ALL enemies
    CORRUPTION = 103  # Skills cost 0, all skills now exhaust
    EVOLVE = 104  # Drawing a status results in drawing n cards
    FEELNOPAIN = 105  # Whenever a card is exhausted, gain n Block
    FLAMEBARRIER = 106  # If you take damage this turn, deal n damage to attacker
    METALLICIZE = 107  # At the END of turn, gain n block
    RAGE = 108  # Playing an attack, gain n block
    RUPTURE = 109  # Lose HP from a CARD gain n strength
    BARRICADE = 110  # Block no longer expires at END of turn
    BERSERK = 111  # If HP <= 50%, gain n more energy each turn
    BRUTALITY = 112  # At START of turn lose n hp draw n cards
    EMBRACE = 113  # Whenever card is exhausted, draw n cards
    DEMON = 114  # At start of each turn, gain n strength
    DOUBLE = 115  # next n attacks are played twice
    JUGGERNAUT = 116  # gain block, deal n damage to random enemy


class StatusCondition:
    def __init__(self, status, value, duration, static):
        self.status = status  # type Status
        self.value = value  # determines value of debuff
        self.duration = duration  # determines duration of debuff
        self.static = static  # true if value will never change, false is value decrements/changes per turn


class Player:
    def __init__(self, deck, health):
        self.deck = deck
        self.health = health
        self.max_health = health


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)


class CardType(Enum):
    ATTACK = 1
    SKILL = 2
    POWER = 3
    STATUS = 4


class Card:
    def __init__(self, cost, card_type, fx, target_type, exhaust):
        self.cost = cost  # cost of the card in order to use (-1 is X, -2 is X+1...)
        self.card_type = card_type  # of type Card_Type
        self.fx = fx  # function that takes in (combat, target) and does something
        self.target_type = target_type  # of type Target
        self.exhaust = exhaust  # boolean indicating whether the card exhausts

    def apply(self, combat, target):
        self.fx(combat, target)


class Combat:
    def __init__(self, player, enemies):
        self.player = CombatPlayer(player, self)
        self.enemies = enemies
        self.game_loop()

    def game_loop(self):
        while True:
            # Main Combat Loop
            for enemy in self.enemies:
                enemy.generate_move()

            # Start-of-Turn Sequence
            self.player.reset_energy()
            draw_size = 5
            for condition in self.player.conditions:
                if condition.status == Status.DRAW_REDUCTION:
                    draw_size -= condition.value
                elif condition.status == Status.BERSERK:
                    if self.player.health <= math.floor(0.5 * self.player.max_health):
                        self.player.gain_energy(condition.value)
                elif condition.status == Status.BRUTALITY:
                    self.player.lose_health(condition.value)
                    self.player.draw_cards(condition.value)
                elif condition.status == Status.DEMON:
                    status = StatusCondition(Status.STRENGTH, condition.value, 0, True)
                    self.player.apply_status_condition(status)

            self.player.draw_cards(draw_size)
            while True:
                break
                # TODO: this while loop controls taking in input from user

                # TODO: check if enemies are dead
            # END OF USER INPUT #

            for enemy in self.enemies:
                enemy.decrement_status_condition()
            # TODO: allow enemies to attack player/apply debuffs/buff themselves
            # TODO: check if player has died

            # End-of-Turn Sequence
            # TODO: finish end-of-turn sequence
            self.player.discard_hand()
            for condition in self.player.conditions:
                if condition.status == Status.FLEX:
                    status = StatusCondition(Status.STRENGTH, -condition.value, 0, True)
                    self.player.apply_status_condition(status)

        # TODO: define end-of-combat sequence


class CombatEnemy:
    def __init__(self, ai, health):
        self.ai = ai  # function that will generate moves
        self.health = health
        self.max_health = health
        self.block = 0
        self.intent = None  # defined as a tuple of (intent, value)
        self.conditions = []
        # TODO: create some AI class and extend it with some forms of enemies

    def generate_move(self):
        self.intent = self.ai.generate_move()

    def take_damage(self, value):
        calc_value = value
        is_vulnerable = False
        for condition in self.conditions:
            if condition.status == Status.VULNERABLE:
                is_vulnerable = True
        if is_vulnerable:
            calc_value = math.floor(1.5 * calc_value)
        if self.block - calc_value >= 0:
            self.block -= calc_value
        else:
            calc_value = calc_value - self.block
            self.block = 0
            self.health -= calc_value

    # TODO: Organize into duration and value
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
                condition.duration -= 1
            if condition.duration == 0:
                conditions_to_remove.append(condition)
        for condition in conditions_to_remove:
            self.conditions.remove(condition)


class CombatPlayer:
    def __init__(self, player, combat):
        self.combat = combat
        self.conditions = []
        self.deck = CombatDeck(player.deck)
        self.health = player.health
        self.max_health = player.max_health
        self.energy = 3
        self.block = 0

    def generate_damage(self, value):
        calc_value = value
        is_weak = False
        for condition in self.conditions:
            if condition.status == Status.STRENGTH:
                calc_value += condition.value
            elif condition.status == Status.WEAK:
                is_weak = True
        if is_weak:
            calc_value = math.floor(0.75 * calc_value)
        return calc_value

    def take_damage(self, value):
        calc_value = value
        is_vulnerable = False
        for condition in self.conditions:
            if condition.status == Status.VULNERABLE:
                is_vulnerable = True
        if is_vulnerable:
            calc_value = math.floor(1.5 * calc_value)
        if self.block - calc_value >= 0:
            self.block -= calc_value
        else:
            calc_value -= self.block
            self.block = 0
            self.health -= calc_value

    def lose_health(self, value):
        # TODO: check for statuses that rely on losing health by CARD effect
        self.health -= value

    def heal_health(self, value):
        self.health += value

    def gain_block(self, value):
        calc_value = value
        is_frail = False
        for condition in self.conditions:
            if condition.status == Status.DEXTERITY:
                calc_value += condition.value
            elif condition.status == Status.FRAIL:
                is_frail = True
        if is_frail:
            calc_value = math.floor(0.75 * calc_value)
        self.block += calc_value

    def draw_cards(self, number):
        for i in range(number):
            self.deck.draw_card()

    def discard_hand(self):
        self.deck.discard_hand()

    def reset_energy(self):
        self.energy = 3

    def gain_energy(self, value):
        self.energy += value

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
                condition.duration -= 1
            if condition.duration == 0:
                conditions_to_remove.append(condition)
        for condition in conditions_to_remove:
            self.conditions.remove(condition)


class CombatDeck:
    def __init__(self, deck, combat):
        self.combat = combat
        self.draw_pile = random.shuffle(deck)
        self.hand = []
        self.discard_pile = []
        self.exhaust_pile = []

    def draw_card(self):
        if len(self.hand) < 12:
            if len(self.draw_pile) == 0:
                if len(self.discard_pile) != 0:
                    self.draw_pile = random.shuffle(self.discard_pile)
                    self.discard_pile = []
            self.hand.append(self.draw_pile.pop())

    def discard_hand(self):
        self.discard_pile.extend(self.hand)
        self.hand = []

    def use_card(self, card, target):
        self.hand.remove(card)
        card.apply(self.combat, target)
        if card.exhaust:
            self.exhaust_pile.append(card)
        else:
            self.discard_pile.append(card)


def generate_default_deck():
    deck = Deck()
    deck.add_card(cards.bash)
    for i in range(5):
        deck.add_card(cards.strike)
    for i in range(4):
        deck.add_card(cards.defend)
    return deck

# TODO:
# We need to give cards types (i.e. attack, skill, power, status)
# How should we define cards? (e.g. unplayable)
# Think about order of effect adding/defend
# For effects, add an effect timer

# Strike
# Defend
# Bash
# Anger

# Which cards do we want to implement?
# Armaments
# Body Slam
# Clash
# Clothesline
# Flex

""" TODO: Implement these cards """
# Havoc
# Headbutt
# Heavy Blade
# Iron Wave
# Perfected Strike
# Pommel Strike
# Shrug it off
# Thunderclap
# True Grit
# Twin Strike
# Warcry
# Wild Strike
# Battle Trance
# Blood for Blood
# Bloodletting
# Burning pact
# Carnage
# Combust
# Corruption
# Disarm
# Dropkick
# Dual Wield
# Entrench
# Evolve
# Feel No Pain
# Flame Barrier
# Ghostly Armor
# Hemokinesis
# Inflame
# Intimidate
# Metallicize
# Power Through
# Pummel
# Rage
# Rampage
# Reckless Charge
# Rupture
# Searing Blow
# Second Wind
# Seeing Red
# Sever Soul
# Shockwave
# Spot Weakness
# Uppercut
# Whirlwind - add special cost for X energy
# Barricade - block no longer expires
# Beserk
# Bludgeon
# Brutality
# Dark Embrace
# Demon Form - for all powers, add an unrecoverable pile
# Double Tap - literally everything happens twice
# Exhume
# Feed - no such thing as "minions"/"bosses" for us... for now
# Fiend fire
# Immolate
# Impervious
# Juggernaut
# Limit Break
# Offering
# Reaper

""" So what kind of thing are we doing here?
Strategy: Function approximation/Q-learning with features.
State - just wherever we are in the game. 
Features - 
I. Wakanda
II. Enemy health
III. Number of enemies
IV. Enemy types
V. Enemy intent/danger
VI. Presence of cards in hand (indicator list)
VII. Cards in discard
VIII. Cards in draw pile
IX. Energy remaining
X. Health remaining
XI. Block remaining
XII. Conditions

