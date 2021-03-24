from Characters.character import Character

class Spy(Character):

    ATTACK_PERC = 0.8
    DEFENSE_PERC = 0.3

    def __init__(self,height, equipment):
        super().__init__(height,equipment)
