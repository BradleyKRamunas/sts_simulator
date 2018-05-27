from player import Card
from combat import StatusCondition
from player import Deck
from enums import *
import random

def testing_deck():
    deck = Deck()

    for i in range(10):
        deck.add_card(defend)
        deck.add_card(bodySlam)
        deck.add_card(shrugItOff)
        deck.add_card(impervious)
    for i in range(3):
        deck.add_card(barricade)
    return deck

def generate_upgrade_dictionary():
    cards = generate_all_cards()
    upgrades = generate_all_upgraded_cards()
    correspond = {}
    for i in range(len(cards)-1):
        card = cards[i]
        upgrade = upgrades[i]
        correspond[card.name] = upgrade
    return correspond

def generate_common_cards():
    cards = []
    cards.append(bash)
    cards.append(anger)
    cards.append(bodySlam)
    cards.append(cleave)
    cards.append(clothesline)
    cards.append(headbutt)
    cards.append(ironWave)
    cards.append(pommelStrike)
    cards.append(shrugItOff)
    cards.append(thunderclap)
    cards.append(trueGrit)
    cards.append(twinStrike)
    cards.append(wildStrike)
    cards.append(rampage)
    cards.append(recklessCharge)
    cards.append(uppercut)
    cards.append(whirlwind)
    cards.append(sentinel)
    return cards


def generate_uncommon_cards():
    cards = []
    cards.append(armaments)  # uncommon
    cards.append(flex)  # uncommon
    cards.append(heavyBlade)  # uncommon
    cards.append(perfectedStrike)  # uncommon
    cards.append(warcry)  # uncommon
    cards.append(battleTrance)  # uncommon
    cards.append(bloodLetting)  # uncommon
    cards.append(carnage)  # uncommon
    cards.append(combust)  # uncommon
    cards.append(dropkick)  # uncommon
    cards.append(entrench)  # uncommon
    cards.append(evolve)  # uncommon
    cards.append(feelNoPain)  # uncommon
    cards.append(flameBarrier)  # uncommon
    cards.append(hemoKinesis)  # uncommon
    cards.append(inflame)  # uncommon
    cards.append(metallicize)  # uncommon
    cards.append(pummel)  # uncommon
    cards.append(rage)  # uncommon
    cards.append(searingBlow)  # uncommon
    cards.append(secondWind)  # uncommon
    cards.append(severSoul)  # uncommon
    cards.append(shockwave)  # uncommon
    cards.append(spotWeakness)  # uncommon
    cards.append(sentinel)  # uncommon
    return cards


def generate_rare_cards():
    cards = []
    cards.append(havoc)  # rare
    cards.append(bloodForBlood)  # rare
    cards.append(burningPact)  # rare
    cards.append(corruption)  # rare
    cards.append(disarm)  # rare
    cards.append(dualWield)  # rare
    cards.append(rupture)  # rare
    cards.append(seeingRed)  # rare
    cards.append(barricade)  # rare
    cards.append(berserk)  # rare
    cards.append(bludgeon)  # rare
    cards.append(brutality)  # rare
    cards.append(darkEmbrace)  # rare
    cards.append(demonForm)  # rare
    cards.append(doubleTap)  # rare
    cards.append(exhume)  # rare
    cards.append(feed)  # rare
    cards.append(fiendFire)  # rare
    cards.append(immolate)  # rare
    cards.append(impervious)  # rare
    cards.append(juggernaut)  # rare
    cards.append(limitBreak)  # rare
    cards.append(offering)  # rare
    cards.append(reaper)  # rare
    return cards


def generate_all_cards():
    cards = []
    cards.append(strike)  # no rarity
    cards.append(defend)  # no rarity
    cards.append(bash)  # common
    cards.append(anger)  # common
    cards.append(armaments)  # uncommon
    cards.append(bodySlam)  # common
    cards.append(clash)  # uncommon
    cards.append(cleave)  # common
    cards.append(clothesline)  # common
    cards.append(flex)  # uncommon
    cards.append(havoc)  # rare
    cards.append(headbutt)  # common
    cards.append(heavyBlade)  # uncommon
    cards.append(ironWave)  # common
    cards.append(perfectedStrike)  # uncommon
    cards.append(pommelStrike)  # common
    cards.append(shrugItOff)  # common
    cards.append(thunderclap)  # common
    cards.append(trueGrit)  # common
    cards.append(twinStrike)  # common
    cards.append(warcry)  # uncommon
    cards.append(wildStrike)  # common
    cards.append(battleTrance)  # uncommon
    cards.append(bloodForBlood)  # rare
    cards.append(bloodLetting)  # uncommon
    cards.append(burningPact)  # rare
    cards.append(carnage)  # uncommon
    cards.append(combust)  # uncommon
    cards.append(corruption)  # rare
    cards.append(disarm)  # rare
    cards.append(dropkick)  # uncommon
    cards.append(dualWield)  # rare
    cards.append(entrench)  # uncommon
    cards.append(evolve)  # uncommon
    cards.append(feelNoPain)  # uncommon
    cards.append(flameBarrier)  # uncommon
    cards.append(ghostlyArmor)  # common
    cards.append(hemoKinesis)  # uncommon
    cards.append(inflame)  # uncommon
    cards.append(intimidate)  # common
    cards.append(metallicize)  # uncommon
    cards.append(powerThrough)  # common
    cards.append(pummel)  # uncommon
    cards.append(rage)  # uncommon
    cards.append(rampage)  # common
    cards.append(recklessCharge)  # common
    cards.append(rupture)  # rare
    cards.append(searingBlow)  # uncommon
    cards.append(secondWind)  # uncommon
    cards.append(seeingRed)  # rare
    cards.append(severSoul)  # uncommon
    cards.append(shockwave)  # uncommon
    cards.append(spotWeakness)  # uncommon
    cards.append(uppercut)  # common
    cards.append(whirlwind)  # common
    cards.append(barricade)  # rare
    cards.append(berserk)  # rare
    cards.append(bludgeon)  # rare
    cards.append(brutality)  # rare
    cards.append(darkEmbrace)  # rare
    cards.append(demonForm)  # rare
    cards.append(doubleTap)  # rare
    cards.append(exhume)  # rare
    cards.append(feed)  # rare
    cards.append(fiendFire)  # rare
    cards.append(immolate)  # rare
    cards.append(impervious)  # rare
    cards.append(juggernaut)  # rare
    cards.append(limitBreak)  # rare
    cards.append(offering)  # rare
    cards.append(reaper)  # rare
    cards.append(sentinel)  # uncommon
    return cards

