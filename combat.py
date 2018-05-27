import random
import math
from enums import *


class StatusCondition:
    def __init__(self, status, value, duration, static):
        self.status = status  # type Status
        self.value = value  # determines value of debuff
        self.duration = duration  # determines duration of debuff
        self.static = static  # true if value will never change, false is value decrements/changes per turn

    def __str__(self):
        return "{} with value {} for duration {} (static: {})"\
            .format(self.status, self.value, self.duration, self.static)

    def __repr__(self):
        return "{} with value {} for duration {} (static: {})" \
            .format(self.status, self.value, self.duration, self.static)


class Combat:
    def __init__(self, player, enemies):
        self.player = CombatPlayer(player, self)
        self.enemies = enemies
        self.state_type = StateType.NORMAL_COMBAT
        for enemy in self.enemies:
            enemy.combat = self
        self.start_turn()
        #self.game_loop()  # meant for human player, not for AI usage

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
        print ("Your hand: "),
        for card in self.player.deck.hand:
            print ("{}: {} |".format(count, card.name)),
            count += 1
        else:
            print

        print ("Your conditions: "),
        print self.player.conditions
        count = 0
        for enemy in self.enemies:
            if enemy.health != 0:
                intent, value, other = enemy.intent

                print ("Enemy {} with health {}/{} is".format(count, enemy.health, enemy.max_health)),
                if intent == Intent.ATTACK:
                    print ("Attacking for {} | ".format(value)),
                if intent == Intent.BLOCK:
                    print ("Defending for {} | ".format(value)),
                if intent == Intent.BUFF:
                    print ("Buffing | "),
                if intent == Intent.DEBUFF:
                    print ("Debuffing | "),
                print ("Conditions: "),
                print (enemy.conditions)
            count += 1
        else:
            print

    def game_loop(self):
        while True:
            self.start_turn()
            while True:
                self.print_information()
                option = int(raw_input("Which card would you like to use (-1 end, -2 draw, -3 discard, -4 exhaust)? > "))
                if option == -1:  # -1 means end turn
                    break
                if option == -2:  # print draw pile
                    print ("Draw pile: "),
                    print self.player.deck.draw_pile
                    print
                    continue
                if option == -3:  # print discard pile
                    print ("Discard pile: "),
                    print self.player.deck.discard_pile
                    print
                    continue
                if option == -4:  # print exhaust pile
                    print ("Exhaust pile: "),
                    print self.player.deck.exhaust_pile
                    print
                    continue
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

    def apply_intent(self):
        if self.health == 0:
            return
        intent, value, status = self.intent
        if intent == Intent.ATTACK:
            self.combat.player.take_damage(self.generate_damage(value))
            if Status.FLAMEBARRIER in self.combat.player.conditions:
                value = self.combat.player.conditions[Status.FLAMEBARRIER].value
                self.lose_health(value)
        if intent == Intent.BLOCK:
            self.block += value
        if intent == Intent.BUFF:
            status_condition = StatusCondition(status, value, 0, True)
            self.apply_status_condition(status_condition)
        if intent == Intent.DEBUFF:
            status_condition = StatusCondition(status, 0, value+1, False)
            self.combat.player.apply_status_condition(status_condition)

    def generate_move(self):
        self.intent = self.ai.generate_move()

    def generate_damage(self, value):
        calc_value = value
        if Status.STRENGTH in self.conditions:
            calc_value += self.conditions[Status.STRENGTH].value
        if Status.WEAK in self.conditions:
            calc_value = int(math.floor(0.75 * calc_value))
        return calc_value

    def lose_health(self, value):
        self.health -= value
        self.health = max(0, self.health)

    def take_damage(self, value):
        if Status.THORNS in self.conditions:
            value = self.conditions[Status.THORNS].value
            self.combat.player.lose_health(value)
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
        self.energy = 3
        self.max_energy = player.max_energy
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
        if Status.JUGGERNAUT in self.conditions:
            value = self.conditions[Status.JUGGERNAUT].value
            random_target = random.randint(0, len(self.combat.enemies)-1)
            while self.combat.enemies[random_target].health <= 0:
                random_target = random.randint(0, len(self.combat.enemies) - 1)
            self.combat.enemies[random_target].lose_health(value)

    def draw_cards(self, number):
        for i in range(number):
            self.deck.draw_card()

    def discard_hand(self):
        self.deck.discard_hand()

    def reset_energy(self):
        self.energy = self.max_energy

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
        if Status.DOUBLE in self.conditions:
            del self.conditions[Status.DOUBLE]


