from main import Card
from main import StatusCondition
from main import Status
from main import CardType
from main import Target
from main import Deck
from main import Intent
import random


def testing_deck():
    deck = Deck()
    for i in range(3):
        deck.add_card(flex)
        deck.add_card(limitBreak)
    return deck

def generate_all_deck():
    deck = Deck()
    for i in range(3):
        deck.add_card(strike)
        deck.add_card(defend)
        deck.add_card(bash)
        deck.add_card(anger)
        deck.add_card(armaments)
        deck.add_card(bodySlam)
        deck.add_card(clash)
        deck.add_card(clothesline)
        deck.add_card(flex)
        deck.add_card(havoc)
        deck.add_card(headbutt)
        deck.add_card(heavyBlade)
        deck.add_card(ironWave)
        deck.add_card(perfectedStrike)
        deck.add_card(pommelStrike)
        deck.add_card(shrugItOff)
        deck.add_card(thunderclap)
        deck.add_card(trueGrit)
        deck.add_card(twinStrike)
        deck.add_card(warcry)
        deck.add_card(wildStrike)
        deck.add_card(battleTrance)
        deck.add_card(bloodForBlood)
        deck.add_card(bloodLetting)
        deck.add_card(burningPact)
        deck.add_card(carnage)
        deck.add_card(combust)
        deck.add_card(corruption)
        deck.add_card(disarm)
        deck.add_card(dropkick)
        deck.add_card(dualWield)
        deck.add_card(entrench)
        deck.add_card(evolve)
        deck.add_card(feelNoPain)
        deck.add_card(flameBarrier)
        deck.add_card(ghostlyArmor)
        deck.add_card(hemoKinesis)
        deck.add_card(inflame)
        deck.add_card(intimidate)
        deck.add_card(metallicize)
        deck.add_card(powerThrough)
        deck.add_card(pummel)
        deck.add_card(rage)
        deck.add_card(rampage)
        deck.add_card(recklessCharge)
        deck.add_card(rupture)
        deck.add_card(searingBlow)
        deck.add_card(secondWind)
        deck.add_card(seeingRed)
        deck.add_card(severSoul)
        deck.add_card(shockwave)
        deck.add_card(spotWeakness)
        deck.add_card(uppercut)
        deck.add_card(whirlwind)
        deck.add_card(barricade)
        deck.add_card(berserk)
        deck.add_card(bludgeon)
        deck.add_card(brutality)
        deck.add_card(darkEmbrace)
        deck.add_card(demonForm)
        deck.add_card(doubleTap)
        deck.add_card(exhume)
        deck.add_card(feed)
        deck.add_card(fiendFire)
        deck.add_card(immolate)
        deck.add_card(impervious)
        deck.add_card(juggernaut)
        deck.add_card(limitBreak)
        deck.add_card(offering)
        deck.add_card(reaper)
        deck.add_card(sentinel)
        deck.add_card(dazed)
        deck.add_card(wound)
        deck.add_card(burn)
    return deck


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


def strike_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(6))


def defend_fx(combat, target, count):
    player = combat.player
    player.gain_block(5)


def bash_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(8))
    condition = StatusCondition(Status.VULNERABLE, 0, 2, False)
    enemy.apply_status_condition(condition)


def anger_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(5))
    player = combat.player
    player.deck.discard_pile.append(anger)


def armaments_fx(combat, target, count):
    # TODO: ask player which card they want to upgrade
    player = combat.player
    player.gain_block(5)


def bodyslam_fx(combat, target, count):
    block = combat.player.block
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(block))


def clash_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(14))


# Clothesline: deals 12(14) damage and applies 2(3) weak.
def clothesline_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))
    vulnerable = StatusCondition(Status.VULNERABLE, 0, 2, False)
    enemy.apply_status_condition(vulnerable)