def generate_all_upgraded_cards():
    cards = []
    cards.append(strikePlus)  # no rarity
    cards.append(defendPlus)  # no rarity
    cards.append(bashPlus)  # common
    cards.append(angerPlus)  # common
    cards.append(armamentsPlus)  # uncommon
    cards.append(bodySlamPlus)  # common
    cards.append(clashPlus)  # uncommon
    cards.append(cleavePlus)  # common
    cards.append(clotheslinePlus)  # common
    cards.append(flexPlus)  # uncommon
    cards.append(havocPlus)  # rare
    cards.append(headbuttPlus)  # common
    cards.append(heavyBladePlus)  # uncommon
    cards.append(ironWavePlus)  # common
    cards.append(perfectedStrikePlus)  # uncommon
    cards.append(pommelStrikePlus)  # common
    cards.append(shrugItOffPlus)  # common
    cards.append(thunderclapPlus)  # common
    cards.append(trueGritPlus)  # common
    cards.append(twinStrikePlus)  # common
    cards.append(warcryPlus)  # uncommon
    cards.append(wildStrikePlus)  # common
    cards.append(battleTrancePlus)  # uncommon
    cards.append(bloodForBloodPlus)  # rare
    cards.append(bloodLettingPlus)  # uncommon
    cards.append(burningPactPlus)  # rare
    cards.append(carnagePlus)  # uncommon
    cards.append(combustPlus)  # uncommon
    cards.append(corruptionPlus)  # rare
    cards.append(disarmPlus)  # rare
    cards.append(dropkickPlus)  # uncommon
    cards.append(dualWieldPlus)  # rare
    cards.append(entrenchPlus)  # uncommon
    cards.append(evolvePlus)  # uncommon
    cards.append(feelNoPainPlus)  # uncommon
    cards.append(flameBarrierPlus)  # uncommon
    cards.append(ghostlyArmorPlus)  # common
    cards.append(hemoKinesisPlus)  # uncommon
    cards.append(inflamePlus)  # uncommon
    cards.append(intimidatePlus)  # common
    cards.append(metallicizePlus)  # uncommon
    cards.append(powerThroughPlus)  # common
    cards.append(pummelPlus)  # uncommon
    cards.append(ragePlus)  # uncommon
    cards.append(rampagePlus)  # common
    cards.append(recklessChargePlus)  # common
    cards.append(rupturePlus)  # rare
    cards.append(searingBlowPlus)  # uncommon
    cards.append(secondWindPlus)  # uncommon
    cards.append(seeingRedPlus)  # rare
    cards.append(severSoulPlus)  # uncommon
    cards.append(shockwavePlus)  # uncommon
    cards.append(spotWeaknessPlus)  # uncommon
    cards.append(uppercutPlus)  # common
    cards.append(whirlwindPlus)  # common
    cards.append(barricadePlus)  # rare
    cards.append(berserkPlus)  # rare
    cards.append(bludgeonPlus)  # rare
    cards.append(brutalityPlus)  # rare
    cards.append(darkEmbracePlus)  # rare
    cards.append(demonFormPlus)  # rare
    cards.append(doubleTapPlus)  # rare
    cards.append(exhumePlus)  # rare
    cards.append(feedPlus)  # rare
    cards.append(fiendFirePlus)  # rare
    cards.append(immolatePlus)  # rare
    cards.append(imperviousPlus)  # rare
    cards.append(juggernautPlus)  # rare
    cards.append(limitBreakPlus)  # rare
    cards.append(offeringPlus)  # rare
    cards.append(reaperPlus)  # rare
    cards.append(sentinelPlus)  # uncommon
    return cards


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
        deck.add_card(cleave)
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
    for i in range(5):
        deck.add_card(clash)
    return deck


def strike_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(6))

def strike_plus_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(9))

def defend_fx(combat, target, count):
    player = combat.player
    player.gain_block(5)

def defend_plus_fx(combat, target, count):
    player = combat.player
    player.gain_block(8)

def bash_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(8))
    condition = StatusCondition(Status.VULNERABLE, 0, 2, False)
    enemy.apply_status_condition(condition)

def bash_plus_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(10))
    condition = StatusCondition(Status.VULNERABLE, 0, 3, False)
    enemy.apply_status_condition(condition)

def anger_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(5))
    player = combat.player
    player.deck.discard_pile.append(anger)

def anger_plus_fx(combat, target, count):
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(7))
    player = combat.player
    player.deck.discard_pile.append(angerPlus)


def armaments_fx(combat, target, count):
    # TODO: ask player which card they want to upgrade
    player = combat.player
    player.gain_block(5)
    combat.state_type = StateType.UPGRADE


def armaments_plus_fx(combat, target, count):
    # TODO: ask player which card they want to upgrade
    player = combat.player
    player.gain_block(5)
    new_hand = []
    for card in player.deck.hand:
        if card.name in UPGRADE_DICT:
            new_hand.append(UPGRADE_DICT[card.name])
        else:
            new_hand.append(card)
    player.deck.hand = new_hand


