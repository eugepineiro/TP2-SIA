from Characters.character import Character

class Archer(Character):

    ATTACK_PERC = 0.9
    DEFENSE_PERC = 0.1

    def __init__(self,id,height, equipment):
        super().__init__(id,height,equipment)
