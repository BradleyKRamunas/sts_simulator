from enum import Enum

import random
import math


class GoblinAI:
    def __init__(self):
        self.sequence = [Intent.ATTACK]
        self.attack = 6
        self.block = 0
        self.buff = 0
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        return (move, self.attack, None)

class SpikeSlimeAI:
    def __init__(self):
        self.sequence = [Intent.DEBUFF, Intent.DEBUFF, Intent.ATTACK, Intent.ATTACK]
        self.attack = 8
        self.block = 0
        self.buff = 0
        self.debuff = 1

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.DEBUFF:
            return (move, self.debuff, Status.FRAIL)
        else:
            return (move, self.attack, None)

class AcidSlimeAI:
    def __init__(self):
        self.sequence = [Intent.DEBUFF, Intent.ATTACK]
        self.attack = 3
        self.block = 0
        self.buff = 0
        self.debuff = 1

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.DEBUFF:
            return (move, self.debuff, Status.WEAK)
        else:
            return (move, self.attack, None)

class JawWormAI:
    def __init__(self):
        self.sequence = [Intent.ATTACK, Intent.BLOCK, Intent.BUFF]
        self.attack = 11
        self.block = 6
        self.buff = 3
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BUFF:
            return (move, self.buff, Status.STRENGTH)
        elif move == Intent.BLOCK:
            return (move, self.block, None)
        else:
            return (move, self.attack, None)

class ExplosiveGoblinAI:
    def __init__(self):
        self.sequence = [Intent.BLOCK, Intent.BLOCK, Intent.BLOCK, Intent.ATTACK]
        self.attack = 30
        self.block = 5
        self.buff = 0
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BLOCK:
            return (move, self.block, None)
        else:
            return (move, self.attack, None)

class FungiBeastAI:
    def __init__(self):
        self.sequence = [Intent.BUFF, Intent.ATTACK, Intent.ATTACK]
        self.attack = 6
        self.block = 0
        self.buff = 3
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BUFF:
            return (move, self.buff, Status.STRENGTH)
        else:
            return (move, self.attack, None)

class SlaverAI:
    def __init__(self):
        self.sequence = [Intent.ATTACK]
        self.attack = 12
        self.block = 0
        self.buff = 0
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        return (move, self.attack, None)


class LagavulinAI:
    def __init__(self):
        self.sequence = [Intent.BLOCK, Intent.BLOCK, Intent.ATTACK, Intent.ATTACK, Intent.ATTACK, Intent.DEBUFF]
        self.attack = 18
        self.block = 12
        self.buff = 0
        self.debuff = 3

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BLOCK:
            return (move, self.block, None)
        elif move == Intent.ATTACK:
            return (move, self.attack, None)
        else:
            return (move, self.debuff, Status.WEAK)

class Intent(Enum):
    ATTACK = 1
    BLOCK = 2
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

    def __str__(self):
        return "{} with value {} for duration {} (static: {})"\
            .format(self.status.name, self.value, self.duration, self.static)

    def __repr__(self):
        return "{} with value {} for duration {} (static: {})" \
            .format(self.status, self.value, self.duration, self.static)


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