def bodyslam_fx(combat, target, count):
    block = combat.player.block
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(block))


def bodyslam_plus_fx(combat, target, count):
    block = combat.player.block
    enemy = combat.enemies[target]
    enemy.take_damage(combat.player.generate_damage(block))


def clash_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    for card in player.deck.hand:
        if card.card_type != CardType.ATTACK:
            return
    enemy.take_damage(player.generate_damage(14))


def clash_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    for card in player.deck.hand:
        if card.card_type != CardType.ATTACK:
            return
    enemy.take_damage(player.generate_damage(18))


def cleave_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        if enemy.health > 0:
            enemy.take_damage(player.generate_damage(8))


def cleave_plus_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        if enemy.health > 0:
            enemy.take_damage(player.generate_damage(11))


def clothesline_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))
    unzipped = StatusCondition(Status.WEAK, 0, 2, False)
    enemy.apply_status_condition(unzipped)


def clothesline_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(14))
    unzipped = StatusCondition(Status.WEAK, 0, 3, False)
    enemy.apply_status_condition(unzipped)



def flex_fx(combat, target, count):
    player = combat.player
    flexing = StatusCondition(Status.FLEX, 2, 1, False)
    strength = StatusCondition(Status.STRENGTH, 2, 0, True)
    player.apply_status_condition(flexing)
    player.apply_status_condition(strength)


def flex_plus_fx(combat, target, count):
    player = combat.player
    flexing = StatusCondition(Status.FLEX, 4, 1, False)
    strength = StatusCondition(Status.STRENGTH, 4, 0, True)
    player.apply_status_condition(flexing)
    player.apply_status_condition(strength)


# Draws the top card on the draw pile, play, and exhaust it
def havoc_fx(combat, target, count):
    if len(combat.player.deck.draw_pile) > 0:
        card = combat.player.deck.draw_pile.pop(0)
        combat.player.deck.hand.append(card)
        tempCost = card.cost
        tempExhaust = card.exhaust
        card.cost = 0
        card.exhaust = True
        randomTarget = random.randint(0, len(combat.enemies) - 1)
        while combat.enemies[randomTarget].health <= 0:
            randomTarget = random.randint(0, len(combat.enemies) - 1)
        combat.player.deck.use_card(card, randomTarget)
        card.cost = tempCost
        card.exhaust = tempExhaust


def havoc_plus_fx(combat, target, count):
    if len(combat.player.deck.draw_pile) > 0:
        card = combat.player.deck.draw_pile.pop(0)
        combat.player.deck.hand.append(card)
        tempCost = card.cost
        tempExhaust = card.exhaust
        card.cost = 0
        card.exhaust = True
        randomTarget = random.randint(0, len(combat.enemies) - 1)
        while combat.enemies[randomTarget].health <= 0:
            randomTarget = random.randint(0, len(combat.enemies) - 1)
        combat.player.deck.use_card(card, randomTarget)
        card.cost = tempCost
        card.exhaust = tempExhaust


def headbutt_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(9))
    if not __debug__:
        if len(combat.player.deck.discard_pile) == 0:
            print ("Your discard is empty.")
        else:
            print ("Your discard: "),
            for card in combat.player.deck.discard_pile:
                print ("{}: {} |".format(count, card.name)),
                count += 1
            print
            index = int(raw_input("Which card would you like to recover from your discard pile? -> "))
            card = combat.player.deck.discard_pile.pop(index)
            player.deck.draw_pile.insert(0, card)
    else:
        combat.state_type = StateType.DISCARD_TO_DRAW


def headbutt_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))
    if not __debug__:
        if len(combat.player.deck.discard_pile) == 0:
            print ("Your discard is empty.")
        else:
            print ("Your discard: "),
            for card in combat.player.deck.discard_pile:
                print ("{}: {} |".format(count, card.name)),
                count += 1
            print
            index = int(raw_input("Which card would you like to recover from your discard pile? -> "))
            card = combat.player.deck.discard_pile.pop(index)
            player.deck.draw_pile.insert(0, card)
    else:
        combat.state_type = StateType.DISCARD_TO_DRAW


def heavy_blade_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    tempStr = 0
    # Multiplies strength by 3, attacks, and divides by 3 again.
    if Status.STRENGTH in player.conditions:
        tempStr = 2 * player.conditions[Status.STRENGTH].value
    enemy.take_damage(player.generate_damage(14 + tempStr))


def heavy_blade_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    tempStr = 0
    # Multiplies strength by 3, attacks, and divides by 3 again.
    if Status.STRENGTH in player.conditions:
        tempStr = 4 * player.conditions[Status.STRENGTH].value
    enemy.take_damage(player.generate_damage(14 + tempStr))


def iron_wave_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(5)
    enemy.take_damage(player.generate_damage(5))


def iron_wave_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(7)
    enemy.take_damage(player.generate_damage(7))


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


def perfected_strike_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    damage = 6
    for card in player.deck.draw_pile:
        if "strike" in card.name.lower():
            damage += 3
    for card in player.deck.hand:
        if "strike" in card.name.lower():
            damage += 3
    for card in player.deck.discard_pile:
        if "strike" in card.name.lower():
            damage += 3
    for card in player.deck.exhaust_pile:
        if "strike" in card.name.lower():
            damage += 3
    enemy.take_damage(player.generate_damage(damage))


def pommel_strike_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(9))
    player.deck.draw_card()


def pommel_strike_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(10))
    player.draw_cards(2)


def shrug_it_off_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(8)
    player.deck.draw_card()


def shrug_it_off_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(11)
    player.deck.draw_card()


