import random
from Characters.character import Character 
from constants import *

class MutationLib:
    # Tengo que definir una probabilidad de mutación Pm --> debería depende de alguna forma de la cantidad de generaciones 
    # que tengo me parece porque la idea es explorar mucho al principio y a medida que van pasando las generaciones o el 
    # tiempo disminuir la exploracion y aumentar la explotacion

    def getMutationProbability():
        return random.uniform(0, 1)

    def getNewGen(gen_class, item_handler):

        if gen_class == HEIGHT_CLASS:
            new_gen = random.uniform(MIN_HEIGHT, MAX_HEIGHT)
        else:
            new_gen = item_handler.getRandomItem(gen_class)

        return new_gen

# Mutates all genes
def completeMutation(individual, item_handler):
    equipment_dict = individual.equipment
    height = individual.height

    genes = [individual.height] + individual.getEquipment()

    for gen in genes: 
        gen_class = gen.__class__.__name__
        new_gen = MutationLib.getNewGen(gen_class, item_handler)
        print(gen_class)
        if gen_class == HEIGHT_CLASS:
            height = new_gen
        else:
            equipment_dict[gen_class] = new_gen
 
    mutated_individual = Character(individual.id, height, equipment_dict, individual.character_class)

    return mutated_individual

#Selects M random genes to mutate 
M = 3
def limitedMultigenMutation(individual, item_handler):
    equipment_dict = individual.equipment
    height = individual.height
    #genes_to_mutate_amount = random.randint(1,M). # Selects x genes to mutate, x in [1, M], M is small
    genes = [individual.height] + individual.getEquipment()

    genes_to_mutate = random.sample(genes, M)

    for gen in genes_to_mutate:
        gen_class = gen.__class__.__name__
        new_gen = MutationLib.getNewGen(gen_class, item_handler)
        print(gen_class)
        if gen_class == HEIGHT_CLASS:
            height = new_gen
        else:
            equipment_dict[gen_class] = new_gen
 
    mutated_individual = Character(individual.id, height, equipment_dict, individual.character_class)

    return mutated_individual

# Selects one random gen to mutate
def oneGenMutation(individual, item_handler):
    # genes[h, weapon, boots, armor, gloves, helmet]
    # Qué es mutar un gen? --> Elijo un gen y lo intercambio por otro del tsv (en caso de ser item), si es height getUniform(1.3 ; 2)
    #                      --> o aplico un delta
    # Tengo que definir una probabilidad de mutación Pm --> si se cumple esa Pm para mi individuo --> 
    # --> agarro un gen al azar y lo muto, sino no (puede pasar que no mute ningun individuo, no pasa nada)
    equipment_dict = individual.equipment
    height = individual.height

    genes = [individual.height] + individual.getEquipment()
    gen_to_mutate = random.choice(genes)
    gen_class = gen_to_mutate.__class__.__name__

    new_gen = MutationLib.getNewGen(gen_class, item_handler)
   
    if gen_class == HEIGHT_CLASS:
        height = new_gen
    else:
        equipment_dict[gen_class] = new_gen
 
    mutated_individual = Character(individual.id, height, equipment_dict, individual.character_class)

    return mutated_individual


# Each gen has a random probability to mutate
def uniformMultigenMutation(individual, item_handler, individual_mutation_probability):
    equipment_dict = individual.equipment
    height = individual.height
    
    genes = [individual.height] + individual.getEquipment()
 
    for gen in genes:
        if individual_mutation_probability < random.uniform(0,1): 
            gen_class = gen.__class__.__name__
            new_gen = MutationLib.getNewGen(gen_class, item_handler)
            print(gen_class)
            if gen_class == HEIGHT_CLASS:
                height = new_gen
            else:
                equipment_dict[gen_class] = new_gen
 
    mutated_individual = Character(individual.id, height, equipment_dict, individual.character_class)

    return mutated_individual