# Flex: gain 2(4) strength at the beginning of turn, then lose 2(4) at the end of turn.
def flex_fx(combat, target, count):
    player = combat.player
    flexing = StatusCondition(Status.FLEX, 2, 1, False)
    strength = StatusCondition(Status.STRENGTH, 2, 0, True)
    player.apply_status_condition(flexing)
    player.apply_status_condition(strength)


# Draws the top card on the draw pile, play, and exhaust it
def havoc_fx(combat, target, count):
    card = combat.player.deck.draw_pile.pop()
    tempCost = card.cost
    tempExhaust = card.exhaust
    card.cost = 0
    card.exhaust = True
    combat.player.deck.use_card(card)
    card.cost = tempCost
    card.exhaust = tempExhaust


def headbutt_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(9))
    addendum = player.deck.discard_pile.pop()
    player.deck.draw_pile.insert(0, addendum)


def heavy_blade_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    # Multiplies strength by 3, attacks, and divides by 3 again.
    if Status.STRENGTH in player.conditions:
        player.conditions[Status.STRENGTH] *= 3
    enemy.take_damage(player.generate_damage(14))
    if Status.STRENGTH in player.conditions:
        player.conditions[Status.STRENGTH] /= 3


def iron_wave_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(5)
    enemy.take_damage(player.generate_damage(5))


def perfected_strike_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    damage = 6
    for card in player.deck.draw_pile:
        if "strike" in card.name.lower():
            damage += 2
    for card in player.deck.hand:
        if "strike" in card.name.lower():
            damage += 2
    for card in player.deck.discard_pile:
        if "strike" in card.name.lower():
            damage += 2
    for card in player.deck.exhaust_pile:
        if "strike" in card.name.lower():
            damage += 2
    enemy.take_damage(player.generate_damage(damage))


def pommel_strike_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(9))
    player.deck.draw_card()


def shrug_it_off_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(8)
    player.deck.draw_card()


def thunderclap_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        vulnerable = StatusCondition(Status.VULNERABLE, 0, 1, False)
        enemy.take_damage(4)
        enemy.apply_status_condition(vulnerable)


# Gains 7 block; exhausts a random card
def true_grit_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(7)
    if len(player.deck.hand) > 0:
        card = random.choice(player.deck.hand)
        player.deck.exhaust_card(card)


def twin_strike_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(5))
    enemy.take_damage(player.generate_damage(5))


def warcry_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.deck.draw_card()
    option = raw_input("Which card to place on top of your draw pile? -> ")
    card = player.deck.hand[option]
    player.deck.hand.remove(card)
    player.deck.draw_pile.append(card)


def wild_strike_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))
    random_number = random.randint(0, len(player.deck.draw_pile))
    player.deck.draw_pile.insert(random_number, wound)


def battle_trance_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    for i in range(3):
        player.deck.draw_card()
    noDraw = StatusCondition(Status.NO_DRAW, 1, 0, True)
    player.apply_status_condition(noDraw)


def blood_for_blood_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(18))
    # Note: Energy reduction already accounted for


def bloodletting_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.lose_health(3)
    player.gain_energy(1)


def burning_pact_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.deck.draw_card()
    player.deck.draw_card()
    option = raw_input("Which card to exhaust? -> ")
    card = player.deck.hand[option]
    player.deck.remove_card(card)
    player.deck.exhaust_pile.append(card)


def carnage_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(20))


def combust_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    combustion = StatusCondition(Status.COMBUST, 0, 1, False)
    player.apply_status_condition(combustion)


def corruption_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    corrupt = StatusCondition(Status.CORRUPTION, 0, 2, False)
    player.apply_status_condition(corrupt)


def disarm_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    weak = StatusCondition(Status.STRENGTH, -2, 0, True)
    enemy.apply_status_condition(weak)


def dropkick_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(5))
    if Status.VULNERABLE in enemy.conditions:
        player.energy += 1
        player.deck.draw_card()


def dual_wield_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    option = raw_input("Which card to copy? -> ")
    card = player.deck.hand[option]
    player.deck.draw_card(card)


def entrench_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(player.block)


def evolve_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    evolved = StatusCondition(Status.EVOLVE, 1, 0, True)
    player.apply_status_condition(evolved)

