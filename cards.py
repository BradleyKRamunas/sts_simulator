import main

# TODO: increase damage by player's strength, apply weakness etc.


def strike_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(6)


def defend_fx(combat, target):
    player = combat.player
    player.gain_defence(5)


def bash_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(8)
    condition = main.StatusCondition(main.Status.VULNERABLE, 2, False)
    enemy.apply_status_condition(condition)


def anger_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(4)
    player = combat.player
    player.deck.discard_pile.append(anger)


strike = main.NewCard(1, main.CardType.ATTACK, strike_fx, main.Target.SINGLE, False)
defend = main.NewCard(1, main.CardType.SKILL, defend_fx, main.Target.SELF, False)
bash = main.NewCard(2, main.CardType.ATTACK, bash_fx, main.Target.SINGLE, False)
anger = main.NewCard(1, main.CardType.ATTACK, anger_fx, main.Target.SINGLE, False)