def thunderclap_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        if enemy.health > 0:
            vulnerable = StatusCondition(Status.VULNERABLE, 0, 1, False)
            enemy.take_damage(4)
            enemy.apply_status_condition(vulnerable)


def thunderclap_plus_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        if enemy.health > 0:
            vulnerable = StatusCondition(Status.VULNERABLE, 0, 1, False)
            enemy.take_damage(7)
            enemy.apply_status_condition(vulnerable)


# Gains 7 block; exhausts a random card
def true_grit_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(7)
    if len(player.deck.hand) > 0:
        card = random.choice(player.deck.hand)
        player.deck.exhaust_card(card)


def true_grit_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(7)
    if not __debug__:
        # not implemented
        return
    else:
        combat.state_type = StateType.HAND_TO_EXHAUST


def twin_strike_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(5))
    enemy.take_damage(player.generate_damage(5))


def twin_strike_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(7))
    enemy.take_damage(player.generate_damage(7))


def warcry_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.deck.draw_card()
    if not __debug__:
        print ("Your hand: "),
        for card in combat.player.deck.hand:
            print ("{}: {} |".format(count, card.name)),
            count += 1
        print
        option = int(raw_input("Which card to place on top of your draw pile? -> "))
        card = player.deck.hand[option]
        player.deck.hand.remove(card)
        player.deck.draw_pile.insert(0, card)
    else:
        combat.state_type = StateType.HAND_TO_DRAW


def warcry_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.draw_cards(2)
    if not __debug__:
        print ("Your hand: "),
        for card in combat.player.deck.hand:
            print ("{}: {} |".format(count, card.name)),
            count += 1
        print
        option = int(raw_input("Which card to place on top of your draw pile? -> "))
        card = player.deck.hand[option]
        player.deck.hand.remove(card)
        player.deck.draw_pile.insert(0, card)
    else:
        combat.state_type = StateType.HAND_TO_DRAW


def wild_strike_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))
    random_number = random.randint(0, len(player.deck.draw_pile))
    player.deck.draw_pile.insert(random_number, wound)


def wild_strike_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(17))
    random_number = random.randint(0, len(player.deck.draw_pile))
    player.deck.draw_pile.insert(random_number, wound)


def battle_trance_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.draw_cards(3)
    noDraw = StatusCondition(Status.NO_DRAW, 1, 0, True)
    player.apply_status_condition(noDraw)


def battle_trance_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.draw_cards(4)
    noDraw = StatusCondition(Status.NO_DRAW, 1, 0, True)
    player.apply_status_condition(noDraw)


def blood_for_blood_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(18))
    # Note: Energy reduction already accounted for

def blood_for_blood_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(22))
    # Note: Energy reduction already accounted for


def bloodletting_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.lose_health(3)
    player.gain_energy(1)


def bloodletting_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.lose_health(3)
    player.gain_energy(2)


def burning_pact_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.draw_cards(2)
    if not __debug__:
        print ("Your hand: "),
        for card in combat.player.deck.hand:
            print ("{}: {} |".format(count, card.name)),
            count += 1
        print
        option = int(raw_input("Which card to exhaust? -> "))
        card = player.deck.hand[option]
        player.deck.exhaust_card(card)
    else:
        combat.state_type = StateType.HAND_TO_EXHAUST


def burning_pact_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.draw_cards(3)
    if not __debug__:
        print ("Your hand: "),
        for card in combat.player.deck.hand:
            print ("{}: {} |".format(count, card.name)),
            count += 1
        print
        option = int(raw_input("Which card to exhaust? -> "))
        card = player.deck.hand[option]
        player.deck.exhaust_card(card)
    else:
        combat.state_type = StateType.HAND_TO_EXHAUST


def carnage_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(20))


def carnage_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(28))

def combust_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    combustion = StatusCondition(Status.COMBUST, 1, 0, True)
    player.apply_status_condition(combustion)


def combust_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    combustion = StatusCondition(Status.COMBUST, 2, 0, True)
    player.apply_status_condition(combustion)


def corruption_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    corrupt = StatusCondition(Status.CORRUPTION, 1, 0, True)
    player.apply_status_condition(corrupt)


def corruption_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    corrupt = StatusCondition(Status.CORRUPTION, 1, 0, True)
    player.apply_status_condition(corrupt)


def disarm_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    weak = StatusCondition(Status.STRENGTH, -2, 0, True)
    enemy.apply_status_condition(weak)


def disarm_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    weak = StatusCondition(Status.STRENGTH, -3, 0, True)
    enemy.apply_status_condition(weak)


def dropkick_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(5))
    if Status.VULNERABLE in enemy.conditions:
        player.energy += 1
        player.deck.draw_card()


def dropkick_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(8))
    if Status.VULNERABLE in enemy.conditions:
        player.energy += 1
        player.deck.draw_card()


def dual_wield_fx(combat, target, count):
    # TODO: only attack cards
    player = combat.player
    enemy = combat.enemies[target]
    if not __debug__:
        print ("Your hand: "),
        for card in combat.player.deck.hand:
            print ("{}: {} |".format(count, card.name)),
            count += 1
        print
        option = int(raw_input("Which card to copy? -> "))
        card = player.deck.hand[option]
        player.deck.hand.append(card)
    else:
        combat.state_type = StateType.COPY


def dual_wield_plus_fx(combat, target, count):
    # TODO: only attack cards
    player = combat.player
    enemy = combat.enemies[target]
    if not __debug__:
        print ("Your hand: "),
        for card in combat.player.deck.hand:
            print ("{}: {} |".format(count, card.name)),
            count += 1
        print
        option = int(raw_input("Which card to copy? -> "))
        card = player.deck.hand[option]
        player.deck.hand.append(card)
    else:
        combat.state_type = StateType.COPY


