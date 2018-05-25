from main import Card
from main import StatusCondition
from main import Status
from main import CardType
from main import Target
from main import Deck
import random


def generate_default_deck():
    deck = Deck()
    deck.add_card(bash)
    for i in range(5):
        deck.add_card(strike)
    for i in range(4):
        deck.add_card(defend)
    for i in range(3):
        deck.add_card(clash)
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
    flexing = StatusCondition(Status.FLEX, 2, False)
    strength = StatusCondition(Status.STRENGTH, 2, True)
    player.apply_status_condition(flexing)
    player.apply_status_condition(strength)


# Draws the top card on the draw pile, play, and exhaust it
def havoc_fx(combat, target):
    card = combat.player.deck.draw_pile.pop()
    tempCost = card.cost
    tempExhaust = card.exhaust
    card.cost = 0
    card.exhaust = True
    combat.player.deck.use_card(card)
    card.cost = tempCost
    card.exhaust = tempExhaust


def headbutt_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(9))
    addendum = player.deck.discard_pile.pop()
    player.deck.draw_pile.insert(0, addendum)


def heavy_blade_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    # Multiplies strength by 3, attacks, and divides by 3 again.
    if Status.STRENGTH in player.conditions:
        player.conditions[Status.STRENGTH] *= 3
    enemy.take_damage(player.generate_damage(14))
    if Status.STRENGTH in player.conditions:
        player.conditions[Status.STRENGTH] /= 3


def iron_wave_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(5)
    enemy.take_damage(player.generate_damage(5))


def perfected_strike_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    damage = 6
    for card in player.deck:
        if "strike" in card.name.lower():
            damage += 2
    enemy.take_damage(player.generate_damage(damage))


def pommel_strike_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(9))
    player.deck.draw_card()


def shrug_it_off_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(8)
    player.deck.draw_card()


def thunderclap_fx(combat, target):
    player = combat.player
    vulnerable = StatusCondition(Status.VULNERABLE, 1, True)
    for enemy in combat.enemies:
        enemy.take_damage(4)
        enemy.apply_status_condition(vulnerable)


# Gains 7 block; exhausts a random card
def true_grit_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(7)
    card = random.choice(player.deck.hand)
    player.deck.remove_card(card)
    player.deck.exhaust_pile.append(card)


def twin_strike_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(5))
    enemy.take_damage(player.generate_damage(5))


def warcry_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    player.deck.draw_card()
    option = raw_input("Which card to place on top of your draw pile? -> ")
    card = player.deck.hand[option]
    player.deck.hand.remove(card)
    player.deck.draw_pile.append(card)


def wild_strike_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))
    # TODO: Add a wound into player's combatdeck


def battle_trance_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    for i in range(3):
        player.deck.draw_card()
    # TODO: Cannot draw any more cards this turn


def blood_for_blood_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(18))


def bloodletting_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    player.health -= 3
    player.energy += 1
    # TODO: Update counter for number of times taken damage


def burning_pact_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    player.deck.draw_card()
    player.deck.draw_card()
    option = raw_input("Which card to exhaust? -> ")
    card = player.deck.hand[option]
    player.deck.remove_card(card)
    player.deck.exhaust_pile.append(card)


def carnage_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(20))


def combust_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    combustion = StatusCondition(Status.COMBUST, 1, False)
    player.apply_status_condition(combustion)


def corruption_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    corrupt = StatusCondition(Status.CORRUPTION, 2, False)
    player.apply_status_condition(corrupt)


def disarm_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    weak = StatusCondition(Status.STRENGTH, -2, False)
    enemy.apply_status_condition(weak)


def dropkick_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(5))
    if Status.VULNERABLE in enemy.conditions:
        player.energy += 1
        player.deck.draw_card()


def dual_wield_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    option = raw_input("Which card to copy? -> ")
    card = player.deck.hand[option]
    player.deck.draw_card(card)


def entrench_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(player.block)


def evolve_fx(combat, target):
    player = combat.player
    enemy = combat.enemies[target]
    evolved = StatusCondition(Status.EVOLVE, 1, True)
    player.apply_status_condition(evolved)


