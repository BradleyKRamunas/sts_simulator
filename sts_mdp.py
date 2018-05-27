from enums import *
from copy import deepcopy

class STSMDP:

    def __init__(self):
        # TODO:
        # Generate start state

    def start_state(self):
        # TODO

    def is_end_state(self, state):
        if state is None:
            return False
        if state.player.health == 0:
            return True
        for enemy in state.enemies:
            if enemy.health > 0:
                return False
        return True


    def generate_successor_state(self, state, action):
        temp_state = deepcopy(state)
        if state.state_type == CombatStateType.NORMAL:
            if action is None:
                temp_state.end_turn()
                temp_state.start_turn()
            else:
                card, target = action
                if not temp_state.player.deck.use_card(card, target):
                    return None
            return temp_state
        if state.state_type == CombatStateType.COPY:
            if action is not None:
                temp_state.player.deck.hand.append(action)
            temp_state.state_type = CombatStateType.NORMAL
            return temp_state
        if state.state_type == CombatStateType.DISCARD_TO_DRAW:
            if action is not None:
                temp_state.player.deck.draw_pile.insert(0, action)
                temp_state.player.deck.discard_pile.remove(action)
            temp_state.state_type = CombatStateType.NORMAL
            return temp_state
        if state.state_type == CombatStateType.EXHAUST_TO_HAND:
            if action is not None:
                temp_state.player.deck.hand.append(action)
                temp_state.player.deck.exhaust_pile.remove(action)
            temp_state.state_type = CombatStateType.NORMAL
            return temp_state
        if state.state_type == CombatStateType.HAND_TO_DRAW:
            if action is not None:
                temp_state.player.deck.draw_pile.insert(0, action)
                temp_state.player.deck.hand.remove(action)
            temp_state.state_type = CombatStateType.NORMAL
            return temp_state
        if state.state_type == CombatStateType.HAND_TO_EXHAUST:
            if action is not None:
                temp_state.player.deck.exhaust_card(action)
            temp_state.state_type = CombatStateType.NORMAL
            return temp_state


    def generate_actions(self, state):
        if state is None:
            return None
        actions = []
        if state.state_type == CombatStateType.NORMAL:
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
        if state.state_type == CombatStateType.COPY:
            for card in state.player.deck.hand:
                if card.card_type == CardType.ATTACK:
                    actions.append(card)
            if len(actions) == 0:
                actions.append(None)
        if state.state_type == CombatStateType.DISCARD_TO_DRAW:
            if len(state.player.deck.discard_pile) == 0:
                actions.append(None)
            for card in state.player.deck.discard_pile:
                actions.append(card)
        if state.state_type == CombatStateType.EXHAUST_TO_HAND:
            if len(state.player.deck.exhaust_pile) == 0:
                actions.append(None)
            for card in state.player.deck.exhaust_pile:
                actions.append(card)
        if state.state_type == CombatStateType.HAND_TO_DRAW:
            if len(state.player.deck.hand) == 0:
                actions.append(None)
            for card in state.player.deck.hand:
                actions.append(card)
        if state.state_type == CombatStateType.HAND_TO_EXHAUST:
            if len(state.player.deck.hand) == 0:
                actions.append(None)
            for card in state.player.deck.hand:
                actions.append(card)

        return actions