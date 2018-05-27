from algorithm import *
from combat import *
from collections import defaultdict


############################################################
def game_general_feature_extractor(state, action):

    # Features is going to be a dictionary of {key: int}
    features = defaultdict(int)

    if state.state_type == StateType.NORMAL_COMBAT:

        # Health feature
        features["health"] = state.player.health

        # Block feature
        features["block"] = state.player.block

        # Total enemy health feature, total enemy block feature, total enemy attack intent, enemy intent indicator
        # Also condition indicators/value/duration for player and enemy
        totalEnemyHP = 0
        totalEnemyAtk = 0
        totalEnemyBlock = 0
        for enemy in state.enemies:

            # If the enemy is not dead, find its intent and append it to our features
            if enemy.intent is not None:
                intent, value, status = enemy.intent
                if intent == Intent.ATTACK:
                    totalEnemyAtk += value
                elif intent == Intent.BLOCK:
                    totalEnemyBlock += value
                elif intent == Intent.BUFF:
                    features[("enemy", status)] += value
                else:
                    features[("player", status)] += value

            totalEnemyHP += enemy.health

        features["total enemy HP"] = totalEnemyHP
        features["total enemy ATK"] = totalEnemyAtk
        features["total enemy block"] = totalEnemyBlock

        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand", card.name)] = 1

        # Appends indicators for all cards in player's draw pile
        for card in state.player.deck.draw_pile:
            features[("draw", card.name)] = 1

        # Appends indicators for all cards in player's discard pile
        for card in state.player.deck.discard_pile:
            features[("discard", card.name)] = 1

        # Appends indicators for all cards in player's exhaust pile
        for card in state.player.deck.exhaust_pile:
            features[("exhausted", card.name)] = 1

    elif state.state_type == StateType.COPY:
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand", card.name)] = 1

    elif state.state_type == StateType.DISCARD_TO_DRAW:
        # Appends indicators for all cards in player's discard pile
        for card in state.player.deck.discard_pile:
            features[("discard", card.name)] = 1

    elif state.state_type == StateType.EXHAUST_TO_HAND:
        # Appends indicators for all cards in player's exhaust pile
        for card in state.player.deck.exhaust_pile:
            features[("exhausted", card.name)] = 1

    elif state.state_type == StateType.HAND_TO_DRAW:
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand", card.name)] = 1

    elif state.state_type == StateType.HAND_TO_EXHAUST:
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand", card.name)] = 1

    elif state.state_type == StateType.NORMAL_REST:
        # Grabs health and indicators for each card in player's deck
        features["health"] = state.player.health
        for card in state.player.deck.cards:
            features[card] = 1

    elif state.state_type == StateType.UPGRADE_REST:
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[card] = 1

    elif state.state_type == StateType.REMOVE_CARD:
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[card] = 1

    elif state.state_type == StateType.ADD_CARD:
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[card] = 1

    # else state.state_type == StateType.NORMAL_RANDOM: no features


"""# Return a single-element list containing a binary (indicator) feature
# for the existence of the (state, action) pair.  Provides no generalization.
def identityFeatureExtractor(state, action):
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]"""

############################################################
# Perform |numTrials| of the following:
# Each trial will run for at most |maxIterations|.
# Return the list of rewards that we get for each trial.
def simulate(mdp, numTrials=10, maxIterations=1000, verbose=False, action_gen_type = 0):

    # (discount, actionGenerator, featureExtractor, explorationProb=0.2)
    # This creates our actual function approximation (based off q-learning) algorithm
    function_approx = Algorithm(1, mdp.generate_actions, game_general_feature_extractor, mdp)

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
            if action_gen_type == 0:
                action = function_approx.generic_policy(state)
            else:
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
