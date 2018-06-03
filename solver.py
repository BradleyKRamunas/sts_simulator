from algorithm import *
from combat import *
from collections import defaultdict
from brain import *
import time


############################################################
def game_general_feature_extractor(state, action):

    # Numba - similar to Cython; offers large performance speedup

    # Features is going to be a dictionary of {key: int}
    features = defaultdict(int)

    if state.state_type == StateType.NORMAL_COMBAT:

        # Policy gradients?

        # Allows for a constant term bias
        features["combat"] = 1

        # Idea: discretized health indicators
        # for i in range(13):
            # features[str(10 * i) + " to " + str(10 * (i + 1)) + " health"] = 1 if state.player.health >= 10 * i and state.player.health < 11 * i else 0

        # Health feature - what fraction of max health are we?
        features["health"] = float(state.player.health) / state.player.max_health

        # Idea: discretized block indicators
        # for i in range(10):
            # features[str(10 * i) + " to " + str(10 * (i + 1)) + " block"] = 1 if state.player.block >= 10 * i and state.player.block < 11 * i else 0

        # Block feature
        # features["block"] = state.player.block

        # Total enemy health feature, total enemy block feature, total enemy attack intent, enemy intent indicator
        # Also condition indicators/value/duration for player and enemy
        totalEnemyHP = 0
        totalEnemyMaxHP = 0
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
            totalEnemyMaxHP += enemy.max_health
            totalEnemyHP += enemy.health

        # features["total enemy HP"] = float(totalEnemyHP) / totalEnemyMaxHP
        features["block percentage"] = min(1, 0 if totalEnemyAtk == 0 else float(state.player.block) / totalEnemyAtk)
        # features["total enemy block"] = totalEnemyBlock
        # TODO: Features for player's action (how much damage it's doing; what statuses it's applying)

        # TODO: Feature for sequences of cards played.

        """# Appends indicators for all cards in player's hand
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
            features[("exhausted", card.name)] = 1"""

        # This way we can keep track of which cards we've played this round
        for card in state.cards_played:
            features[("single_played", card)] += 1
        for card_pair in state.two_combos_played:
            features[("double_played", card_pair)] += 1

        # See how many turns we ended early
        features["early_end"] = state.turns_ended_early

    elif state.state_type == StateType.COPY:
        features["copy"] = 1
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("copy_hand", card.name)] = 1

    elif state.state_type == StateType.DISCARD_TO_DRAW:
        features["discardToDraw"] = 1
        # Appends indicators for all cards in player's discard pile
        for card in state.player.deck.discard_pile:
            features[("discard_to_draw", card.name)] = 1

    elif state.state_type == StateType.EXHAUST_TO_HAND:
        features["exhaustToHand"] = 1
        # Appends indicators for all cards in player's exhaust pile
        for card in state.player.deck.exhaust_pile:
            features[("exhausted_to_hand", card.name)] = 1

    elif state.state_type == StateType.HAND_TO_DRAW:
        features["handToDraw"] = 1
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand_to_draw", card.name)] = 1

    elif state.state_type == StateType.HAND_TO_EXHAUST:
        features["handToExhaust"] = 1
        # Appends indicators for all cards in player's hand
        for card in state.player.deck.hand:
            features[("hand_to_exhaust", card.name)] = 1

    elif state.state_type == StateType.NORMAL_REST:
        features["normalRest"] = 1
        # Grabs health and indicators for each card in player's deck
        # for i in range(13):
            # features[str(10 * i) + " to " + str(10 * (i + 1)) + " health"] = 1 if state.player.health >= 10 * i and state.player.health < 11 * i else 0
        # Health feature - what fraction of max health are we?
        features["health_rest"] = float(state.player.health) / state.player.max_health

        for card in state.player.deck.cards:
            features[("health_rest", card.name)] = 1

    elif state.state_type == StateType.UPGRADE_REST:
        features["upgradeRest"] = 1
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[("upgrade_rest", card.name)] = 1

    elif state.state_type == StateType.REMOVE_CARD:
        features["removeCard"] = 1
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[("remove_card", card.name)] = 1

    elif state.state_type == StateType.ADD_CARD:
        features["addCard"] = 1
        # Grabs indicators for each card in the player's deck
        for card in state.player.deck.cards:
            features[("add_card", card.name)] = 1

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
def learn(mdp, numTrials=10, verbose=False, action_gen_type = 0, weights = False):

    startTime = time.time()
    lastThirty = startTime

    # (discount, featureExtractor, temp_mdp, explorationProb = 0.2)
    # This creates our actual function approximation (based off q-learning) algorithm
    function_approx = Algorithm(0.5, game_general_feature_extractor, mdp)

    totalRewards = []  # The rewards we get on each trial

    # Exploration probability
    epsilon = numTrials

    for trial in range(numTrials):

        curTime = time.time()
        if curTime - lastThirty >= 15:
            print str(int(curTime - startTime)) + " seconds have elapsed."
            print "Iteration number: " + str(trial)
            lastThirty = curTime

        # Grab the start state and put it in the sequence.
        state = mdp.start_state()

        # Total Discount is 1 for now.
        totalDiscount = 1

        # Keeping track of total reward
        totalReward = 0

        while True:
            # Algorithm will pick one of its possible actions from state state to do.
            if action_gen_type == 0:
                action = function_approx.generic_policy(state, float(epsilon) / numTrials)
            else:
                action = function_approx.q_learning_action(state, float(epsilon) / numTrials)

            if verbose:
                print "------------------"
                state.print_information()
                print "\t", action
                print "------------------"

            # Single successor state generated (our MDP is, for all intents and purposes, well, deterministic.)
            successorState, reward = mdp.generate_successor_state(state, action, True)
            # if mdp.is_end_state(successorState):
                # print state.nc_player.deck.cards

            """if reward != 0:
                print "pre fight finished (w/o incorporate feedback)"
                print reward
                print function_approx.weights"""

            # Incorporate the feedback we got from state, action, reward, state'.
            if action_gen_type != 0:
                function_approx.incorporateFeedback(state, action, reward, successorState)

            """if reward != 0:
                print "post fight finished (w/incorporate feedback)"
                print reward
                print function_approx.weights"""

            totalReward += totalDiscount * reward
            # totalDiscount *= mdp.discount()
            state = successorState

            # If we've hit an end state, we need to stop.
            if mdp.is_end_state(state):
                break

        # Make it slightly more likely we'll exploit
        epsilon -= 1
        totalRewards.append(totalReward)
        if verbose:
            print("====================================")
            print("====================================")
            print("Iteration done")
            print("====================================")
            print("====================================")
        mdp.combat_count = 0
        if weights:
            print(function_approx.weights)

    print "Total runtime: " + str(int(time.time() - startTime)) + " seconds."
    return totalRewards, function_approx.weights


