import math
from enums import *
from copy import deepcopy
# offer a chance to rest or upgrade (occurs with 0.2 probability)
# OPTIONS:
# rest -> heal 30% of max_health
# upgrade -> upgrade any of the non-upgraded cards


class RestSite:
    def __init__(self, player):
        self.player = deepcopy(player)
        self.state_type = StateType.NORMAL_REST

    def heal(self):
        print self.player.health
        possible_heal = int(self.player.health + math.floor(0.3 * self.player.max_health))
        self.player.health = min(possible_heal, self.player.max_health)
        print self.player.health

    def upgrade(self):
        self.state_type = StateType.UPGRADE_REST

    def print_information(self):
        print "We are at a rest site at the moment."
