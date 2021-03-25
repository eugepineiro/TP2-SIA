from Characters.character import Character

class Warrior(Character):

    ATTACK_PERC = 0.6
    DEFENSE_PERC = 0.6

    def __init__(self, id, height, equipment):
        super().__init__(id, height, equipment)