class CombatDeck:
    def __init__(self, deck, combat):
        self.combat = combat
        self.draw_pile = deck.cards
        random.shuffle(self.draw_pile)
        self.hand = []
        self.discard_pile = []
        self.exhaust_pile = []

    def draw_card(self):
        if Status.NO_DRAW in self.combat.player.conditions:
            return
        if len(self.hand) < 12:
            if len(self.draw_pile) == 0:
                if len(self.discard_pile) != 0:
                    self.draw_pile = list(self.discard_pile)
                    random.shuffle(self.draw_pile)
                    self.discard_pile = []
                elif len(self.discard_pile) == 0:
                    return
            card = self.draw_pile.pop(0)
            if card.card_type == CardType.STATUS and Status.EVOLVE in self.combat.player.conditions:
                value = self.combat.player.conditions[Status.EVOLVE].value
                for i in range(value):
                    self.draw_card()
            self.hand.append(card)

    def discard_hand(self):
        cards_to_exhaust = []
        for card in self.hand:
            if "Burn" in card.name:
                self.combat.player.lose_health(2)
            if "Dazed" in card.name or "Carnage" in card.name or "Ghostly Armor" in card.name:
                cards_to_exhaust.append(card)
            else:
                self.discard_pile.append(card)
        for card in cards_to_exhaust:
            self.exhaust_card(card)
        self.hand = []

    def exhaust_card(self, card):
        self.hand.remove(card)
        self.exhaust_pile.append(card)
        if card.name == "Sentinel":
            self.combat.player.energy += 2
        if card.name == "Sentinel+":
            self.combat.player.energy += 3
        if Status.FEELNOPAIN in self.combat.player.conditions:
            value = self.combat.player.conditions[Status.FEELNOPAIN].value
            self.combat.player.block += value
        if Status.EMBRACE in self.combat.player.conditions:
            value = self.combat.player.conditions[Status.EMBRACE].value
            self.combat.player.draw_cards(value)

    def use_card(self, card, target):
        if card.card_type == CardType.STATUS:
            return False
        if "Clash" in card.name:
            for card_in_hand in self.hand:
                if card_in_hand.card_type != CardType.ATTACK:
                    return False
        if Status.RAGE in self.combat.player.conditions:
            value = self.combat.player.conditions[Status.RAGE].value
            self.combat.player.block += value  # note that dexterity is not accounted for
        if "Blood for Blood" in card.name:
            card.cost = max(0, 4 - self.combat.player.damage_track)
        if card.card_type == CardType.SKILL and Status.CORRUPTION in self.combat.player.conditions:
            card.cost = 0
            card.exhaust = True
        if card.cost <= self.combat.player.energy:
            self.combat.player.energy -= card.cost
            if card.exhaust:
                self.exhaust_card(card)
            else:
                if card.card_type == CardType.POWER:
                    self.hand.remove(card)
                else:
                    self.hand.remove(card)
                    self.discard_pile.append(card)
            if card.card_type == CardType.ATTACK and Status.DOUBLE in self.combat.player.conditions:
                card.apply(self.combat, target)
                remover = StatusCondition(Status.DOUBLE, 0, -1, False)
                self.combat.player.apply_status_condition(remover)
                card.count += 1
            card.apply(self.combat, target)
            if "Whirlwind" in card.name:
                self.combat.player.energy = 0
            card.count += 1
            return True
        else:
            return False


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

