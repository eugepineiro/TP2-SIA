# genes[h, weapon, boots, armor, gloves, helmet]
# Qué es mutar un gen? --> Elijo un gen y lo intercambio por otro del tsv (en caso de ser item), si es height getUniform(1.3 ; 2)
#                      --> o aplico un delta
# Tengo que definir una probabilidad de mutación Pm --> si se cumple esa Pm para mi individuo --> agarro un gen al azar y lo muto, sino no (puede pasar que no mute ningun individuo, no pasa nada)
import random
from .mutation_lib import MutationLib
from Characters.character import Character 
from constants import *

# Selects one random gen to mutate

def oneGenMutation(individual, item_handler):
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