def test(mdp, weights, numTrials=10, verbose=False):

    startTime = time.time()
    lastThirty = startTime

    # (discount, featureExtractor, temp_mdp, explorationProb = 0.2)
    # This creates our actual function approximation (based off q-learning) algorithm
    brain = Brain(1, game_general_feature_extractor, mdp, weights)

    totalRewards = []  # The rewards we get on each trial

    for trial in range(numTrials):

        curTime = time.time()
        if curTime - lastThirty >= 15:
            print str(int(curTime - startTime)) + " seconds have elapsed."
            print "Iteration number: " + str(trial)
            lastThirty = curTime

        # Grab the start state and put it in the sequence.
        state = mdp.start_state()

        # Total Discount is 1 for now.
        totalDiscount = 1

        # Keeping track of total reward
        totalReward = 0

        while True:
            # Algorithm will pick one of its possible actions from state state to do.
            action = brain.q_learning_test(state)

            if verbose:
                print "------------------"
                state.print_information()
                print "\t", action
                print "------------------"

            # Single successor state generated (our MDP is, for all intents and purposes, well, deterministic.)
            successorState, reward = mdp.generate_successor_state(state, action, True)

            totalReward += totalDiscount * reward
            # totalDiscount *= mdp.discount()
            state = successorState

            # If we've hit an end state, we need to stop.
            if mdp.is_end_state(state):
                break

        totalRewards.append(totalReward)
        """print("==========================")
        print("==========================")
        print("Iteration done")
        print("==========================")
        print("==========================")"""
        mdp.combat_count = 0

    print "Total runtime: " + str(int(time.time() - startTime)) + " seconds."
    return totalRewards