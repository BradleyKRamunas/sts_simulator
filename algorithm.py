import collections
import random
import math
from combat import *


class Algorithm:
    def __init__(self, discount, featureExtractor, temp_get_action, temp_mdp, explorationProb = 0.2):

        # Actions is a function where actions(state) returns a list of actions one can take at that state.
        self.mdp = temp_mdp

        # getAction is a function that takes in a state, and returns which action to play.
        self.getAction = temp_get_action

        # Discount TBD
        self.discount = discount

        # Features and stuff TBD
        self.featureExtractor = featureExtractor

        # ExplorationProb changer TBD as well
        self.explorationProb = explorationProb

        # Weights TBD alongside features
        self.weights = collections.defaultdict(float)

        # This is useful for storing how many times we've stepped forward one state
        self.numIters = 0

    # Return the Q function associated with the weights and features
    def getQ(self, state, action):
        score = 0
        for f, v in self.featureExtractor(state, action):
            score += self.weights[f] * v
        return score

    # Call this function to get the step size to update the weights.
    # We... may want to change this, although we may not?
    def getStepSize(self):
        return 1.0 / (1 + math.sqrt(self.numIters))

    # Baseline policy: randomly play a card with probability 0.5, or attack with the card
    # that does the most damage.
    def generic_policy(self, state):
        epsilon = 0.5
        if state.state_type == StateType.NORMAL_COMBAT:
            actions = self.mdp.generate_actions(state)
            if random.uniform(0, 1) <= epsilon:
                max_action = None
                max_delta = 0
                prev_sum = 0
                for enemy in state.enemies:
                    prev_sum += enemy.block
                    prev_sum += enemy.health

                for action in actions:
                    next_state, reward = self.mdp.generate_successor_state(state, action)
                    new_sum = 0
                    if next_state is not None and next_state.state_type == StateType.NORMAL_COMBAT:
                        for enemy in next_state.enemies:
                            new_sum += enemy.block
                            new_sum += enemy.health
                        if prev_sum - new_sum > max_delta:
                            max_action = action
                            max_delta = prev_sum - new_sum

                return max_action
            else:
                action = random.choice(actions)
                next_state = self.mdp.generate_successor_state(state, action)
                if next_state is None:
                    return None
                return action
        else:
            return random.choice(self.mdp.generate_actions(state))

    # Sort of epsilon greedy right now... we'll probably change this.
    # Here's where we get to loop through all the successor states and see which generates the greatest Q_opt
    def getAction(self, state):
        actions = self.mdp.generate_actions(state)
        self.numIters += 1
        if random.random() < self.explorationProb:
            return random.choice(actions)
        else:
            return max((self.getQ(state, action), action) for action in actions)[1]

    # Performs weights = weights + k * features (for sparse vectors weights (dictionary) and features (list))
    def increment(self, weights, features, k):
        for featureTwo in features:
            if featureTwo[0] in weights:
                weights[featureTwo[0]] += k * featureTwo[1]
            else:
                weights[featureTwo[0]] = k * featureTwo[1]

    # We will call this function with (s, a, r, s'), which you should use to update |weights|.
    # Note that if s is a terminal state, then s' will be None.  Remember to check for this.
    # You should update the weights using self.getStepSize(); use
    # self.getQ() to compute the current estimate of the parameters.
    def incorporateFeedback(self, state, action, reward, newState):

        # Eta computed using the inverse square root weight method
        eta = self.getStepSize()

        # Grab the current estimate of Q_opt
        qOptCur = self.getQ(state, action)

        # Assume end state
        vOptNextState = 0

        # If new state is None, then our reward is 0.
        if newState is not (None or True or False):
            # Grab the estimated V_opt of the new state
            vOptNextState = max(self.getQ(newState, newAction) for newAction in self.actions(newState))

        coefficient = (1.0 - eta) * qOptCur + eta * (reward + self.discount * vOptNextState)

        self.increment(self.weights, self.featureExtractor(state, action), coefficient)


"""def simulate_QL_over_MDP(mdp, featureExtractor):
    # NOTE: adding more code to this function is totally optional, but it will probably be useful
    # to you as you work to answer question 4b (a written question on this assignment).  We suggest
    # that you add a few lines of code here to run value iteration, simulate Q-learning on the MDP,
    # and then print some stats comparing the policies learned by these two approaches.
    # BEGIN_YOUR_CODE
    qlearn = QLearningAlgorithm(mdp.actions, mdp.discount(), featureExtractor)
    util.simulate(mdp, qlearn, 30000)
    qlearn.explorationProb = 0
    mdp.computeStates()
    allStates = mdp.states

    vi = util.ValueIteration()
    vi.solve(mdp)
    vi_policy = vi.pi

    qlearnPolicy = {}
    for state in allStates:
        qlearnPolicy[state] = qlearn.getAction(state)

    total = 0.0
    sameCounter = 0
    for state in vi_policy:
        if vi_policy[state] == qlearnPolicy[state]:
            sameCounter += 1
        total += 1

    print("total: {}, sameCounter: {}, percentage: {}".format(total, sameCounter, sameCounter / total))

    # END_YOUR_CODE
"""