# --------------------------------------------

def feel_no_pain_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    noPainNoGain = StatusCondition(Status.FEELNOPAIN, 4, 0, True)
    enemy.apply_status_condition(noPainNoGain)


def flame_barrier_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(12)
    fireInYourHair = StatusCondition(Status.FLAMEBARRIER, 6, 1, False)
    enemy.apply_status_condition(fireInYourHair)


def ghostly_armor_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(10)


def hemokinesis_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.lose_health(3)
    enemy.take_damage(player.generate_damage(14))


def inflame_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    inflamed = StatusCondition(Status.STRENGTH, 2, 0, True)
    player.apply_status_condition(inflamed)


def intimidate_fx(combat, target, count):
    player = combat.player
    getRekt = StatusCondition(Status.WEAK, 0, 1, False)
    for enemy in combat.enemies:
        enemy.apply_status_condition(getRekt)


def metallicize_fx(combat, target, count):
    player = combat.player
    metalMan = StatusCondition(Status.METALLICIZE, 3, 0, True)
    player.apply_status_condition(metalMan)


def power_through_fx(combat, target, count):
    player = combat.player
    player.gain_block(15)
    if len(player.deck.hand) < 12:
        player.deck.hand.append(wound)
    else:
        player.deck.discard_pile.append(wound)
    player.deck.hand.append(wound)



def pummel_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    for i in range(4):
        enemy.take_damage(player.generate_damage(2))


def rage_fx(combat, target, count):
    player = combat.player
    rawr = StatusCondition(Status.RAGE, 3, 0, True)
    player.apply_status_condition(rawr)

# ----------------------------------------------------

def rampage_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(8 + 4 * count))


def reckless_charge_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(7))
    player.deck.discard_pile.append(dazed)


def rupture_fx(combat, target, count):
    player = combat.player
    wheredMyBloodGo = StatusCondition(Status.RUPTURE, 1, 0, True)
    player.apply_status_condition(wheredMyBloodGo)


def searing_blow_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))


def second_wind_fx(combat, target, count):
    player = combat.player
    to_remove = []
    for card in player.deck.hand:
        if card.card_type != CardType.ATTACK:
            to_remove.append(card)
    for card in to_remove:
        player.gain_block(5)
        player.deck.exhaust_card(card)


def seeing_red_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_energy(2)


def sever_soul_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(16))
    to_remove = []
    for card in player.deck.hand:
        if card.card_type != CardType.ATTACK:
            to_remove.append(card)
    for card in to_remove:
        player.deck.exhaust_card(card)


def shockwave_fx(combat, target, count):
    shock = StatusCondition(Status.VULNERABLE, 0, 3, False)
    wave = StatusCondition(Status.WEAK, 0, 3, False)
    for enemy in combat.enemies:
        enemy.apply_status_condition(shock)
        enemy.apply_status_condition(wave)


def spot_weakness_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    if enemy.intent[0] == Intent.ATTACK:
        gotem = StatusCondition(Status.STRENGTH, 3, 0, True)
        player.apply_status_condition(gotem)


def uppercut_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(13))
    upper = StatusCondition(Status.VULNERABLE, 0, 1, False)
    cut = StatusCondition(Status.WEAK, 0, 1, False)
    enemy.apply_status_condition(upper)
    enemy.apply_status_condition(cut)

# -----------------------------------------------


def whirlwind_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        for i in range(player.energy + 1):
            enemy.take_damage(player.generate_damage(5))


def barricade_fx(combat, target, count):
    player = combat.player
    barricadus = StatusCondition(Status.BARRICADE, 1, 0, True)
    player.apply_status_condition(barricadus)


def berserk_fx(combat, target, count):
    player = combat.player
    betaBerserker = StatusCondition(Status.BERSERK, 1, 0, True)
    player.apply_status_condition(betaBerserker)


def bludgeon_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(32))