def entrench_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(player.block)


def entrench_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(player.block)


def evolve_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    evolved = StatusCondition(Status.EVOLVE, 1, 0, True)
    player.apply_status_condition(evolved)


def evolve_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    evolved = StatusCondition(Status.EVOLVE, 2, 0, True)
    player.apply_status_condition(evolved)

# --------------------------------------------

def feel_no_pain_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    noPainNoGain = StatusCondition(Status.FEELNOPAIN, 3, 0, True)
    enemy.apply_status_condition(noPainNoGain)


def feel_no_pain_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    noPainNoGain = StatusCondition(Status.FEELNOPAIN, 4, 0, True)
    enemy.apply_status_condition(noPainNoGain)


def flame_barrier_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(12)
    fireInYourHair = StatusCondition(Status.FLAMEBARRIER, 4, 1, False)
    enemy.apply_status_condition(fireInYourHair)


def flame_barrier_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(16)
    fireInYourHair = StatusCondition(Status.FLAMEBARRIER, 6, 1, False)
    enemy.apply_status_condition(fireInYourHair)


def ghostly_armor_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(10)


def ghostly_armor_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(13)


def hemokinesis_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.lose_health(3)
    enemy.take_damage(player.generate_damage(14))


def hemokinesis_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.lose_health(2)
    enemy.take_damage(player.generate_damage(18))


def inflame_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    inflamed = StatusCondition(Status.STRENGTH, 2, 0, True)
    player.apply_status_condition(inflamed)


def inflame_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    inflamed = StatusCondition(Status.STRENGTH, 3, 0, True)
    player.apply_status_condition(inflamed)


def intimidate_fx(combat, target, count):
    player = combat.player
    getRekt = StatusCondition(Status.WEAK, 0, 1, False)
    for enemy in combat.enemies:
        if enemy.health > 0:
            enemy.apply_status_condition(getRekt)


def intimidate_plus_fx(combat, target, count):
    player = combat.player
    getRekt = StatusCondition(Status.WEAK, 0, 2, False)
    for enemy in combat.enemies:
        if enemy.health > 0:
            enemy.apply_status_condition(getRekt)


def metallicize_fx(combat, target, count):
    player = combat.player
    metalMan = StatusCondition(Status.METALLICIZE, 3, 0, True)
    player.apply_status_condition(metalMan)


def metallicize_plus_fx(combat, target, count):
    player = combat.player
    metalMan = StatusCondition(Status.METALLICIZE, 4, 0, True)
    player.apply_status_condition(metalMan)


def power_through_fx(combat, target, count):
    player = combat.player
    player.gain_block(15)
    if len(player.deck.hand) < 12:
        player.deck.hand.append(wound)
    else:
        player.deck.discard_pile.append(wound)
    player.deck.hand.append(wound)


def power_through_plus_fx(combat, target, count):
    player = combat.player
    player.gain_block(20)
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


def pummel_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    for i in range(5):
        enemy.take_damage(player.generate_damage(2))


def rage_fx(combat, target, count):
    player = combat.player
    rawr = StatusCondition(Status.RAGE, 3, 0, True)
    player.apply_status_condition(rawr)


def rage_plus_fx(combat, target, count):
    player = combat.player
    rawr = StatusCondition(Status.RAGE, 5, 0, True)
    player.apply_status_condition(rawr)

# ----------------------------------------------------

def rampage_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(8 + 4 * count))


def rampage_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(8 + 8 * count))


def reckless_charge_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(7))
    player.deck.discard_pile.append(dazed)


def reckless_charge_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(10))
    player.deck.discard_pile.append(dazed)


def rupture_fx(combat, target, count):
    player = combat.player
    wheredMyBloodGo = StatusCondition(Status.RUPTURE, 1, 0, True)
    player.apply_status_condition(wheredMyBloodGo)


def rupture_plus_fx(combat, target, count):
    player = combat.player
    wheredMyBloodGo = StatusCondition(Status.RUPTURE, 1, 0, True)
    player.apply_status_condition(wheredMyBloodGo)


def searing_blow_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))


def searing_blow_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(16))


def second_wind_fx(combat, target, count):
    player = combat.player
    to_remove = []
    for card in player.deck.hand:
        if card.card_type != CardType.ATTACK:
            to_remove.append(card)
    for card in to_remove:
        player.gain_block(5)
        player.deck.exhaust_card(card)


def second_wind_plus_fx(combat, target, count):
    player = combat.player
    to_remove = []
    for card in player.deck.hand:
        if card.card_type != CardType.ATTACK:
            to_remove.append(card)
    for card in to_remove:
        player.gain_block(7)
        player.deck.exhaust_card(card)


def seeing_red_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_energy(2)


def seeing_red_plus_fx(combat, target, count):
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


def sever_soul_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(20))
    to_remove = []
    for card in player.deck.hand:
        if card.card_type != CardType.ATTACK:
            to_remove.append(card)
    for card in to_remove:
        player.deck.exhaust_card(card)


def shockwave_fx(combat, target, count):
    for enemy in combat.enemies:
        if enemy.health > 0:
            shock = StatusCondition(Status.VULNERABLE, 0, 3, False)
            wave = StatusCondition(Status.WEAK, 0, 3, False)
            enemy.apply_status_condition(shock)
            enemy.apply_status_condition(wave)


def shockwave_plus_fx(combat, target, count):
    for enemy in combat.enemies:
        if enemy.health > 0:
            shock = StatusCondition(Status.VULNERABLE, 0, 5, False)
            wave = StatusCondition(Status.WEAK, 0, 5, False)
            enemy.apply_status_condition(shock)
            enemy.apply_status_condition(wave)


