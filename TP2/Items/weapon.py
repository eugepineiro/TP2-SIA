from Items.item import Item

class Weapon(Item):
 
    def __init__(self, id,force, agility, expertise, resistance, life):
        super().__init__(id,force, agility, expertise, resistance, life)

    def __str__():
        return 'Weapon'