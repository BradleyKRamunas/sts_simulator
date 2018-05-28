from algorithm import *
from combat import *
from collections import defaultdict


############################################################
def game_general_feature_extractor(state, action):

    # Features is going to be a dictionary of {key: int}
    features = defaultdict(int)

    if state.state_type == StateType.NORMAL_COMBAT:

        # Allows for a constant term bias
        features["combat"] = 1

        for i in range(13):
            features[str(10 * i) + " to " + str(10 * (i + 1)) + " health"] = 1 if state.player.health >= 10 * i and state.player.health < 11 * i else 0

        # Health feature
        # features["health"] = state.player.health

        for i in range(10):
            features[str(10 * i) + " to " + str(10 * (i + 1)) + " block"] = 1 if state.player.block >= 10 * i and state.player.block < 11 * i else 0


        # Block feature
        # features["block"] = state.player.block

        # Total enemy health feature, total enemy block feature, total enemy attack intent, enemy intent indicator
        # Also condition indicators/value/duration for player and enemy
        # totalEnemyHP = 0
        # totalEnemyAtk = 0
        # totalEnemyBlock = 0
        """for enemy in state.enemies:

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
        features["total enemy block"] = totalEnemyBlock"""

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
        features["copy"] = 1
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand", card.name)] = 1

    elif state.state_type == StateType.DISCARD_TO_DRAW:
        features["discardToDraw"] = 1
        # Appends indicators for all cards in player's discard pile
        for card in state.player.deck.discard_pile:
            features[("discard", card.name)] = 1

    elif state.state_type == StateType.EXHAUST_TO_HAND:
        features["exhaustToHand"] = 1
        # Appends indicators for all cards in player's exhaust pile
        for card in state.player.deck.exhaust_pile:
            features[("exhausted", card.name)] = 1

    elif state.state_type == StateType.HAND_TO_DRAW:
        features["handToDraw"] = 1
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand", card.name)] = 1

    elif state.state_type == StateType.HAND_TO_EXHAUST:
        features["handToExhaust"] = 1
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand", card.name)] = 1

    elif state.state_type == StateType.NORMAL_REST:
        features["normalRest"] = 1
        # Grabs health and indicators for each card in player's deck
        for i in range(13):
            features[str(10 * i) + " to " + str(10 * (i + 1)) + " health"] = 1 if state.player.health >= 10 * i and state.player.health < 11 * i else 0

        for card in state.player.deck.cards:
            features[card.name] = 1

    elif state.state_type == StateType.UPGRADE_REST:
        features["upgradeRest"] = 1
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[card.name] = 1

    elif state.state_type == StateType.REMOVE_CARD:
        features["removeCard"] = 1
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[card.name] = 1

    elif state.state_type == StateType.ADD_CARD:
        features["addCard"] = 1
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[card.name] = 1

    else:  # state.state_type == StateType.NORMAL_RANDOM:
        features["normalRandom"] = 1

    return features


"""# Return a single-element list containing a binary (indicator) feature
# for the existence of the (state, action) pair.  Provides no generalization.
def identityFeatureExtractor(state, action):
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]"""

############################################################
# Return the list of rewards that we get for each trial.
def simulate(mdp, numTrials=10, verbose=False, action_gen_type = 0):

    # (discount, featureExtractor, temp_mdp, explorationProb = 0.2)
    # This creates our actual function approximation (based off q-learning) algorithm
    function_approx = Algorithm(1, game_general_feature_extractor, mdp)

    totalRewards = []  # The rewards we get on each trial

    epsilon = 0.0

    for trial in range(numTrials):

        # Grab the start state and put it in the sequence.
        state = mdp.start_state()
        #sequence = [state]

        # Total Discount is 1 for now.
        totalDiscount = 1

        # Keeping track of total reward
        totalReward = 0

        while True:
            # Algorithm will pick one of its possible actions from state state to do.
            # if state.state_type == StateType.ADD_CARD:
                # print mdp.generate_actions(state)

            if action_gen_type == 0:
                action = function_approx.generic_policy(state, epsilon / numTrials)
            else:
                action = function_approx.q_learning_action(state, epsilon / numTrials)

            if verbose:
                print "------------------"
                state.print_information()
                print "\t", action
                print "------------------"

            # Single successor state generated (our MDP is, for all intents and purposes, well, deterministic.)
            successorState, reward = mdp.generate_successor_state(state, action)
            # if mdp.is_end_state(successorState):
                # print state.nc_player.deck.cards

            # Append our action and successor state to the sequence (for verbose display if needed)
            #sequence.append(action)
            #sequence.append(successorState)

            # Incorporate the feedback we got from state, action, reward, state'.
            if action_gen_type != 0:
                function_approx.incorporateFeedback(state, action, reward, successorState)

            totalReward += totalDiscount * reward
            # totalDiscount *= mdp.discount()
            state = successorState

            # If we've hit an end state, we need to stop.
            if mdp.is_end_state(state):
                break

        # Make it slightly more likely we'll exploit
        epsilon += 1
        totalRewards.append(totalReward)
        """print("==========================")
        print("==========================")
        print("Iteration done")
        print("==========================")
        print("==========================")"""
        mdp.combat_count = 0
        # print(function_approx.weights)
    return totalRewards
