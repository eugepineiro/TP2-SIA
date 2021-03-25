from Characters.warrior import Warrior
from Characters.archer import Archer
from Characters.defender import Defender
from Characters.spy import Spy
import math
#Selects the k characters with better fitness, k = individuals_amount 

def elite(characters, individuals_amount, population_amount):

    characters.sort()
    new_characters = []
    
    for i,character in enumerate(characters):
        n = math.ceil((individuals_amount - i) / population_amount)
        len_new_characters = len(new_characters)
        
        if len_new_characters >= individuals_amount:
            return new_characters
        elif individuals_amount - len_new_characters < n : 
            n = individuals_amount - len_new_characters
        for j in range(n):
            new_characters.append(character)
        
    return new_characters