def brutality_fx(combat, target, count):
    player = combat.player
    brute = StatusCondition(Status.BRUTALITY, 1, 0, True)
    player.apply_status_condition(brute)


def dark_embrace_fx(combat, target, count):
    player = combat.player
    hugs = StatusCondition(Status.EMBRACE, 1, 0, True)
    player.apply_status_condition(hugs)


def demon_form_fx(combat, target, count):
    player = combat.player
    antiChrist = StatusCondition(Status.DEMON, 1, 0, True)
    player.apply_status_condition(antiChrist)


def double_tap_fx(combat, target, count):
    player = combat.player
    doubleDipping = StatusCondition(Status.DOUBLE, 0, 1, False)
    player.apply_status_condition(doubleDipping)


# TODO: Draw a card from the exhaust pile
def exhume_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]


def feed_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(10))
    if enemy.health == 0:
        player.max_health += 3
        # TODO: increase real player's max health (not the combat players)

# -------------------------------------


def fiend_fire_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    for i in range(len(player.deck.hand)):
        enemy.take_damage(player.generate_damage(7))
        player.deck.exhaust_card(player.deck.hand[0])


def immolate_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        enemy.take_damage(player.generate_damage(21))
    player.deck.discard_pile.append(burn)


def impervious_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(30)


def juggernaut_fx(combat, target, count):
    player = combat.player
    juggler_naught = StatusCondition(Status.JUGGERNAUT, 3, 0, True)
    player.apply_status_condition(juggler_naught)


def limit_break_fx(combat, target, count):
    player = combat.player
    if Status.STRENGTH in player.conditions:
        player.conditions[Status.STRENGTH].value *= 2


def offering_fx(combat, target, count):
    player = combat.player
    player.lose_health(4)
    player.gain_energy(2)
    for i in range(3):
        player.deck.draw_card()


def reaper_fx(combat, target, count):
    player = combat.player
    oldTotalHealth = 0
    newTotalHealth = 0
    for enemy in combat.enemies:
        oldTotalHealth += enemy.health
        enemy.take_damage(player.generate_damage(5))
        newTotalHealth += enemy.health
    player.heal_health(oldTotalHealth - newTotalHealth)


def sentinel_fx(combat, target, count):
    player = combat.player
    player.gain_block(5)


def status_fx(combat, target, count):
    return

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

bloodLetting = Card("Bloodletting", 0, CardType.SKILL, bloodletting_fx, Target.SELF, False)
burningPact = Card("Burning Pact", 1, CardType.SKILL, burning_pact_fx, Target.SELF, False)
carnage = Card("Carnage", 2, CardType.ATTACK, carnage_fx, Target.SINGLE, False)
combust = Card("Combust", 1, CardType.POWER, combust_fx, Target.SELF, False)
corruption = Card("Corruption", 3, CardType.POWER, corruption_fx, Target.SELF, False)
disarm = Card("Disarm", 1, CardType.SKILL, disarm_fx, Target.SINGLE, True)
dropkick = Card("Dropkick", 1, CardType.ATTACK, dropkick_fx, Target.SINGLE, False)
dualWield = Card("Dual Wield", 1, CardType.SKILL, dual_wield_fx, Target.SELF, False)
entrench = Card("Entrench", 2, CardType.SKILL, entrench_fx, Target.SELF, False)
evolve = Card("Evolve", 1, CardType.POWER, evolve_fx, Target.SELF, False)

feelNoPain = Card("Feel No Pain", 1, CardType.POWER, feel_no_pain_fx, Target.SELF, False)
flameBarrier = Card("Flame Barrier", 2, CardType.SKILL, flame_barrier_fx, Target.SELF, False)
ghostlyArmor = Card("Ghostly Armor", 1, CardType.SKILL, ghostly_armor_fx, Target.SELF, False)
hemoKinesis = Card("Hemokinesis", 1, CardType.ATTACK, hemokinesis_fx, Target.SINGLE, False)
inflame = Card("Inflame", 1, CardType.POWER, inflame_fx, Target.SELF, False)
intimidate = Card("Intimidate", 0, CardType.SKILL, intimidate_fx, Target.ALL, True)
metallicize = Card("Metallicize", 1, CardType.POWER, metallicize_fx, Target.SELF, False)
powerThrough = Card("Power Through", 1, CardType.SKILL, power_through_fx, Target.SELF, False)
pummel = Card("Pummel", 1, CardType.ATTACK, pummel_fx, Target.SINGLE, True)
rage = Card("Rage", 0, CardType.SKILL, rage_fx, Target.SELF, False)

