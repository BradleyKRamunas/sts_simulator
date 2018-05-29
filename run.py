from sts_mdp import STSMDP
from solver import simulate

def run():
    mdp = STSMDP()
    numIters = 1000
    totalRewards = simulate(mdp, numIters, False, 1)
    print totalRewards

    numWon = 0.0
    for reward in totalRewards:
        if reward > 0:
            numWon += 1

    print "Total averages: (win/loss rate)"
    print numWon / numIters
    print 1 - (numWon / numIters)
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


if __name__ == '__main__':
    run()
