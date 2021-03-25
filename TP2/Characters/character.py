from abc import ABC
import math

class Character(ABC):
    ATTACK_PERC = 0
    DEFENSE_PERC = 0 

    def __init__(self, height, equipment):
        
        self.h = height              # uniform [1,3 ; 2] meters 
        self.equipment = equipment   # array d weapon, boots, helmet, gloves, armor   

        self.ATM = self.getATM()
        self.DEM = self.getDEM()

        self.force = self.getStat(100,list(map(lambda item: item.getForce(),self.equipment)))
        self.agility = self.getStat(1,list(map(lambda item: item.getAgility(),self.equipment)))
        self.expertise = self.getStat(0.6,list(map(lambda item: item.getExpertise(),self.equipment)))
        self.resistence = self.getStat(1,list(map(lambda item: item.getResistence(),self.equipment)))
        self.life = self.getStat(100,list(map(lambda item: item.getLife(),self.equipment)))
        
        self.attack = self.calculateAttack()
        self.defense = self.calculateDefense()
        
        self.fitness = self.getFitness()
        
        
    def getFitness(self):
        return self.ATTACK_PERC * self.attack + self.DEFENSE_PERC * self.defense

    def getATM(self):
        return 0.7 - pow(3*self.h-5, 4) + pow(3*self.h-5, 2) + self.h/4.0

    def getDEM(self):
        return 1.9 + pow(2.5*self.h-4.16, 4) - pow(2.5*self.h-4.16, 2) - 3*self.h/10.0 
    
    def getStat(self, multiplier, stats):     
        return multiplier * math.tanh(0.01*sum(stats))
          
    def calculateAttack(self):
        return (self.agility + self.expertise) * self.force * self.ATM

    def calculateDefense(self):
        return (self.resistence + self.expertise) * self.life * self.DEM
        