# <<<<<<< HEAD
# Parameters: "name", cost, CardType, fx function, Target, Exhaust (t/f)
strike = Card("Strike", 1, CardType.ATTACK, strike_fx, Target.SINGLE, False)
defend = Card("Defend", 1, CardType.SKILL, defend_fx, Target.SELF, False)
bash = Card("Bash", 2, CardType.ATTACK, bash_fx, Target.SINGLE, False)
anger = Card("Anger", 1, CardType.ATTACK, anger_fx, Target.SINGLE, False)
armaments = Card("Armaments", 1, CardType.SKILL, armaments_fx, Target.SELF, False)
bodySlam = Card("Body Slam", 1, CardType.ATTACK, bodyslam_fx, Target.SINGLE, False)
clash = Card("Clash", 0, CardType.ATTACK, clash_fx, Target.SINGLE, False)
clothesline = Card("Clothesline", 2, CardType.ATTACK, clothesline_fx, Target.SINGLE, False)
flex = Card("Flex", 0, CardType.SKILL, flex_fx, Target.SELF, False)
havoc = Card("Havoc", 1, CardType.SKILL, havoc_fx, Target.SELF, False)

headbutt = Card("Headbutt", 1, CardType.ATTACK, headbutt_fx, Target.SINGLE, False)
heavyBlade = Card("Heavy Blade", 2, CardType.ATTACK, heavy_blade_fx, Target.SINGLE, False)
ironWave = Card("Iron Wave", 1, CardType.ATTACK, iron_wave_fx, Target.SINGLE, False)
perfectedStrike = Card("Perfected Strike", 2, CardType.ATTACK, perfected_strike_fx, Target.SINGLE, False)
pommelStrike = Card("Pommel Strike", 1, CardType.ATTACK, pommel_strike_fx, Target.SINGLE, False)
shrugItOff = Card("Shrug it off", 1, CardType.SKILL, shrug_it_off_fx, Target.SELF, False)
thunderclap = Card("Thunderclap", 1, CardType.ATTACK, thunderclap_fx, Target.ALL, False)
trueGrit = Card("True Grit", 1, CardType.SKILL, true_grit_fx, Target.SELF, False)
twinStrike = Card("Twin Strike", 1, CardType.ATTACK, twin_strike_fx, Target.SINGLE, False)
warcry = Card("Warcry", 0, CardType.SKILL, warcry_fx, Target.SELF, True)
wildStrike = Card("Wild Strike", 1, CardType.ATTACK, wild_strike_fx, Target.SINGLE, False)
battleTrance = Card("Battle Trance", 0, CardType.SKILL, battle_trance_fx, Target.SELF, False)

# TODO: Counter for number of times we've taken damage
bloodForBlood = Card("Blood for Blood", 4, CardType.SKILL, blood_for_blood_fx, Target.SINGLE, False)

bloodLetting = Card("Bloodletting", 0, CardType.SKILL, wild_strike_fx, Target.SELF, False)
burningPact = Card("Burning Pact", 1, CardType.SKILL, wild_strike_fx, Target.SELF, False)
carnage = Card("Carnage", 2, CardType.ATTACK, wild_strike_fx, Target.SINGLE, False)
combust = Card("Combust", 1, CardType.POWER, wild_strike_fx, Target.SELF, False)
corruption = Card("Corruption", 3, CardType.POWER, wild_strike_fx, Target.SELF, False)
disarm = Card("Disarm", 1, CardType.SKILL, wild_strike_fx, Target.SINGLE, True)
dropkick = Card("Dropkick", 1, CardType.ATTACK, wild_strike_fx, Target.SINGLE, False)
dualWield = Card("Dual Wield", 1, CardType.SKILL, wild_strike_fx, Target.SELF, False)
entrench = Card("Entrench", 2, CardType.SKILL, wild_strike_fx, Target.SELF, False)
evolve = Card("Evolve", 1, CardType.POWER, wild_strike_fx, Target.SELF, False)
# =======
# >>>>>>> b048d96c58fdacaa4b154b626b5cb9008c106daf
# Not sure what this is...

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
