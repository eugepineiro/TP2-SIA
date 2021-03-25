from Characters.character import Character

class Defender(Character):

    ATTACK_PERC = 0.3
    DEFENSE_PERC = 0.8

    def __init__(self,id,height, equipment):
        super().__init__(id,height,equipment)
