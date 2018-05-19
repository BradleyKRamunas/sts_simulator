import main
import cards

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
    if action == None:
        return None
    else:
        state.player.deck.use_card(action)
        return state

def generate_actions(state):
    actions = []
    energy = state.player.energy
    for card in state.player.deck.hand:
        if card.cost <= energy:
            actions.append(card)
    actions.append(None)
    return actions

def state_feature_extractor(state):
    #TODO: implement some sort of feature extraction
    return

def run():
    player = main.Player(cards.generate_default_deck(), 80)
    enemy_ai = main.GoblinAI()
    enemy = main.CombatEnemy(None, enemy_ai, 30)
    combat = main.Combat(player, [enemy])


if __name__ == '__main__':
    run()