rampage = Card("Rampage", 1, CardType.ATTACK, rampage_fx, Target.SINGLE, False)
recklessCharge = Card("Reckless Charge", 0, CardType.ATTACK, reckless_charge_fx, Target.SINGLE, False)
rupture = Card("Rupture", 1, CardType.POWER, rupture_fx, Target.SELF, False)
searingBlow = Card("Searing Blow", 2, CardType.ATTACK, searing_blow_fx, Target.SINGLE, False)
secondWind = Card("Second Wind", 1, CardType.SKILL, second_wind_fx, Target.SELF, False)
seeingRed = Card("Seeing Red", 1, CardType.SKILL, seeing_red_fx, Target.SELF, True)
severSoul = Card("Sever Soul", 2, CardType.ATTACK, sever_soul_fx, Target.SINGLE, False)
shockwave = Card("Shock Wave", 2, CardType.SKILL, shockwave_fx, Target.ALL, True)
spotWeakness = Card("Spot Weakness", 1, CardType.SKILL, spot_weakness_fx, Target.SINGLE, False)
uppercut = Card("Uppercut", 2, CardType.ATTACK, uppercut_fx, Target.SINGLE, False)

whirlwind = Card("Whirlwind", 1, CardType.ATTACK, whirlwind_fx, Target.ALL, False)
barricade = Card("Barricade", 3, CardType.SKILL, barricade_fx, Target.SELF, False)
berserk = Card("Berserk", 1, CardType.POWER, berserk_fx, Target.SELF, False)
bludgeon = Card("Bludgeon", 3, CardType.ATTACK, bludgeon_fx, Target.SINGLE, False)
brutality = Card("Brutality", 0, CardType.POWER, brutality_fx, Target.SELF, False)
darkEmbrace = Card("Dark Embrace", 2, CardType.POWER, dark_embrace_fx, Target.SELF, False)
demonForm = Card("Demon Form", 3, CardType.POWER, demon_form_fx, Target.SELF, False)
doubleTap = Card("Double Tap", 1, CardType.SKILL, double_tap_fx, Target.SELF, False)
exhume = Card("Exhume", 1, CardType.SKILL, exhume_fx, Target.SELF, True)
feed = Card("Feed", 1, CardType.ATTACK, feed_fx, Target.SINGLE, False)

fiendFire = Card("Fiend Fire", 2, CardType.ATTACK, fiend_fire_fx, Target.SINGLE, True)
immolate = Card("Immolate", 2, CardType.ATTACK, immolate_fx, Target.ALL, False)
impervious = Card("Impervious", 2, CardType.SKILL, impervious_fx, Target.SELF, True)
juggernaut = Card("Juggernaut", 2, CardType.POWER, juggernaut_fx, Target.SELF, False)
limitBreak = Card("Limit Break", 1, CardType.SKILL, limit_break_fx, Target.SELF, True)
offering = Card("Offering", 0, CardType.SKILL, offering_fx, Target.SINGLE, True)
reaper = Card("Reaper", 2, CardType.ATTACK, reaper_fx, Target.ALL, True)
sentinel = Card("Sentinel", 1, CardType.SKILL, sentinel_fx, Target.SELF, False)

dazed = Card("Dazed", 0, CardType.STATUS, status_fx, Target.SELF, False)
wound = Card("Wound", 0, CardType.STATUS, status_fx, Target.SELF, False)
burn = Card("Burn", 0, CardType.STATUS, status_fx, Target.SELF, False)
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
