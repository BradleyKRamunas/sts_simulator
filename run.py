from sts_mdp import STSMDP
from solver import learn
from solver import test
from time import time
import datetime
from collections import defaultdict
from numpy_test import test_np


def run(q_learn, testing, file_name, num_enemies = 10):

    def learn_phase(mdp, weights = defaultdict(float), numIters = 1000):
        print
        print "========================= TRAINING PHASE ========================="
        print

        # simulate params: (mdp, weights, number of iterations, verbose, 0 - generic policy; 1 - q-learning, print weights)
        totalRewards, final_weights = learn(mdp, weights, numIters, False, 1, False)
        print totalRewards

        # Write weights to file
        write_weight_file = open(str(datetime.datetime.fromtimestamp(time())).replace(":", ".")[:19] + " with " + str(numIters) + " iterations.txt", "w")
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
            print "win rate: " + str(float(numWon) / numIters)
            print "loss rate: " + str(1 - (float(numWon) / numIters))
            print

            print "Last " + str(numIters / 2) + " rounds: win rate"
            print "----------------------"
            numLaterWon = 0
            for i in range(numIters / 2, numIters):
                if totalRewards[i] > 0:
                    numLaterWon += 1
            print float(numLaterWon) / (numIters / 2)
            print

            print "Last 100 rounds: win rate"
            print "----------------------"
            last100 = 0
            for i in range(numIters - 100, numIters):
                if totalRewards[i] > 0:
                    last100 += 1
            print float(last100) / 100
            print

            print "Last 50 rounds: win rate"
            print "----------------------"
            last50 = 0
            for i in range(numIters - 50, numIters):
                if totalRewards[i] > 0:
                    last50 += 1
            print float(last50) / 50
            print

            print "First " + str(numIters / 2) + " rounds: win rate"
            print "----------------------"
            first250 = 0
            for i in range(0, numIters / 2):
                if totalRewards[i] > 0:
                    first250 += 1
            print float(first250) / (numIters / 2)

        print_weights(final_weights)
        print_all_stats()

        return final_weights

    # =================================== TESTING PHASE ===================================
    def test_phase(test_mdp, test_weights, num_tests):
        print
        print "========================= TESTING PHASE ========================="
        print

        # Policies - 0 -> random; 1 -> damage greedy; 2 -> q-learning
        # test params:     mdp,     weight vector, numTests, Verbose, policy
        testRewards = test(test_mdp, test_weights, num_tests, True, 2)
        print testRewards

        numWon = 0
        for reward in testRewards:
            if reward > 0:
                numWon += 1

        print "Total averages: (win/loss rate)"
        print "win rate: " + str(float(numWon) / numTests)
        print "loss rate: " + str(1 - (float(numWon) / numTests))
        print

        return float(numWon) / numTests

    def read_weights(name):
        weight_file = open(name)
        weights = defaultdict(float)
        line = weight_file.readline()
        while len(line) > 0:
            data = line.split(" | ")
            weights[data[0]] = float(data[1])
            line = weight_file.readline()
        weight_file.close()
        return weights

    # =========================================================================================
    # Usage: change numTests for number of test iterations. Change numIters for number of learning
    # iterations. If you want pure learning starting from uninitialized (zeroed) weights, file_name
    # must be None. If you want pure testing starting with file-saved weights, use False, True, file_name.
    # Params are q_learn, testing, file_name. N.B. Testing returns the average win rate of using whichever
    # weights were just used for testing.
    mdp = STSMDP(num_enemies)
    numTests = 1
    numIters = 1000
    weights = defaultdict(float)
    if file_name is not None:
        weights = read_weights(file_name)
    if q_learn:
        weights = learn_phase(mdp, weights, numIters)
    if testing:
        return test_phase(mdp, weights, numTests)


def helper(text_file_name):
    f = open(text_file_name)
    line = f.readline()
    stuff_list = []
    while len(line) > 0:
        data = line.split(" | ")
        stuff_list.append((data[0], float(data[1])))
    stuff_list.sort(key=lambda x: x[1])
    for item in stuff_list:
        print item

if __name__ == '__main__':
    # None if we want to just learn and immediately save/test weights
    # run(learn, test, file_name, num_enemies) - num_enemies goes for learning and testing
    # Usage: file_name -> None if you want to start learning anew
    enemies = 10
    # for i in range(3):
    run(False, True, 'best_txt/best.txt', enemies)

