from sts_mdp import STSMDP
from solver import simulate

def run():
    mdp = STSMDP()
    simulate(mdp, 1, True, 0)


if __name__ == '__main__':
    run()