class Combat:
    def __init__(self, player, enemies):
        self.player = CombatPlayer(player, self)
        self.enemies = enemies
        for enemy in self.enemies:
            enemy.combat = self
        self.game_loop()  # meant for human player, not for AI usage

    def start_turn(self):
        for enemy in self.enemies:
            if enemy.health != 0:
                enemy.generate_move()
            else:
                enemy.intent = None

        self.player.reset_energy()
        self.player.reset_block()
        draw_size = 5
        if Status.DRAW_REDUCTION in self.player.conditions:
            value = self.player.conditions[Status.DRAW_REDUCTION].value
            draw_size -= value
        if Status.BERSERK in self.player.conditions:
            value = self.player.conditions[Status.BERSERK].value
            if self.player.health <= int(math.floor(0.5 * self.player.max_health)):
                self.player.gain_energy(value)
        if Status.BRUTALITY in self.player.conditions:
            value = self.player.conditions[Status.BRUTALITY].value
            self.player.lose_health(value)
            if self.player.health == 0:
                return  # premature stop condition, no need to continue
            self.player.draw_cards(value)
        if Status.DEMON in self.player.conditions:
            value = self.player.conditions[Status.DEMON].value
            status = StatusCondition(Status.STRENGTH, value, 0, True)
            self.player.apply_status_condition(status)

        self.player.draw_cards(draw_size)

    def end_turn(self):
        for enemy in self.enemies:
            enemy.decrement_status_conditions()

        dead_enemies = 0
        for enemy in self.enemies:
            if enemy.health == 0:
                dead_enemies += 1
        if dead_enemies == len(self.enemies):
            return  # premature stop condition to ensure that we do not lose health

        for enemy in self.enemies:
            enemy.apply_intent()

        if self.player.health == 0:
            return  # premature stop condition, no need to continue

        self.player.discard_hand()
        if Status.FLEX in self.player.conditions:
            value = self.player.conditions[Status.FLEX].value
            status = StatusCondition(Status.STRENGTH, -value, 0, True)
            self.player.apply_status_condition(status)
        if Status.COMBUST in self.player.conditions:
            value = self.player.conditions[Status.COMBUST].value
            self.player.lose_health(value)
            for enemy in self.enemies:
                enemy.take_damage(5 * value)
        if Status.METALLICIZE in self.player.conditions:
            value = self.player.conditions[Status.METALLICIZE].value
            self.player.block += value  # note that dexterity does not affect this

        self.player.decrement_status_conditions()

    def print_information(self):
        print ("Your health: {}/{} | Your Energy: {} | Your Block: {}"\
            .format(self.player.health, self.player.max_health, self.player.energy, self.player.block))
        count = 0
        for card in self.player.deck.hand:
            print ("{}: {} |".format(count, card.name)),
            count += 1
        else:
            print
        count = 0
        for enemy in self.enemies:
            if enemy.health != 0:
                intent, value = enemy.intent
                print (enemy.conditions)
                print ("Enemy {} with health {}/{} is".format(count, enemy.health, enemy.max_health)),
                if intent == Intent.ATTACK:
                    print ("Attacking for {} | ".format(value)),
                if intent == Intent.DEFEND:
                    print ("Defending for {} | ".format(value)),
                if intent == Intent.BUFF:
                    print ("Buffing | "),
                if intent == Intent.DEBUFF:
                    print ("Debuffing | "),
            count += 1
        else:
            print

    def game_loop(self):
        while True:
            self.start_turn()
            while True:
                self.print_information()
                option = int(raw_input("Which card would you like to use (-1 to end turn)? > "))
                if option == -1:  # -1 means end turn
                    break
                card = self.player.deck.hand[option]
                option = int(raw_input("Target (-1 for self)? > "))

                self.player.deck.use_card(card, option)

                if self.player.health == 0:
                    return -1  # return -1 indicates that you have lost
                dead_enemies = 0
                for enemy in self.enemies:
                    if enemy.health == 0:
                        dead_enemies += 1
                if dead_enemies == len(self.enemies):
                    return 1  # return 1 indicates that you have won
            print ("---END OF TURN---")
            self.end_turn()

class CombatEnemy:
    def __init__(self, combat, ai, health):
        self.combat = combat
        self.ai = ai  # function that will generate moves
        self.health = health
        self.max_health = health
        self.block = 0
        self.intent = None  # defined as a tuple of (intent, value, status)
        self.conditions = {}
        # TODO: create some AI class and extend it with some forms of enemies

    def apply_intent(self):
        # TODO: finish this for all types of intents
        intent, value = self.intent
        if intent == Intent.ATTACK:
            self.combat.player.take_damage(value)

    def generate_move(self):
        self.intent = self.ai.generate_move()

    def take_damage(self, value):
        calc_value = value
        if Status.VULNERABLE in self.conditions:
            calc_value = int(math.floor(1.5 * calc_value))
        if self.block - calc_value >= 0:
            self.block -= calc_value
        else:
            calc_value = calc_value - self.block
            self.block = 0
            self.health -= calc_value
        if self.health < 0:
            self.health = 0

    def apply_status_condition(self, condition):
        if condition.status in self.conditions:
            self.conditions[condition.status].value += condition.value
            self.conditions[condition.status].duration += condition.duration
        else:
            self.conditions[condition.status] = condition
        status = self.conditions[condition.status]
        if not status.static and status.duration <= 0:
            del self.conditions[condition.status]
        if status.static and status.value == 0:
            del self.conditions[condition.status]

    def decrement_status_conditions(self):
        conditions_to_remove = []
        for key, value in self.conditions.items():
            if not value.static:
                value.duration -= 1
                if value.duration == 0:
                    conditions_to_remove.append(key)
        for condition in conditions_to_remove:
            del self.conditions[condition]


