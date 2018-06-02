from enums import *
from copy import deepcopy
import random
import cards
import player
import combat
from enemy_ai import *
from rest_site import RestSite
from random_event import RandomEvent

class STSMDP:

    def __init__(self):
        self.combat_count = 0
        self.easy_enemies = [[combat.CombatEnemy(None, SpikeSlimeAI(), 12), combat.CombatEnemy(None, AcidSlimeAI(), 15)],
                             [combat.CombatEnemy(None, JawWormAI(), 30)], [combat.CombatEnemy(None, FungiBeastAI(), 24),
                                                                           combat.CombatEnemy(None, FungiBeastAI(), 25)],
                             [combat.CombatEnemy(None, SlaverAI(), 34)]]
        self.common_cards = cards.generate_common_cards()
        self.uncommon_cards = cards.generate_uncommon_cards()
        self.rare_cards = cards.generate_rare_cards()
        self.upgrade_list = cards.generate_upgrade_dictionary()

    def start_state(self):
        actor = player.Player(cards.generate_default_deck(), 80)
        enemies = random.choice(self.easy_enemies)
        start_state = combat.Combat(actor, enemies)
        return start_state

    def is_end_state(self, state):
        if isinstance(state, int):
            return True
        else:
            return False

    def get_enemy_encounter(self):
        # TODO: implement tiers via combat_count
        return random.choice(self.easy_enemies)

    def generate_successor_state(self, state, action, real):
        temp_state = deepcopy(state)
        reward = 0
        if state.state_type == StateType.NORMAL_COMBAT:
            if action is None:
                temp_state.end_turn()
                temp_state.start_turn()
            else:
                card, target = action
                if not temp_state.player.deck.use_card(card, target):
                    return (None, 0)
            dead_enemies = True
            for enemy in temp_state.enemies:
                if enemy.health > 0:
                    dead_enemies = False
                    break

            # If we've lost this combat/game
            if temp_state.player.health <= 0:
                return (0, -1000)

            # If we've won this combat...
            if dead_enemies:

                # Only increment combat_count if we've won a real combat
                if real:
                    self.combat_count += 1

                # 10 wins = win game!
                if self.combat_count >= 10:
                    return (1, 1000)

                # Else, we have some probability of going to a number of different events.
                probability = random.uniform(0, 1)
                temp_state.nc_player.health = temp_state.player.health
                temp_state.nc_player.max_health = temp_state.player.max_health

                next_state = RandomEvent(deepcopy(temp_state.nc_player))
                next_state.state_type = StateType.ADD_CARD

                # Our reward is how much health we had left at the end of this combat
                return(next_state, next_state.player.health)
            else:
                return (temp_state, 0)
        if state.state_type == StateType.COPY:
            if action is not None:
                temp_state.player.deck.hand.append(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return (temp_state, 0)
        if state.state_type == StateType.DISCARD_TO_DRAW:
            if action is not None:
                temp_state.player.deck.draw_pile.insert(0, action)
                temp_state.player.deck.discard_pile.remove(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return (temp_state, 0)
        if state.state_type == StateType.EXHAUST_TO_HAND:
            if action is not None:
                temp_state.player.deck.hand.append(action)
                temp_state.player.deck.exhaust_pile.remove(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return (temp_state, 0)
        if state.state_type == StateType.HAND_TO_DRAW:
            if action is not None:
                temp_state.player.deck.draw_pile.insert(0, action)
                temp_state.player.deck.hand.remove(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return (temp_state, 0)
        if state.state_type == StateType.HAND_TO_EXHAUST:
            if action is not None:
                temp_state.player.deck.exhaust_card(action)
            temp_state.state_type = StateType.NORMAL_COMBAT
            return (temp_state, 0)
        if state.state_type == StateType.UPGRADE:
            if action is not None and action.card_type != CardType.STATUS:
                temp_state.player.deck.hand.remove(action)
                temp_state.player.deck.hand.append(self.upgrade_list[action.name])
            temp_state.state_type = StateType.NORMAL_COMBAT
            return (temp_state, 0)
        if state.state_type == StateType.NORMAL_REST:
            if action == 0:
                temp_state.heal()
                probability = random.uniform(0, 1)
                if probability <= 0.2:
                    # go to rest
                    next_state = RestSite(deepcopy(temp_state.player))
                    return (next_state, 0)
                elif probability <= 0.4:
                    # go to a random event
                    next_state = RandomEvent(deepcopy(temp_state.player))
                    return (next_state, 0)
                else:
                    # go to a combat
                    next_state = combat.Combat(deepcopy(temp_state.player), self.get_enemy_encounter())
                    return (next_state, 0)
            else:
                temp_state.state_type = StateType.UPGRADE_REST
                return (temp_state, 0)
        if state.state_type == StateType.UPGRADE_REST:
            if action is not None:
                upgraded_card = self.upgrade_list[action.name]
                temp_state.player.deck.remove_card(action)
                temp_state.player.deck.add_card(upgraded_card)
            probability = random.uniform(0, 1)
            if probability <= 0.2:
                # go to rest
                next_state = RestSite(deepcopy(temp_state.player))
                return (next_state, 0)
            elif probability <= 0.3:
                # go to a random event
                next_state = RandomEvent(deepcopy(temp_state.player))
                return (next_state, 0)
            else:
                # go to a combat
                next_state = combat.Combat(deepcopy(temp_state.player), self.get_enemy_encounter())
                return (next_state, 0)
        if state.state_type == StateType.NORMAL_RANDOM:
            if temp_state.generate_random_event():
                probability = random.uniform(0, 1)
                if probability <= 0.1:
                    # go to rest
                    next_state = RestSite(deepcopy(temp_state.player))
                    return (next_state, 0)
                elif probability <= 0.2:
                    # go to a random event
                    next_state = RandomEvent(deepcopy(temp_state.player))
                    return (next_state, 0)
                else:
                    next_state = combat.Combat(deepcopy(temp_state.player), self.get_enemy_encounter())
                    return (next_state, 0)
            else:
                return (temp_state, 0)
        if state.state_type == StateType.REMOVE_CARD:
            if action is not None:
                temp_state.player.deck.remove_card(action)
            probability = random.uniform(0, 1)
            if probability <= 0.1:
                # go to rest
                next_state = RestSite(deepcopy(temp_state.player))
                return (next_state, 0)
            elif probability <= 0.2:
                # go to a random event
                next_state = RandomEvent(deepcopy(temp_state.player))
                return (next_state, 0)
            else:
                next_state = combat.Combat(deepcopy(temp_state.player), self.get_enemy_encounter())
                return (next_state, 0)
        if state.state_type == StateType.ADD_CARD:
            if action is not None:
                temp_state.player.deck.add_card(action)
            probability = random.uniform(0, 1)
            if probability <= 0.1:
                # go to rest
                next_state = RestSite(deepcopy(temp_state.player))
                return (next_state, 0)
            elif probability <= 0.2:
                # go to a random event
                next_state = RandomEvent(deepcopy(temp_state.player))
                return (next_state, 0)
            else:
                next_state = combat.Combat(deepcopy(temp_state.player), self.get_enemy_encounter())
                return (next_state, 0)


    def generate_actions(self, state):
        if state is None:
            return [None]
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
        if state.state_type == StateType.UPGRADE:
            if len(state.player.deck.hand) == 0:
                actions.append(None)
            for card in state.player.deck.hand:
                if not card.upgraded:
                    actions.append(card)
        if state.state_type == StateType.NORMAL_REST:
            actions.append(0)  # corresponding to rest
            actions.append(1)  # corresponding to upgrade
        if state.state_type == StateType.UPGRADE_REST:
            for card in state.player.deck.cards:
                if not card.upgraded:
                    actions.append(card)
            if len(actions) == 0:
                actions.append(None)
        if state.state_type == StateType.NORMAL_RANDOM:
            actions.append(None)
        if state.state_type == StateType.REMOVE_CARD:
            for card in state.player.deck.cards:
                actions.append(card)
            if len(actions) == 0:
                actions.append(None)
        if state.state_type == StateType.ADD_CARD:
            count = 0
            # actions.append(None)
            while count <= 2:
                value = random.uniform(0, 1)
                if value <= 0.1:
                    actions.append(random.choice(self.rare_cards))
                    count += 1
                elif value <= 0.35:
                    actions.append(random.choice(self.uncommon_cards))
                    count += 1
                elif value <= 1:
                    actions.append(random.choice(self.common_cards))
                    count += 1
        return actions
