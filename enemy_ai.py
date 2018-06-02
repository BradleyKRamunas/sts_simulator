from enums import Intent
from enums import Status

class GoblinAI:
    def __init__(self):
        self.sequence = [Intent.ATTACK]
        self.attack = 6
        self.block = 0
        self.buff = 0
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        return (move, self.attack, None)

class SpikeSlimeAI:
    def __init__(self):
        self.sequence = [Intent.DEBUFF, Intent.DEBUFF, Intent.ATTACK, Intent.ATTACK]
        self.attack = 8
        self.block = 0
        self.buff = 0
        self.debuff = 1

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.DEBUFF:
            return (move, self.debuff, Status.FRAIL)
        else:
            return (move, self.attack, None)

class AcidSlimeAI:
    def __init__(self):
        self.sequence = [Intent.DEBUFF, Intent.ATTACK]
        self.attack = 3
        self.block = 0
        self.buff = 0
        self.debuff = 1

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.DEBUFF:
            return (move, self.debuff, Status.WEAK)
        else:
            return (move, self.attack, None)

class JawWormAI:
    def __init__(self):
        self.sequence = [Intent.ATTACK, Intent.BLOCK, Intent.BUFF]
        self.attack = 11
        self.block = 6
        self.buff = 3
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BUFF:
            return (move, self.buff, Status.STRENGTH)
        elif move == Intent.BLOCK:
            return (move, self.block, None)
        else:
            return (move, self.attack, None)

class ExplosiveGoblinAI:
    def __init__(self):
        self.sequence = [Intent.BLOCK, Intent.BLOCK, Intent.BLOCK, Intent.ATTACK]
        self.attack = 30
        self.block = 5
        self.buff = 0
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BLOCK:
            return (move, self.block, None)
        else:
            return (move, self.attack, None)

class FungiBeastAI:
    def __init__(self):
        self.sequence = [Intent.BUFF, Intent.ATTACK, Intent.ATTACK]
        self.attack = 6
        self.block = 0
        self.buff = 3
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BUFF:
            return (move, self.buff, Status.STRENGTH)
        else:
            return (move, self.attack, None)

class SlaverAI:
    def __init__(self):
        self.sequence = [Intent.ATTACK]
        self.attack = 12
        self.block = 0
        self.buff = 0
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        return (move, self.attack, None)


class LagavulinAI:
    def __init__(self):
        self.sequence = [Intent.BLOCK, Intent.BLOCK, Intent.ATTACK, Intent.ATTACK, Intent.ATTACK, Intent.DEBUFF]
        self.attack = 18
        self.block = 12
        self.buff = 0
        self.debuff = 3

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BLOCK:
            return (move, self.block, None)
        elif move == Intent.ATTACK:
            return (move, self.attack, None)
        else:
            return (move, self.debuff, Status.WEAK)

class SentryOddAI:
    def __init__(self):
        self.sequence = [Intent.BLOCK, Intent.ATTACK]
        self.attack = 8
        self.block = 8
        self.buff = 0
        self.debuff = 3

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BLOCK:
            return (move, self.block, None)
        else:
            return (move, self.attack, None)


class SentryEvenAI:
    def __init__(self):
        self.sequence = [Intent.ATTACK, Intent.BLOCK]
        self.attack = 8
        self.block = 8
        self.buff = 0
        self.debuff = 3

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.BLOCK:
            return (move, self.block, None)
        else:
            return (move, self.attack, None)


class GremlinNobAI:
    def __init__(self):
        self.sequence = [Intent.BUFF, Intent.ATTACK, Intent.ATTACK, Intent.ATTACK]
        self.attack = 15
        self.block = 0
        self.buff = 3
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.ATTACK:
            return (move, self.attack, None)
        else:
            return (move, self.buff, Status.STRENGTH)


class DoubleThiefAI:
    def __init__(self):
        self.sequence = [Intent.ATTACK, Intent.ATTACK, Intent.ATTACK, Intent.BLOCK]
        self.attack = 8
        self.block = 15
        self.buff = 0
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.ATTACK:
            return (move, self.attack, None)
        else:
            return (move, self.block, None)


class GremlinWizardAI:
    def __init__(self):
        self.sequence = [Intent.DEBUFF, Intent.BUFF, Intent.BLOCK, Intent.ATTACK]
        self.attack = 18
        self.block = 10
        self.buff = 2
        self.debuff = 2

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.ATTACK:
            return (move, self.attack, None)
        elif move == Intent.BLOCK:
            return (move, self.block, None)
        elif move == Intent.DEBUFF:
            return (move, self.debuff, Status.WEAK)
        elif move == Intent.BUFF:
            return (move, self.buff, Status.STRENGTH)


class ThornyPlantAI:
    def __init__(self):
        self.sequence = Intent[Intent.BUFF, Intent.BLOCK, Intent.BLOCK, Intent.ATTACK, Intent.ATTACK]
        self.attack = 6
        self.block = 12
        self.buff = 3
        self.debuff = 0

    def generate_move(self):
        move = self.sequence.pop(0)
        self.sequence.append(move)
        if move == Intent.ATTACK:
            return (move, self.attack, None)
        elif move == Intent.BLOCK:
            return (move, self.block, None)
        elif move == Intent.BUFF:
            return (move, self.buff, Status.THORNS)

