from Items.item import Item

class Armor(Item):
 
    def __init__(self,id, force, agility, expertise, resistance, life):
        super().__init__(id,force, agility, expertise, resistance, life)