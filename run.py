import main
import cards


def run():
    player = main.Player(cards.generate_default_deck(), 80)
    enemy_ai = main.GoblinAI()
    enemy = main.CombatEnemy(None, enemy_ai, 30)
    combat = main.Combat(player, [enemy])


if __name__ == '__main__':
    run()
