import main

# TODO: increase damage by player's strength, apply weakness etc.


def strike_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(6))


def defend_fx(combat, target):
    player = combat.player
    player.gain_defence(5)


def bash_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(8))
    condition = main.StatusCondition(main.Status.VULNERABLE, 2, False)
    enemy.apply_status_condition(condition)


def anger_fx(combat, target):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(5))
    player = combat.player
    player.deck.discard_pile.append(anger)

def armaments_fx(combat, target):
    # TODO: ask player which card they want to upgrade

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
    vulnerable = main.StatusCondition(main.Stats.VULNERABLE, 2, False)
    enemy.apply_status_condition(vulnerable)

# Flex: gain 2(4) strength at the beginning of turn, then lose 2(4) at the end of turn.
def flex_fx(combat, target):
    player = combat.player
    flex = main.StatusCondition(main.Stats.FLEX, 2, False)
    player.apply_status_condition(flex)

strike = main.Card(1, main.CardType.ATTACK, strike_fx, main.Target.SINGLE, False)
defend = main.Card(1, main.CardType.SKILL, defend_fx, main.Target.SELF, False)
bash = main.Card(2, main.CardType.ATTACK, bash_fx, main.Target.SINGLE, False)
anger = main.Card(1, main.CardType.ATTACK, anger_fx, main.Target.SINGLE, False)
armaments = main.Card(1, main.CardType.SKILL, armaments_fx, main.Target.SELF, False)
bodyslam = main.Card(1, main.CardType.ATTACK, bodyslam_fx, main.Target.SINGLE, False)
clash = main.Card(0, main.CardType.ATTACK, clash_fx, main.Target.SINGLE, False)
clothesline = main.Card(2, main.CardType.ATTACK, clothesline_fx, main.Target.SINGLE, False)
flex = main.Card(0, main.CardType.SKILL, flex_fx, main.Target.SELF, False)
