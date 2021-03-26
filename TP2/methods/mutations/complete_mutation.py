import random
from .mutation_lib import MutationLib
from Characters.character import Character 
from constants import *

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
