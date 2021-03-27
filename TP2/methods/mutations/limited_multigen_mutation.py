import random
from .mutation_lib import MutationLib
from Characters.character import Character 
from constants import *

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