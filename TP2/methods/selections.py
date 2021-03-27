import math
import random
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

# Selects k (indidivuals_amount) individuals between q[i-1] < r[k] < q[i], r random [0,1)
def roulette(characters, individuals_amount): 

    fitness = [] #array of tuples (acum_fitness, character)
    selected_characters = []

    total_fitness = getTotalFitness(characters)

    accum_fitness = 0
    for character in characters: 
        relative_fitness = character.fitness / total_fitness
        accum_fitness = accum_fitness + relative_fitness
        fitness.append((accum_fitness, character))
    
    r=0
    for i in range(individuals_amount): 
         
        r = random.uniform(0,1)

        for j in range(len(fitness)-1):
            accum1 = fitness[j][0]  # q[i-1]
            accum2 = fitness[j+1][0]  # q[1]

            if accum1 < r and r <= accum2 :
                selected_characters.append(fitness[j+1][1])

    return selected_characters

def getTotalFitness(characters): 
    total = 0
    for c in characters: 
        total = total + c.fitness

    return total