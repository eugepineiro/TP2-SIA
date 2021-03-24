from abc import ABC
class Item(ABC):
     
    def __init__(self, id,force, agility, expertise, resistence, life):
        
        self.id = id
        self.force = force
        self.agility = agility
        self.expertise = expertise
        self.resistence = resistence
        self.life = life
        
    
    def getForce(self):
        return self.force  
    
    def getAgility(self):
        return self.agility
    
    def getExpertise(self):
        return self.expertise
    
    def getResistence(self):
        return self.resistence
    
    def getLife(self):
        return self.life
        