class CombatPlayer:
    def __init__(self, player, combat):
        self.combat = combat
        self.conditions = {}  # a dictionary of Status, StatusCondition
        self.deck = CombatDeck(player.deck, combat)
        self.health = player.health
        self.max_health = player.max_health
        self.energy = 10
        self.block = 0
        self.damage_track = 0  # used for keeping track of damage taken for Blood For Blood

    def generate_damage(self, value):
        calc_value = value
        if Status.STRENGTH in self.conditions:
            calc_value += self.conditions[Status.STRENGTH].value
        if Status.WEAK in self.conditions:
            calc_value = int(math.floor(0.75 * calc_value))
        return calc_value

    def take_damage(self, value):
        self.damage_track += 1
        calc_value = value
        if Status.VULNERABLE in self.conditions:
            calc_value = int(math.floor(1.5 * calc_value))
        if self.block - calc_value >= 0:
            self.block -= calc_value
        else:
            calc_value -= self.block
            self.block = 0
            self.health -= calc_value
        if self.health < 0:
            self.health = 0

    def lose_health(self, value):
        self.damage_track += 1
        if Status.RUPTURE in self.conditions:
            value = self.conditions[Status.RUPTURE].value
            strength = StatusCondition(Status.STRENGTH, value, 0, True)
            self.apply_status_condition(strength)
        self.health -= value
        if self.health < 0:
            self.health = 0

    def heal_health(self, value):
        self.health += value
        self.health = min(self.max_health, self.health)

    def gain_block(self, value):
        calc_value = value
        if Status.DEXTERITY in self.conditions:
            calc_value += self.conditions[Status.DEXTERITY].value
        if Status.FRAIL in self.conditions:
            calc_value = int(math.floor(0.75 * calc_value))
        self.block += calc_value

    def draw_cards(self, number):
        for i in range(number):
            self.deck.draw_card()

    def discard_hand(self):
        self.deck.discard_hand()

    def reset_energy(self):
        self.energy = 10

    def reset_block(self):
        if Status.BARRICADE not in self.conditions:
            self.block = 0

    def gain_energy(self, value):
        self.energy += value

    def apply_status_condition(self, condition):
        if condition.status in self.conditions:
            self.conditions[condition.status].value += condition.value
            self.conditions[condition.status].duration += condition.duration
        else:
            self.conditions[condition.status] = condition
        status = self.conditions[condition.status]
        if not status.static and status.duration <= 0:
            del self.conditions[condition.status]
        if status.static and status.value == 0:
            del self.conditions[condition.status]

    def decrement_status_conditions(self):
        conditions_to_remove = []
        for key, value in self.conditions.items():
            if not value.static:
                value.duration -= 1
                if value.duration == 0:
                    conditions_to_remove.append(key)
        for condition in conditions_to_remove:
            del self.conditions[condition]


class CombatDeck:
    def __init__(self, deck, combat):
        self.combat = combat
        self.draw_pile = deck.cards
        random.shuffle(self.draw_pile)
        self.hand = []
        self.discard_pile = []
        self.exhaust_pile = []

    def draw_card(self):
        if len(self.hand) < 12:
            if len(self.draw_pile) == 0:
                if len(self.discard_pile) != 0:
                    self.draw_pile = list(self.discard_pile)
                    random.shuffle(self.draw_pile)
                    self.discard_pile = []
            card = self.draw_pile.pop()
            if card.card_type == CardType.STATUS and Status.EVOLVE in self.combat.player.conditions:
                value = self.combat.player.conditions[Status.EVOLVE].value
                for i in range(value):
                    self.draw_card()
            self.hand.append(card)

    def discard_hand(self):
        self.discard_pile.extend(self.hand)
        self.hand = []

    def exhaust_card(self, card):
        self.exhaust_pile.append(card)
        if Status.FEELNOPAIN in self.combat.player.conditions:
            value = self.combat.player.conditions[Status.FEELNOPAIN].value
            self.combat.player.block += value
        if Status.EMBRACE in self.combat.player.conditions:
            value = self.combat.player.conditions[Status.EMBRACE].value
            self.combat.player.draw_cards(value)

    def use_card(self, card, target):
        # TODO: implement checks for card target types and apply appropriately
        if card.name == "Clash":
            for card_in_hand in self.hand:
                if card_in_hand.card_type != CardType.ATTACK:
                    return
        if Status.RAGE in self.combat.player.conditions:
            value = self.combat.player.conditions[Status.RAGE].value
            self.combat.player.block += value  # note that dexterity is not accounted for
        if card.name == "Blood for Blood":
            card.cost = max(0, 4 - self.damage_track)
        if card.cost <= self.combat.player.energy:
            self.combat.player.energy -= card.cost
            self.hand.remove(card)
            card.apply(self.combat, target)
            if card.exhaust:
                self.exhaust_card(card)
            else:
                self.discard_pile.append(card)




# TODO:
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
XII. Conditions"""

