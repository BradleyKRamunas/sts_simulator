import collections
import random
import math
from combat import *
import numpy
import types


class Algorithm:
    def __init__(self, discount, featureExtractor, temp_mdp):

        # Actions is a function where actions(state) returns a list of actions one can take at that state.
        self.mdp = temp_mdp

        # Discount TBD
        self.discount = discount

        # Features and stuff TBD
        self.feature_extractor = featureExtractor

        # Weights TBD alongside features
        self.weights = collections.defaultdict(float)

        # This is useful for storing how many times we've stepped forward one state
        self.numIters = 0

    # Return the Q function associated with the weights and features
    def getQ(self, state, action):
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

    # Call this function to get the step size to update the weights.
    # We... may want to change this, although we may not?
    def getStepSize(self):
        # return 1.0 / (1 + math.sqrt(self.numIters))
        # Just return a constant of some sort
        return 0.00001

    # Baseline policy: randomly play a card with probability epsilon, or attack with the card
    # that does the most damage.
    def generic_policy(self, state, epsilon1):
        # 1 for random, 0 for greedy. Un-define it for a spectrum.
        epsilon = 1
        if state is not None and state.state_type == StateType.NORMAL_COMBAT and random.uniform(0, 1) > epsilon:
            actions = self.mdp.generate_actions(state)
            max_action = None
            max_delta = 0
            prev_sum = 0
            for enemy in state.enemies:
                prev_sum += enemy.block
                prev_sum += enemy.health

            for action in actions:
                next_state, reward = self.mdp.generate_successor_state(state, action, False)
                new_sum = 0
                if next_state is not None and not isinstance(next_state, int):

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

            return max_action

        else:
            # Otherwise, generate a random non-invalid action
            successorState = None
            action = None
            actions = self.mdp.generate_actions(state)
            while successorState is None:
                action = random.choice(actions)
                # action = actions[0]
                successorState, reward = self.mdp.generate_successor_state(state, action, False)
                if successorState is None:
                    actions.remove(action)
            return action

    # Sort of epsilon greedy right now... we'll probably change this.
    # Here's where we get to loop through all the successor states and see which generates the greatest Q_opt
    def q_learning_action(self, state, epsilon):
        actions = self.mdp.generate_actions(state)
        self.numIters += 1
        action = None
        successorState = None

        # Epsilon = probability of exploration
        if random.random() <= epsilon:
            while successorState is None:
                action = random.choice(actions)
                successorState, reward = self.mdp.generate_successor_state(state, action, False)
                if successorState is None:
                    actions.remove(action)
        else:
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
                        vEst = self.getQ(successorState, a)
                        if vEst > bestVOpt:
                            bestVOpt = vEst
                            action = a

                # action = max((self.getQ(state, action), action) for action in actions)[1]
                # successorState, reward = self.mdp.generate_successor_state(state, action)
                # if successorState is None:
                    # actions.remove(action)
        return action

    # Performs weights = weights + k * features (for sparse vectors weights (dictionary) and features (list))
    def increment(self, weights, features, k):
        for featureTwo in features:
            if featureTwo[0] in weights:
                weights[featureTwo] += k * features[featureTwo]
            else:
                weights[featureTwo] = k * features[featureTwo]

    # Performs incorporating feedback for every (state, action, reward, state') tuple whenever we choose
    # an action during Q-learning.
    def incorporateFeedback(self, state, action, reward, newState):

        # Eta computed using the inverse square root weight method
        eta = self.getStepSize()

        # Grab the current estimate of Q_opt
        qOptCur = self.getQ(state, action)

        # Assume end state
        vOptNextState = 0

        # If new state is None or an end combat state, we don't have Vopts for our "next state" (no next state)
        if newState is not None and (not isinstance(newState, int)):
            # Grab the estimated V_opt of the new state
            try:
                vOptNextState = max(self.getQ(newState, newAction) for newAction in self.mdp.generate_actions(newState))
            except ValueError:
                print newState
                print self.mdp.generate_actions(newState)

        # Probably this (to debug, check qOptCur before and after)
        coefficient = - eta * (qOptCur - (reward + self.discount * vOptNextState))

        # print coefficient
        # print self.weights
        # print "incrementing"
        self.increment(self.weights, self.feature_extractor(state, action), coefficient)

        # Normalize our weight vector
        # self.normalize()

        # print self.weights

    def normalize(self):
        sum = 0.0
        for key in self.weights:
            sum += abs(self.weights[key])
        if sum > 0:
            for key in self.weights:
                self.weights[key] /= sum