import main
import cards
from copy import deepcopy

'''
--OUR MODEL--
States: Instances of Combat
Actions: Card to use
Successor: generate_successor_state
T(s,a,s') Probability: 1 for all
IsEnd(s): is_end_state
'''

def is_end_state(state):
    if state.player.health == 0:
        return True
    for enemy in state.enemies:
        if enemy.health > 0:
            return False
    return True

def generate_successor_state(state, action):
    #TODO: handle non-determinism of drawing a card?
    temp_state = deepcopy(state)
    if action == None:
        temp_state.end_turn()
        temp_state.start_turn()
    else:
        card, target = action
        temp_state.player.deck.use_card(card, target)
    return temp_state

def generate_actions(state):
    actions = []
    energy = state.player.energy
    for card in state.player.deck.hand:
        if card.cost <= energy:
            if card.target_type == main.Target.SELF:
                actions.append((card, -1))
            if card.target_type == main.Target.SINGLE:
                for target, enemy in enumerate(state.enemies):
                    if enemy.health > 0:
                        actions.append((card, target))
            if card.target_type == main.Target.RANDOM:
                # another issue with random...
                # TODO: implement randomness, right now targets first alive enemy
                for target, enemy in enumerate(state.enemies):
                    if enemy.health > 0:
                        actions.append((card, target))
                        break
            if card.target_type == main.Target.ALL:
                actions.append((card, -1))



    actions.append(None)  # None represents ending turn
    return actions

def state_feature_extractor(state):
    #TODO: implement some sort of feature extraction

    # Sparse vector of features represented by dictionary
    features = {}

    # Grabs the health of each enemy
    for i, enemy in enumerate(state.enemies):
            features["enemy" + str(i) + "Health"] = enemy.health

    # Grabs the number of alive enemies
    aliveEnemies = 0
    for enemy in state.enemies:
        if enemy.health > 0:
            aliveEnemies += 1
    features["numEnemies"] = aliveEnemies

    # TODO: Implement enemyAI as a feature

    # TODO: Cards as features somehow (indicator list with all cards in it, singleton/pairs/triples of cards, etc.)

    #

    return

def run():
    player = main.Player(cards.generate_all_deck(), 10000)
    enemy_ai = main.GoblinAI()
    enemy = main.CombatEnemy(None, enemy_ai, 10000)
    combat = main.Combat(player, [enemy])


if __name__ == '__main__':
    run()
