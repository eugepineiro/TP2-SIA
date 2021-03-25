from Characters.character import Character

class Warrior(Character):

    ATTACK_PERC = 0.6
    DEFENSE_PERC = 0.6

    def __init__(self,height, equipment):
        super().__init__(height,equipment)
