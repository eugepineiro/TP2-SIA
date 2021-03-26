import math

class Character:

    def __init__(self, id, height, equipment,character_class):
        
        self.id = id
        self.h = height              # uniform [1,3 ; 2] meters 
        self.equipment = equipment   # array d weapon, boots, helmet, gloves, armor   
        self.character_class = character_class
        self.ATM = self.getATM()
        self.DEM = self.getDEM()

        self.force = self.getStat(100,list(map(lambda item: item.getForce(),self.equipment)))
        self.agility = self.getStat(1,list(map(lambda item: item.getAgility(),self.equipment)))
        self.expertise = self.getStat(0.6,list(map(lambda item: item.getExpertise(),self.equipment)))
        self.resistance = self.getStat(1,list(map(lambda item: item.getresistance(),self.equipment)))
        self.life = self.getStat(100,list(map(lambda item: item.getLife(),self.equipment)))
        
        self.attack = self.calculateAttack()
        self.defense = self.calculateDefense()
        
        self.fitness = self.getFitness()
        
        
    def getFitness(self):
        return self.character_class.attack_perc * self.attack + self.character_class.defense_perc * self.defense

    def getATM(self):
        return 0.7 - pow(3*self.h-5, 4) + pow(3*self.h-5, 2) + self.h/4.0

    def getDEM(self):
        return 1.9 + pow(2.5*self.h-4.16, 4) - pow(2.5*self.h-4.16, 2) - 3*self.h/10.0 
    
    def getStat(self, multiplier, stats):     
        return multiplier * math.tanh(0.01*sum(stats))
          
    def calculateAttack(self):
        return (self.agility + self.expertise) * self.force * self.ATM

    def calculateDefense(self):
        return (self.resistance + self.expertise) * self.life * self.DEM

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and other.id == self.id)

    def __hash__(self):
        return hash(self.id)

    def __lt__(self, other):
        return self.fitness > other.fitness
    
    def __le__(self, other):
        return self.fitness >= other.fitness

    def __str__(self):
        return '(Id: {id} - Fitness: {fitness} - Class: {char_class})'.format(id=self.id, fitness=self.fitness, char_class=self.character_class)

    def __repr__(self):
        return self.__str__()