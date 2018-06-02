from sts_mdp import STSMDP
from solver import learn
from solver import test
from numpy_test import test_np


def run():
    mdp = STSMDP()
    numIters = 500
    # simulate params: (mdp, number of iterations, verbose, 0 - generic policy; 1 - q-learning, print weights)
    totalRewards, final_weights = learn(mdp, numIters, False, 1, False)
    print totalRewards

    write_weight_file = open("weights.txt", "w")
    for item in final_weights:
        write_weight_file.write(str(item) + " | " + str(final_weights[item]) + "\n")

    numWon = 0.0
    for reward in totalRewards:
        if reward > 0:
            numWon += 1

    def print_weights(weights):
        print "Turns ended early"
        print "{}, {}".format("early_end", weights["early_end"])

        print "Overall Status"
        for key in weights.keys():
            if "enemy" in key or "player" in key or "health" in key or "total enemy HP" in key or "block percentage" in key:
                print "{}, {}".format(key, weights[key])

        """print "Cards in hand"
        for key in weights.keys():
            if "hand" in key:
                print "{}, {}".format(key, weights[key])"""

        # Prints out which cards were used this game
        print "Cards used"
        for key in weights.keys():
            if "single_played" in key:
                print "{}, {}".format(key, weights[key])

        print "Card pairs used"
        for key in weights.keys():
            if "double_played" in key:
                print "{}, {}".format(key, weights[key])

    def print_all_stats():
        print "Total averages: (win/loss rate)"
        print "win rate: " + str(numWon / numIters)
        print "loss rate: " + str(1 - (numWon / numIters))
        print

        print "Last " + str(numIters / 2) + " rounds: win rate"
        print "----------------------"
        numLaterWon = 0.0
        for i in range(numIters / 2, numIters):
            if totalRewards[i] > 0:
                numLaterWon += 1
        print numLaterWon / (numIters / 2)
        print

        print "Last 100 rounds: win rate"
        print "----------------------"
        last100 = 0.0
        for i in range(numIters - 100, numIters):
            if totalRewards[i] > 0:
                last100 += 1
        print last100 / 100
        print

        print "Last 50 rounds: win rate"
        print "----------------------"
        last50 = 0.0
        for i in range(numIters - 50, numIters):
            if totalRewards[i] > 0:
                last50 += 1
        print last50 / 50
        print

        print "First " + str(numIters / 2) + " rounds: win rate"
        print "----------------------"
        first250 = 0.0
        for i in range(0, numIters / 2):
            if totalRewards[i] > 0:
                first250 += 1
        print first250 / (numIters / 2)

    print_weights(final_weights)
    print_all_stats()

    # =================================== TESTING PHASE ===================================
    print
    print "========================= TESTING PHASE ========================="
    print

    """numTests = 300
    testRewards = test(mdp, final_weights, numTests, False)
    print testRewards"""

if __name__ == '__main__':
    run()
