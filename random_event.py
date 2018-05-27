import random
import cards
from enums import StateType
# offer a random event (occurs with 0.2 probability)
# 1/8 probability for each possible random event
# EVENTS:
# gain 1 energy
# gain 5 max hp
# lose 5 max hp
# gain 10 max hp
# lose 7 max hp
# gain 3 random cards
# remove card from deck
# choose card to add to deck out of 3

class RandomEvent:
    def __init__(self, player):
        self.player = player
        self.state_type = StateType.NORMAL_RANDOM

    def generate_random_event(self):
        event_pos = random.randint(1,7)
        if event_pos == 0:
            # gain 1 energy
            self.player.max_energy += 1
        elif event_pos == 1:
            # gain 5 max hp
            self.player.max_health += 5
        elif event_pos == 2:
            # lose 5 max hp
            self.player.max_health -= 5
        elif event_pos == 3:
            # gain 10 max hp
            self.player.max_health += 10
        elif event_pos == 4:
            # lose 7 max hp
            self.player.max_health -= 7
        elif event_pos == 5:
            # gain 3 random cards
            all_cards = cards.generate_all_cards()
            first_card = random.choice(all_cards)
            second_card = random.choice(all_cards)
            third_card = random.choice(all_cards)
            self.player.deck.add_card(first_card)
            self.player.deck.add_card(second_card)
            self.player.deck.add_card(third_card)
        elif event_pos == 6:
            # remove a card from deck
            self.state_type = StateType.REMOVE_CARD
        elif event_pos == 7:
            self.state_type = StateType.ADD_CARD
