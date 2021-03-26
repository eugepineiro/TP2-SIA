# crear un personaje --> conseguir el array de items que le tiene que pasar --> abre los tsv y elige uno de cada PONELE QUE DE FORMA RANDOM
# el mejor personaje --> genes: h, equipent
# poblacion: n personajes --> QUIERO EL FITNESS --> elegir algun alg genetico y aplicar crossover y mutation
# --------
# GEN1: Height
# GEN2: Helmet
# GEN3: Armor
# GEN4: Boots
# GEN5: Weapon
# GEN6: Gloves

# 1. SELECCION DE PADRES
# 2. SE APAREAN LOS PADRES
# 3. SE HACE CROSSOVER
# 4. SE HACE MUTACION DE ALGUNOS HIJOS DE LA NUEVA GENERACION
# 5. CONDICION DE CORTE

import json
import csv
import random
from item_handler import ItemHandler

from Characters.character import Character
from Characters.character_class import CharacterClass
from Items.armor import Armor
from Items.boots import Boots
from Items.gloves import Gloves
from Items.helmet import Helmet
from Items.weapon import Weapon

from methods.selections.elite import elite
from methods.mutations.one_gen_mutation import oneGenMutation
from methods.mutations.complete_mutation import completeMutation
from methods.mutations.limited_multigen_mutation import limitedMultigenMutation
from methods.mutations.uniform_multigen_mutation import uniformMultigenMutation
from methods.mutations.mutation_lib import MutationLib
from methods.crossovers.one_point_cross import onePointCross
from methods.implementations.fill_all import fill_all

file_list = [('TP2/allitems/armas-short.tsv', Weapon), ('TP2/allitems/botas-short.tsv', Boots), ('TP2/allitems/cascos-short.tsv',
                                                                                                 Helmet), ('TP2/allitems/guantes-short.tsv', Gloves), ('TP2/allitems/pecheras-short.tsv', Armor)]
item_handler = ItemHandler(file_list)
data = None

with open('TP2/config.json', 'r') as json_file:
    data = json.load(json_file)

    character_class = data['class']
    population_amount = data['population_amount']
    individuals_amount = data['individuals_amount']
    individual_mutation_probability = data['individual_mutation_probability']
    selection_method = data["methods"]["selection"]

# Build Generation 0
characters = []

for i in range(population_amount):
    equipment = item_handler.getEquipment()
    char = None
    height = random.uniform(1.3, 2)
    char = Character(i, height, equipment,
                        CharacterClass[character_class.upper()])
    characters.append(char)
    # print(char)

# Parents Selection
parents = elite(characters, individuals_amount, population_amount)

# Pair parent for crossover
parents1 = parents[0::2]
parents2 = parents[1::2]

# Crossover --> get children
# children = onePointCross(parents, CharacterClass[character_class.upper()])

# Mutate children

individual = parents[0]  # CHILDREN !
print(individual)
print(individual.height)
print(individual.equipment)
print("---------------------------")
if individual_mutation_probability < MutationLib.getMutationProbability():
    individual = uniformMultigenMutation(individual, item_handler, individual_mutation_probability)
print(individual)
print(individual.height)
print(individual.equipment)

# Get new Generation


# Get new Generation
#print("-------------------- REPLACEMENT ----------------------")
 
#characters = fill_all(characters, children,
#                     individuals_amount, population_amount)
#print(characters)

# print(parents)

# print(parents)
