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
        state.end_turn()
        state.start_turn()
    else:
        card, target = action
        state.player.deck.use_card(card, target)
    return state

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
    return

def run():
    player = main.Player(cards.generate_default_deck(), 80)
    enemy_ai = main.GoblinAI()
    enemy = main.CombatEnemy(None, enemy_ai, 30)
    combat = main.Combat(player, [enemy])


if __name__ == '__main__':
    run()
