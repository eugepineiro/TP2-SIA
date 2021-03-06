from abc import ABC
class Item(ABC):
     
    def __init__(self, id,force, agility, expertise, resistance, life):
        
        self.id = id
        self.force = force
        self.agility = agility
        self.expertise = expertise
        self.resistance = resistance
        self.life = life
        
    def getForce(self):
        return self.force  
    
    def getAgility(self):
        return self.agility
    
    def getExpertise(self):
        return self.expertise
    
    def getresistance(self):
        return self.resistance
    
    def getLife(self):
        return self.life
    
    def __str__(self):
        return 'Item'

    def __repr__(self):
        return 'Id: {id} - Force: {force} - Agility: {agility} - Expertise: {expertise} - resistance: {resistance} - Life: {life}'.format(
            id=self.id, force=self.force, agility=self.agility, expertise=self.expertise, resistance=self.resistance, life=self.life)

    def __eq__(self,other):
        if type(other) is type(self):
            return self.id == other.id and self.force == other.force and self.agility == other.agility and self.expertise == other.expertise and self.resistance == other.resistance and self.life == other.life
        return False
    
    def __hash__(self):
        return hash(self.id,self.force,self.agility,self.expertise,self.resistance,self.life)