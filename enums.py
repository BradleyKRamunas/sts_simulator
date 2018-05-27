from enum import Enum


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


class CardType(Enum):
    ATTACK = 1
    SKILL = 2
    POWER = 3
    STATUS = 4


class StateType(Enum):

    # Combats
    NORMAL_COMBAT = 1
    HAND_TO_EXHAUST = 2
    HAND_TO_DRAW = 3
    DISCARD_TO_DRAW = 4
    EXHAUST_TO_HAND = 5
    COPY = 6
    UPGRADE = 7

    # Rest_sites
    NORMAL_REST = 8
    UPGRADE_REST = 9

    # Random_events
    NORMAL_RANDOM = 10
    REMOVE_CARD = 11
    ADD_CARD = 12