def spot_weakness_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    if enemy.intent[0] == Intent.ATTACK:
        gotem = StatusCondition(Status.STRENGTH, 3, 0, True)
        player.apply_status_condition(gotem)


def spot_weakness_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    if enemy.intent[0] == Intent.ATTACK:
        gotem = StatusCondition(Status.STRENGTH, 4, 0, True)
        player.apply_status_condition(gotem)


def uppercut_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(13))
    upper = StatusCondition(Status.VULNERABLE, 0, 1, False)
    cut = StatusCondition(Status.WEAK, 0, 1, False)
    enemy.apply_status_condition(upper)
    enemy.apply_status_condition(cut)


def uppercut_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(13))
    upper = StatusCondition(Status.VULNERABLE, 0, 2, False)
    cut = StatusCondition(Status.WEAK, 0, 2, False)
    enemy.apply_status_condition(upper)
    enemy.apply_status_condition(cut)

# -----------------------------------------------


def whirlwind_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        if enemy.health > 0:
            for i in range(player.energy + 1):
                enemy.take_damage(player.generate_damage(5))


def whirlwind_plus_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        if enemy.health > 0:
            for i in range(player.energy + 1):
                enemy.take_damage(player.generate_damage(8))


def barricade_fx(combat, target, count):
    player = combat.player
    barricadus = StatusCondition(Status.BARRICADE, 1, 0, True)
    player.apply_status_condition(barricadus)


def barricade_plus_fx(combat, target, count):
    player = combat.player
    barricadus = StatusCondition(Status.BARRICADE, 1, 0, True)
    player.apply_status_condition(barricadus)


def berserk_fx(combat, target, count):
    player = combat.player
    betaBerserker = StatusCondition(Status.BERSERK, 1, 0, True)
    player.apply_status_condition(betaBerserker)


def berserk_plus_fx(combat, target, count):
    player = combat.player
    betaBerserker = StatusCondition(Status.BERSERK, 1, 0, True)
    player.apply_status_condition(betaBerserker)


def bludgeon_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(32))


def bludgeon_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(42))


def brutality_fx(combat, target, count):
    player = combat.player
    brute = StatusCondition(Status.BRUTALITY, 1, 0, True)
    player.apply_status_condition(brute)


def brutality_plus_fx(combat, target, count):
    player = combat.player
    brute = StatusCondition(Status.BRUTALITY, 2, 0, True)
    player.apply_status_condition(brute)


def dark_embrace_fx(combat, target, count):
    player = combat.player
    hugs = StatusCondition(Status.EMBRACE, 1, 0, True)
    player.apply_status_condition(hugs)


def dark_embrace_plus_fx(combat, target, count):
    player = combat.player
    hugs = StatusCondition(Status.EMBRACE, 1, 0, True)
    player.apply_status_condition(hugs)


def demon_form_fx(combat, target, count):
    player = combat.player
    antiChrist = StatusCondition(Status.DEMON, 2, 0, True)
    player.apply_status_condition(antiChrist)


def demon_form_plus_fx(combat, target, count):
    player = combat.player
    antiChrist = StatusCondition(Status.DEMON, 3, 0, True)
    player.apply_status_condition(antiChrist)


def double_tap_fx(combat, target, count):
    player = combat.player
    doubleDipping = StatusCondition(Status.DOUBLE, 0, 1, False)
    player.apply_status_condition(doubleDipping)


def double_tap_plus_fx(combat, target, count):
    player = combat.player
    doubleDipping = StatusCondition(Status.DOUBLE, 0, 2, False)
    player.apply_status_condition(doubleDipping)


def exhume_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    if not __debug__:
        # TODO: not implemented for debug mode
        return
    else:
        combat.state_type = StateType.EXHAUST_TO_HAND


def exhume_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    if not __debug__:
        # TODO: not implemented for debug mode
        return
    else:
        combat.state_type = StateType.EXHAUST_TO_HAND


def feed_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(10))
    if enemy.health == 0:
        player.max_health += 3
        player.heal_health(3)
        # TODO: increase real player's max health (not the combat players)


def feed_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    enemy.take_damage(player.generate_damage(12))
    if enemy.health == 0:
        player.max_health += 4
        player.heal_health(4)
        # TODO: increase real player's max health (not the combat players)

# -------------------------------------


def fiend_fire_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    for i in range(len(player.deck.hand)):
        enemy.take_damage(player.generate_damage(7))
        player.deck.exhaust_card(player.deck.hand[0])


def fiend_fire_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    for i in range(len(player.deck.hand)):
        enemy.take_damage(player.generate_damage(10))
        player.deck.exhaust_card(player.deck.hand[0])


def immolate_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        if enemy.health > 0:
            enemy.take_damage(player.generate_damage(21))
    player.deck.discard_pile.append(burn)


def immolate_plus_fx(combat, target, count):
    player = combat.player
    for enemy in combat.enemies:
        if enemy.health > 0:
            enemy.take_damage(player.generate_damage(28))
    player.deck.discard_pile.append(burn)


def impervious_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(30)


def impervious_plus_fx(combat, target, count):
    player = combat.player
    enemy = combat.enemies[target]
    player.gain_block(40)


def juggernaut_fx(combat, target, count):
    player = combat.player
    juggler_naught = StatusCondition(Status.JUGGERNAUT, 3, 0, True)
    player.apply_status_condition(juggler_naught)


def juggernaut_plus_fx(combat, target, count):
    player = combat.player
    juggler_naught = StatusCondition(Status.JUGGERNAUT, 5, 0, True)
    player.apply_status_condition(juggler_naught)


def limit_break_fx(combat, target, count):
    player = combat.player
    if Status.STRENGTH in player.conditions:
        player.conditions[Status.STRENGTH].value *= 2


