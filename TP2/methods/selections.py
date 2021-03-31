import math
import random
from constants import * 
from Characters.character import Character
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

def roulette(characters, individuals_amount):
    return rouletteOrUniversal(ROULETTE_S, characters,individuals_amount)

def universal(characters, individuals_amount):
    return rouletteOrUniversal(UNIVERSAL_S, characters,individuals_amount)

# Selects k (individuals_amount) individuals between q[i-1] < r[k] < q[i], r random [0,1)
def rouletteOrUniversal(method,characters, individuals_amount): 

    fitness = [(0,None)] #array of tuples (acum_fitness, character)
    selected_characters = []
    total_fitness = getTotalFitness(characters)

    accum_fitness = 0
    for character in characters: 
        relative_fitness = character.fitness / total_fitness
        accum_fitness = accum_fitness + relative_fitness
        fitness.append((accum_fitness, character))
    
    r=0
    for i in range(individuals_amount): 
         
        rand = random.uniform(0,1)
        if method == ROULETTE_S: 
            r = rand
        elif method == UNIVERSAL_S: 
            r = (i + rand)/individuals_amount

        for j in range(len(fitness)-1):
            accum1 = fitness[j][0]      # q[i-1]
            accum2 = fitness[j+1][0]    # q[1]
            
            if accum1 < r and r <= accum2 :
                selected_characters.append(fitness[j+1][1])
    return selected_characters

def getTotalFitness(characters): 
    total = 0
    for c in characters: 
        total = total + c.fitness

    return total

def ranking(characters, individuals_amount, population_amount):
    characters.sort()
    aux_chars = []
    id_char_dict = {}
    
    for i, character in enumerate(characters):
        id_char_dict[character.id] = character
        pseudo_fitness = (population_amount - i - 1) / population_amount
        aux_char = Character(character.id, character.height, character.equipment,character.character_class)
        aux_char.fitness = pseudo_fitness
        aux_chars.append(aux_char)
    
    aux_chars = roulette(aux_chars,individuals_amount)

    ids = list(map(lambda char: char.id, aux_chars))
    selected_chars = []
    for id in ids:
        selected_chars.append(id_char_dict.get(id))
    return selected_chars

def boltzmann(characters, individuals_amount, population_amount, generation,t0,tc,k):
    
    aux_chars = []
    id_char_dict = {}
    temp = tc + (t0 - tc) * math.exp(-k * generation)
    pop_avg = calculatePopAvg(characters,temp)

    for i, character in enumerate(characters):
        id_char_dict[character.id] = character
        pseudo_fitness = math.exp(character.fitness/temp)/pop_avg
        aux_char = Character(character.id, character.height, character.equipment,character.character_class)
        aux_char.fitness = pseudo_fitness
        aux_chars.append(aux_char)
    
    aux_chars = roulette(aux_chars,individuals_amount)

    ids = list(map(lambda char: char.id, aux_chars))
    selected_chars = []
    for id in ids:
        selected_chars.append(id_char_dict.get(id))
    return selected_chars

def calculatePopAvg(characters,temp):
    return sum(list(map(lambda char: math.exp(char.fitness/temp),characters)))/len(characters)


def d_tournaments(characters, individuals_amount, population_amount, m_value):
    selected_characters = []
    for i in range(individuals_amount):
        selected = characters[random.randint(0,population_amount-1)]
        for j in range(m_value-1):
            char = characters[random.randint(0,population_amount-1)]
            if char.fitness > selected.fitness:
                selected = char
        selected_characters.append(selected)
    
    return selected_characters

def p_tournaments(characters, individuals_amount, population_amount, threshold):
    selected_characters = []
    for i in range(individuals_amount):
        
        if threshold < 0.5 or threshold > 1:
            raise ValueError("Probabilistic Tournaments threshold must be between 0.5 and 1")
        
        chars = sorted([characters[random.randint(0,population_amount-1)],characters[random.randint(0,population_amount-1)]],key=lambda char: char.fitness, reverse=True)
        r = random.uniform(0,1)
        if r < threshold:
            selected_characters.append(chars[0])
        else:
            selected_characters.append(chars[1])
    return selected_characters