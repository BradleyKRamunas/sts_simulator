import random
import cards
from combat import StateType
from collections import defaultdict

class Brain:
    def __init__(self, discount, feature_extractor, temp_mdp, weights):

        # Actions is a function where actions(state) returns a list of actions one can take at that state.
        self.mdp = temp_mdp

        # Discount TBD
        self.discount = discount

        # Features and stuff TBD
        self.feature_extractor = feature_extractor

        # Grabbing weights we've already learned
        self.weights = weights

        # Trying to see if there's a strategy going on
        # self.action_count = defaultdict(int)

    # Return the value associated with the weights and features
    def get_v(self, state, action):
        score = 0
        # If state is None, the action we tried taking was illegal
        # If state is an int, we've either won the game or lost the game.
        if state is not None:
            if isinstance(state, int):
                return 1000 if state == 1 else -1000
            features = self.feature_extractor(state, action)
            for f in features.keys():
                score += self.weights[f] * features[f]
        return score

    # When we do this, we assume we already have a Q_opt set and strictly try and exploit.
    def q_learning_test(self, state):
        actions = self.mdp.generate_actions(state)
        action = None
        successorState = None

        while successorState is None:
            bestVOpt = -10000000
            action = None
            for a in actions:
                successorState, reward = self.mdp.generate_successor_state(state, a, False)
                if successorState is None:
                    actions.remove(a)
                else:
                    # We're really only taking successorState into account here; the action is the prev action.
                    # Else there's too many possibilities to loop through - we have to go through all actions of the new state too.
                    vEst = self.get_v(successorState, a)
                    if vEst > bestVOpt:
                        bestVOpt = vEst
                        action = a
        # self.action_count[action] += 1
        return action

    def random_action(self, state):
        successorState = None
        action = None
        actions = self.mdp.generate_actions(state)
        while successorState is None:
            try:
                # action = random.choice(actions) # Grabs a completely random action
                action = actions[0] # Always tries the first action available
            except IndexError:
                print state.state_type
                state.print_information()
            successorState, reward = self.mdp.generate_successor_state(state, action, False)
            if successorState is None:
                actions.remove(action)

        # self.action_count[action] += 1
        return action

    # Greedy baseline: Always picks the card that does the most damage in combat, or random otherwise.
    def greedy_baseline(self, state):
        if state is not None and state.state_type == StateType.NORMAL_COMBAT:
            actions = self.mdp.generate_actions(state)
            max_action = actions[0]
            max_delta = 0
            prev_sum = 0
            for enemy in state.enemies:
                prev_sum += enemy.block
                prev_sum += enemy.health

            for action in actions:
                next_state, reward = self.mdp.generate_successor_state(state, action, False)
                new_sum = 0
                if next_state is not None:
                    if isinstance(next_state, int):
                        return (cards.strike, -1)
                    # If we're still in a combat, consider the next states.
                    if next_state.state_type == StateType.NORMAL_COMBAT:
                        for enemy in next_state.enemies:
                            new_sum += enemy.block
                            new_sum += enemy.health
                        # If we've won a combat and instantly entered a new one
                        if prev_sum - new_sum < 0:
                            max_action = action
                            break
                        elif prev_sum - new_sum > max_delta:
                            max_action = action
                            max_delta = prev_sum - new_sum
                    else:
                        # We got out of combat, which means we probably won the fight, so take that action.
                        max_action = action
                        break
            if self.mdp.generate_successor_state(state, max_action, False)[0] is None:
                return self.random_action(state)
            else:
                return max_action
        else:
            return self.random_action(state)