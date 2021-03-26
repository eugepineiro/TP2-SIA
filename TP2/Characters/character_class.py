from enum import Enum

class CharacterClass(Enum):
    WARRIOR = (0.6,0.6)
    ARCHER = (0.9,0.1)
    DEFENDER = (0.3,0.8)
    SPY = (0.8,0.3)

    def __init__(self,attack_perc, defense_perc):
        self.attack_perc = attack_perc
        self.defense_perc = defense_perc

    def __str__(self):
        return '{name}'.format(name=self.name)