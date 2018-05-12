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


strike = Card("Strike", 1, CardType.ATTACK, strike_fx, Target.SINGLE, False)
defend = Card("Defend", 1, CardType.SKILL, defend_fx, Target.SELF, False)
bash = Card("Bash", 2, CardType.ATTACK, bash_fx, Target.SINGLE, False)
anger = Card("Anger", 1, CardType.ATTACK, anger_fx, Target.SINGLE, False)
