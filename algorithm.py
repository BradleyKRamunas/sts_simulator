import collections
import random
import math


class Algorithm:
    def __init__(self, discount, actionGenerator, featureExtractor, explorationProb=0.2):

        # Actions is a function where actions(state) returns a list of actions one can take at that state.
        self.actions = actionGenerator

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

    # Sort of epsilon greedy right now... we'll probably change this.
    # Here's where we get to loop through all the successor states and see which generates the greatest Q_opt
    def getAction(self, state):
        self.numIters += 1
        if random.random() < self.explorationProb:
            return random.choice(self.actions(state))
        else:
            return max((self.getQ(state, action), action) for action in self.actions(state))[1]

    # Call this function to get the step size to update the weights.
    # We... may want to change this, although we may not?
    def getStepSize(self):
        return 1.0 / (1 + math.sqrt(self.numIters))

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
        if newState is not None:
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