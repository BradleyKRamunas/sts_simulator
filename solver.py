import collections
import random
import algorithm


############################################################
def gameGeneralFeatureExtractor(state, action): # TODO: lol

# Return a single-element list containing a binary (indicator) feature
# for the existence of the (state, action) pair.  Provides no generalization.
def identityFeatureExtractor(state, action):
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]

############################################################
# Perform |numTrials| of the following:
# Each trial will run for at most |maxIterations|.
# Return the list of rewards that we get for each trial.
def simulate(mdp, numTrials=10, maxIterations=1000, verbose=False):


    # (discount, actionGenerator, featureExtractor, explorationProb=0.2)
    # This creates our actual function approximation (based off q-learning) algorithm
    function_approx = algorithm.Algorithm(1, mdp.generate_actions, identityFeatureExtractor) # <- identityFeatureExtractor is placeholder

    totalRewards = []  # The rewards we get on each trial

    for trial in range(numTrials):

        # Grab the start state and put it in the sequence.
        state = mdp.startState()
        sequence = [state]

        # Total Discount is 1 for now.
        totalDiscount = 1

        # Keeping track of total reward
        totalReward = 0

        while True:

            # Algorithm will pick one of its possible actions from state state to do.
            action = function_approx.getAction(state)

            # Single successor state generated (our MDP is, for all intents and purposes, well, deterministic.)
            successorState, reward = mdp.generate_successor_state(state, action)

            # Append our action and successor state to the sequence (for verbose display if needed)
            sequence.append(action)
            sequence.append(successorState)

            # Incorporate the feedback we got from state, action, reward, state'.
            function_approx.incorporateFeedback(state, action, reward, successorState)

            totalReward += totalDiscount * reward
            # totalDiscount *= mdp.discount()
            state = successorState

            # If we've hit an end state, we need to stop.
            if mdp.is_end_state(state):
                break

        if verbose:
            print "Trial %d (totalReward = %s): %s" % (trial, totalReward, sequence)

        totalRewards.append(totalReward)
    return totalRewards
