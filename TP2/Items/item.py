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
    
    def __str__(self):
        return 'Id: {id} - Force: {force} - Agility: {agility} - Expertise: {expertise} - Resistence: {resistence} - Life: {life}'.format(
            id=self.id, force=self.force, agility=self.agility, expertise=self.expertise, resistence=self.resistence, life=self.life)

    def __repr__(self):
        return self.__str__()
        