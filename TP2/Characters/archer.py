from Characters.character import Character

class Archer(Character):

    ATTACK_PERC = 0.9
    DEFENSE_PERC = 0.1

    def __init__(self,height, equipment):
        super().__init__(height,equipment)