def limit_break_plus_fx(combat, target, count):
    player = combat.player
    if Status.STRENGTH in player.conditions:
        player.conditions[Status.STRENGTH].value *= 2


def offering_fx(combat, target, count):
    player = combat.player
    player.lose_health(4)
    player.gain_energy(2)
    player.draw_cards(3)


def offering_plus_fx(combat, target, count):
    player = combat.player
    player.lose_health(4)
    player.gain_energy(2)
    player.draw_cards(5)


def reaper_fx(combat, target, count):
    player = combat.player
    oldTotalHealth = 0
    newTotalHealth = 0
    for enemy in combat.enemies:
        if enemy.health > 0:
            oldTotalHealth += enemy.health
            enemy.take_damage(player.generate_damage(4))
            newTotalHealth += enemy.health
    player.heal_health(oldTotalHealth - newTotalHealth)


def reaper_plus_fx(combat, target, count):
    player = combat.player
    oldTotalHealth = 0
    newTotalHealth = 0
    for enemy in combat.enemies:
        if enemy.health > 0:
            oldTotalHealth += enemy.health
            enemy.take_damage(player.generate_damage(5))
            newTotalHealth += enemy.health
    player.heal_health(oldTotalHealth - newTotalHealth)


def sentinel_fx(combat, target, count):
    player = combat.player
    player.gain_block(5)


def sentinel_plus_fx(combat, target, count):
    player = combat.player
    player.gain_block(8)


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
cleave = Card("Cleave", 1, CardType.ATTACK, cleave_fx, Target.ALL, False)
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

# Upgraded cards

strikePlus = Card("Strike+", 1, CardType.ATTACK, strike_plus_fx, Target.SINGLE, False)
defendPlus = Card("Defend+", 1, CardType.SKILL, defend_plus_fx, Target.SELF, False)
bashPlus = Card("Bash+", 2, CardType.ATTACK, bash_plus_fx, Target.SINGLE, False)
angerPlus = Card("Anger+", 1, CardType.ATTACK, anger_plus_fx, Target.SINGLE, False)
armamentsPlus = Card("Armaments+", 1, CardType.SKILL, armaments_plus_fx, Target.SELF, False)
bodySlamPlus = Card("Body Slam+", 0, CardType.ATTACK, bodyslam_plus_fx, Target.SINGLE, False)
clashPlus = Card("Clash+", 0, CardType.ATTACK, clash_plus_fx, Target.SINGLE, False)
cleavePlus = Card("Cleave+", 1, CardType.ATTACK, cleave_plus_fx, Target.ALL, False)
clotheslinePlus = Card("Clothesline+", 2, CardType.ATTACK, clothesline_plus_fx, Target.SINGLE, False)
flexPlus = Card("Flex+", 0, CardType.SKILL, flex_plus_fx, Target.SELF, False)
havocPlus = Card("Havoc+", 0, CardType.SKILL, havoc_plus_fx, Target.SELF, False)

headbuttPlus = Card("Headbutt+", 1, CardType.ATTACK, headbutt_plus_fx, Target.SINGLE, False)
heavyBladePlus = Card("Heavy Blade+", 2, CardType.ATTACK, heavy_blade_plus_fx, Target.SINGLE, False)
ironWavePlus = Card("Iron Wave+", 1, CardType.ATTACK, iron_wave_plus_fx, Target.SINGLE, False)
perfectedStrikePlus = Card("Perfected Strike+", 2, CardType.ATTACK, perfected_strike_plus_fx, Target.SINGLE, False)
pommelStrikePlus = Card("Pommel Strike+", 1, CardType.ATTACK, pommel_strike_plus_fx, Target.SINGLE, False)
shrugItOffPlus = Card("Shrug it off+", 1, CardType.SKILL, shrug_it_off_plus_fx, Target.SELF, False)
thunderclapPlus = Card("Thunderclap+", 1, CardType.ATTACK, thunderclap_plus_fx, Target.ALL, False)
trueGritPlus = Card("True Grit+", 1, CardType.SKILL, true_grit_plus_fx, Target.SELF, False)
twinStrikePlus = Card("Twin Strike+", 1, CardType.ATTACK, twin_strike_plus_fx, Target.SINGLE, False)
warcryPlus = Card("Warcry+", 0, CardType.SKILL, warcry_plus_fx, Target.SELF, True)
wildStrikePlus = Card("Wild Strike+", 1, CardType.ATTACK, wild_strike_plus_fx, Target.SINGLE, False)
battleTrancePlus = Card("Battle Trance+", 0, CardType.SKILL, battle_trance_plus_fx, Target.SELF, False)

# TODO: Counter for number of times we've taken damage
bloodForBloodPlus = Card("Blood for Blood+", 3, CardType.SKILL, blood_for_blood_plus_fx, Target.SINGLE, False)

bloodLettingPlus = Card("Bloodletting+", 0, CardType.SKILL, bloodletting_plus_fx, Target.SELF, False)
burningPactPlus = Card("Burning Pact+", 1, CardType.SKILL, burning_pact_plus_fx, Target.SELF, False)
carnagePlus = Card("Carnage+", 2, CardType.ATTACK, carnage_plus_fx, Target.SINGLE, False)
combustPlus = Card("Combust+", 1, CardType.POWER, combust_plus_fx, Target.SELF, False)
corruptionPlus = Card("Corruption+", 2, CardType.POWER, corruption_plus_fx, Target.SELF, False)
disarmPlus = Card("Disarm+", 1, CardType.SKILL, disarm_plus_fx, Target.SINGLE, True)
dropkickPlus = Card("Dropkick+", 1, CardType.ATTACK, dropkick_plus_fx, Target.SINGLE, False)
dualWieldPlus = Card("Dual Wield+", 0, CardType.SKILL, dual_wield_plus_fx, Target.SELF, False)
entrenchPlus = Card("Entrench+", 1, CardType.SKILL, entrench_plus_fx, Target.SELF, False)
evolvePlus = Card("Evolve+", 1, CardType.POWER, evolve_plus_fx, Target.SELF, False)

