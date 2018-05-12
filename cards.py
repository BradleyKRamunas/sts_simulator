from main import Card
from main import StatusCondition
from main import Status
from main import CardType
from main import Target
from main import Deck

def generate_default_deck():
    deck = Deck()
    deck.add_card(bash)
    for i in range(5):
        deck.add_card(strike)
    for i in range(4):
        deck.add_card(defend)
    return deck

def strike_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(6))


def defend_fx(combat, target):
    player = combat.player
    player.gain_block(5)


def bash_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(8))
    condition = StatusCondition(Status.VULNERABLE, 0, 2, False)
    enemy.apply_status_condition(condition)


def anger_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(5))
    player = combat.player
    player.deck.discard_pile.append(anger)

def armaments_fx(combat, target):
    # TODO: ask player which card they want to upgrade
    player = combat.player
    player.gain_block(5)

def bodyslam_fx(combat, target):
    block = combat.player.block
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(block))

# TODO: Can only be used if all cards in the player's hand are attack cards
def clash_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(14))

# Clothesline: deals 12(14) damage and applies 2(3) weak.
def clothesline_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))
    vulnerable = StatusCondition(Status.VULNERABLE, 2, False)
    enemy.apply_status_condition(vulnerable)

# Flex: gain 2(4) strength at the beginning of turn, then lose 2(4) at the end of turn.
def flex_fx(combat, target):
    player = combat.player
    flex = StatusCondition(Stats.FLEX, 2, False)
    player.apply_status_condition(flex)

# <<<<<<< HEAD
strike = Card("Strike", 1, CardType.ATTACK, strike_fx, Target.SINGLE, False)
defend = Card("Defend", 1, CardType.SKILL, defend_fx, Target.SELF, False)
bash = Card("Bash", 2, CardType.ATTACK, bash_fx, Target.SINGLE, False)
anger = Card("Anger", 1, CardType.ATTACK, anger_fx, Target.SINGLE, False)
armaments = Card("Armaments", 1, CardType.SKILL, armaments_fx, Target.SELF, False)
bodyslam = Card("Body Slam", 1, CardType.ATTACK, bodyslam_fx, Target.SINGLE, False)
clash = Card("Clash", 0, CardType.ATTACK, clash_fx, Target.SINGLE, False)
clothesline = Card("Clothesline", 2, CardType.ATTACK, clothesline_fx, Target.SINGLE, False)
flex = Card("Flex", 0, CardType.SKILL, flex_fx, Target.SELF, False)
# =======
# >>>>>>> b048d96c58fdacaa4b154b626b5cb9008c106daf
# Not sure what this is...
