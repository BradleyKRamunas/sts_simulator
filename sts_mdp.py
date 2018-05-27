from enums import *
from copy import deepcopy
import random
import cards
import player
import combat
from enemy_ai import *

class STSMDP:

    def __init__(self):
        self.combat_count = 0
        self.easy_enemies = [[combat.CombatEnemy(None, SpikeSlimeAI(), 12), combat.CombatEnemy(None, AcidSlimeAI(), 15)],
                             [combat.CombatEnemy(None, JawWormAI(), 30)], [combat.CombatEnemy(None, FungiBeastAI(), 24),
                                                                           combat.CombatEnemy(None, FungiBeastAI(), 25)],
                             [combat.CombatEnemy(None, SlaverAI(), 34)]]

    def start_state(self):
        actor = player.Player(cards.generate_default_deck(), 80)
        enemies = random.choice(self.easy_enemies)
        start_state = combat.Combat(actor, enemies)
        return start_state

    def is_end_state(self, state):
        if self.combat_count >= 10:
            return True
        else:
            return False


    def generate_successor_state(self, state, action):
        temp_state = deepcopy(state)
        if state.state_type == StateType.NORMAL_COMBAT:
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
            temp_state.state_type = StateType.NORMAL_COMBAT
            return temp_state
        if state.state_type == StateType.DISCARD_TO_DRAW:
            if action is not None:
                temp_state.player.deck.draw_pile.insert(0, action)
                temp_state.player.deck.discard_pile.remove(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return temp_state
        if state.state_type == StateType.EXHAUST_TO_HAND:
            if action is not None:
                temp_state.player.deck.hand.append(action)
                temp_state.player.deck.exhaust_pile.remove(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return temp_state
        if state.state_type == StateType.HAND_TO_DRAW:
            if action is not None:
                temp_state.player.deck.draw_pile.insert(0, action)
                temp_state.player.deck.hand.remove(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return temp_state
        if state.state_type == StateType.HAND_TO_EXHAUST:
            if action is not None:
                temp_state.player.deck.exhaust_card(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return temp_state


    def generate_actions(self, state):
        if state is None:
            return None
        actions = []
        if state.state_type == StateType.NORMAL_COMBAT:
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