feelNoPainPlus = Card("Feel No Pain+", 1, CardType.POWER, feel_no_pain_plus_fx, Target.SELF, False)
flameBarrierPlus = Card("Flame Barrier+", 2, CardType.SKILL, flame_barrier_plus_fx, Target.SELF, False)
ghostlyArmorPlus = Card("Ghostly Armor+", 1, CardType.SKILL, ghostly_armor_plus_fx, Target.SELF, False)
hemoKinesisPlus = Card("Hemokinesis+", 1, CardType.ATTACK, hemokinesis_plus_fx, Target.SINGLE, False)
inflamePlus = Card("Inflame+", 1, CardType.POWER, inflame_plus_fx, Target.SELF, False)
intimidatePlus = Card("Intimidate+", 0, CardType.SKILL, intimidate_plus_fx, Target.ALL, True)
metallicizePlus = Card("Metallicize+", 1, CardType.POWER, metallicize_plus_fx, Target.SELF, False)
powerThroughPlus = Card("Power Through+", 1, CardType.SKILL, power_through_plus_fx, Target.SELF, False)
pummelPlus = Card("Pummel+", 1, CardType.ATTACK, pummel_plus_fx, Target.SINGLE, True)
ragePlus = Card("Rage+", 0, CardType.SKILL, rage_plus_fx, Target.SELF, False)

rampagePlus = Card("Rampage+", 1, CardType.ATTACK, rampage_plus_fx, Target.SINGLE, False)
recklessChargePlus = Card("Reckless Charge+", 0, CardType.ATTACK, reckless_charge_plus_fx, Target.SINGLE, False)
rupturePlus = Card("Rupture+", 0, CardType.POWER, rupture_plus_fx, Target.SELF, False)
searingBlowPlus = Card("Searing Blow+", 2, CardType.ATTACK, searing_blow_plus_fx, Target.SINGLE, False)
secondWindPlus = Card("Second Wind+", 1, CardType.SKILL, second_wind_plus_fx, Target.SELF, False)
seeingRedPlus = Card("Seeing Red+", 0, CardType.SKILL, seeing_red_plus_fx, Target.SELF, True)
severSoulPlus = Card("Sever Soul+", 2, CardType.ATTACK, sever_soul_plus_fx, Target.SINGLE, False)
shockwavePlus = Card("Shock Wave+", 2, CardType.SKILL, shockwave_plus_fx, Target.ALL, True)
spotWeaknessPlus = Card("Spot Weakness+", 1, CardType.SKILL, spot_weakness_plus_fx, Target.SINGLE, False)
uppercutPlus = Card("Uppercut+", 2, CardType.ATTACK, uppercut_plus_fx, Target.SINGLE, False)

whirlwindPlus = Card("Whirlwind+", 1, CardType.ATTACK, whirlwind_plus_fx, Target.ALL, False)
barricadePlus = Card("Barricade+", 2, CardType.SKILL, barricade_plus_fx, Target.SELF, False)
berserkPlus = Card("Berserk+", 0, CardType.POWER, berserk_plus_fx, Target.SELF, False)
bludgeonPlus = Card("Bludgeon+", 3, CardType.ATTACK, bludgeon_plus_fx, Target.SINGLE, False)
brutalityPlus = Card("Brutality+", 0, CardType.POWER, brutality_plus_fx, Target.SELF, False)
darkEmbracePlus = Card("Dark Embrace+", 1, CardType.POWER, dark_embrace_plus_fx, Target.SELF, False)
demonFormPlus = Card("Demon Form+", 3, CardType.POWER, demon_form_plus_fx, Target.SELF, False)
doubleTapPlus = Card("Double Tap+", 1, CardType.SKILL, double_tap_plus_fx, Target.SELF, False)
exhumePlus = Card("Exhume+", 0, CardType.SKILL, exhume_plus_fx, Target.SELF, True)
feedPlus = Card("Feed+", 1, CardType.ATTACK, feed_plus_fx, Target.SINGLE, False)

fiendFirePlus = Card("Fiend Fire+", 2, CardType.ATTACK, fiend_fire_plus_fx, Target.SINGLE, True)
immolatePlus = Card("Immolate+", 2, CardType.ATTACK, immolate_plus_fx, Target.ALL, False)
imperviousPlus = Card("Impervious+", 2, CardType.SKILL, impervious_plus_fx, Target.SELF, True)
juggernautPlus = Card("Juggernaut+", 2, CardType.POWER, juggernaut_plus_fx, Target.SELF, False)
limitBreakPlus = Card("Limit Break+", 1, CardType.SKILL, limit_break_plus_fx, Target.SELF, True)
offeringPlus = Card("Offering+", 0, CardType.SKILL, offering_plus_fx, Target.SINGLE, True)
reaperPlus = Card("Reaper+", 2, CardType.ATTACK, reaper_plus_fx, Target.ALL, True)
sentinelPlus = Card("Sentinel+", 1, CardType.SKILL, sentinel_plus_fx, Target.SELF, False)

dazed = Card("Dazed", 0, CardType.STATUS, status_fx, Target.SELF, False)
wound = Card("Wound", 0, CardType.STATUS, status_fx, Target.SELF, False)
burn = Card("Burn", 0, CardType.STATUS, status_fx, Target.SELF, False)

UPGRADE_DICT = generate_upgrade_dictionary()
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
