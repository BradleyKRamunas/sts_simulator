from sts_mdp import STSMDP
from solver import simulate
import time

def run():
    mdp = STSMDP()
    startTime = time.time()
    totalRewards = simulate(mdp, 10, True, 1)
    print("Total runtime: " + str(time.time() - startTime))
    print totalRewards

if __name__ == '__main__':
    run()
