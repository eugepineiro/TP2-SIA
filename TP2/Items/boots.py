from Items.item import Item

class Boots(Item):
 
    def __init__(self,id, force, agility, expertise, resistance, life):
        super().__init__(id,force, agility, expertise, resistance, life)

    def __str__(self):
        return 'Boots'