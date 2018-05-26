import combat
import cards
import random
import player
from enemy_ai import *
from enums import *
from copy import deepcopy

'''
--OUR MODEL--
States: Instances of Combat
Actions: Card to use
Successor: generate_successor_state
T(s,a,s') Probability: 1 for all
IsEnd(s): is_end_state
'''

EPSILON = 0.5


def generic_policy(state, actions):
    if state.state_type == StateType.NORMAL:
        if random.uniform(0, 1) <= EPSILON:
            max_action = None
            max_delta = 0
            prev_sum = 0
            for enemy in state.enemies:
                prev_sum += enemy.block
                prev_sum += enemy.health

            for action in actions:
                next_state = generate_successor_state(state, action)
                new_sum = 0
                if next_state is not None:
                    for enemy in next_state.enemies:
                        new_sum += enemy.block
                        new_sum += enemy.health
                    if prev_sum - new_sum > max_delta:
                        max_action = action
                        max_delta = prev_sum - new_sum

            return max_action
        else:
            action = random.choice(actions)
            next_state = generate_successor_state(state, action)
            if next_state is None:
                return None
            return action
    else:
        return random.choice(actions)


def is_end_state(state):
    if state is None:
        return False
    if state.player.health == 0:
        return True
    for enemy in state.enemies:
        if enemy.health > 0:
            return False
    return True


def generate_successor_state(state, action):
    temp_state = deepcopy(state)
    if state.state_type == StateType.NORMAL:
        if action is None:
            temp_state.end_turn()
            temp_state.start_turn()
        else:
            card, target = action
            if not temp_state.player.deck.use_card(card, target):
                return None
        return temp_state
    if state.state_type == StateType.COPY:
        if action is not None:
            temp_state.player.deck.hand.append(action)
        temp_state.state_type = StateType.NORMAL
        return temp_state
    if state.state_type == StateType.DISCARD_TO_DRAW:
        if action is not None:
            temp_state.player.deck.draw_pile.insert(0, action)
            temp_state.player.deck.discard_pile.remove(action)
        temp_state.state_type = StateType.NORMAL
        return temp_state
    if state.state_type == StateType.EXHAUST_TO_HAND:
        if action is not None:
            temp_state.player.deck.hand.append(action)
            temp_state.player.deck.exhaust_pile.remove(action)
        temp_state.state_type = StateType.NORMAL
        return temp_state
    if state.state_type == StateType.HAND_TO_DRAW:
        if action is not None:
            temp_state.player.deck.draw_pile.insert(0, action)
            temp_state.player.deck.hand.remove(action)
        temp_state.state_type = StateType.NORMAL
        return temp_state
    if state.state_type == StateType.HAND_TO_EXHAUST:
        if action is not None:
            temp_state.player.deck.exhaust_card(action)
        temp_state.state_type = StateType.NORMAL
        return temp_state


def generate_actions(state):
    if state is None:
        return None
    actions = []
    if state.state_type == StateType.NORMAL:
        for card in state.player.deck.hand:
            if card.target_type == Target.SELF:
                actions.append((card, -1))
            if card.target_type == Target.SINGLE:
                for target, enemy in enumerate(state.enemies):
                    if enemy.health > 0:
                        actions.append((card, target))
            if card.target_type == Target.ALL:
                actions.append((card, 0))
        actions.append(None)
    if state.state_type == StateType.COPY:
        for card in state.player.deck.hand:
            if card.card_type == CardType.ATTACK:
                actions.append(card)
        if len(actions) == 0:
            actions.append(None)
    if state.state_type == StateType.DISCARD_TO_DRAW:
        if len(state.player.deck.discard_pile) == 0:
            actions.append(None)
        for card in state.player.deck.discard_pile:
            actions.append(card)
    if state.state_type == StateType.EXHAUST_TO_HAND:
        if len(state.player.deck.exhaust_pile) == 0:
            actions.append(None)
        for card in state.player.deck.exhaust_pile:
            actions.append(card)
    if state.state_type == StateType.HAND_TO_DRAW:
        if len(state.player.deck.hand) == 0:
            actions.append(None)
        for card in state.player.deck.hand:
            actions.append(card)
    if state.state_type == StateType.HAND_TO_EXHAUST:
        if len(state.player.deck.hand) == 0:
            actions.append(None)
        for card in state.player.deck.hand:
            actions.append(card)

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
    actor = player.Player(cards.testing_deck(), 800)
    enemies = [combat.CombatEnemy(None, SpikeSlimeAI(), 1000), combat.CombatEnemy(None, AcidSlimeAI(), 1000)]
    current_state = combat.Combat(actor, enemies)
    current_state.start_turn()
    while not is_end_state(current_state):
        current_state.print_information()
        actions = generate_actions(current_state)
        action = generic_policy(current_state, actions)
        print "\tDoing action: ",
        print action
        print
        current_state = generate_successor_state(current_state, action)
        current_state.print_information()


if __name__ == '__main__':
    run()
