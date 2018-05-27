import math
from enums import *
# offer a chance to rest or upgrade (occurs with 0.2 probability)
# OPTIONS:
# rest -> heal 30% of max_health
# upgrade -> upgrade any of the non-upgraded cards


class RestSite:
    def __init__(self, player):
        self.player = player
        self.state_type = StateType.NORMAL_REST

    def heal(self):
        possible_heal = self.player.health + math.floor(0.3 * self.player.max_health)
        self.player.health = min(possible_heal, self.player.max_health)

    def upgrade(self):
        # TODO: once upgraded cards are implemented... for now, only heal
        self.state_type = StateType.UPGRADE_REST
        return