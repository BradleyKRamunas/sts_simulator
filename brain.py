import random

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
        return action

    def random_action(self, state):
        successorState = None
        action = None
        actions = self.mdp.generate_actions(state)
        while successorState is None:
            # action = random.choice(actions)
            action = actions[0]
            successorState, reward = self.mdp.generate_successor_state(state, action, False)
            if successorState is None:
                actions.remove(action)
        return action
