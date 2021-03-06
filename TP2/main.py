# crear un personaje --> conseguir el array de items que le tiene que pasar --> abre los tsv y elige uno de cada PONELE QUE DE FORMA RANDOM
# el mejor personaje --> genes: h, equipment
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

import json, random
# Population
from Characters.character import Character
from simulation import runSimulation
from item_handler import ItemHandler
from Items.armor import Armor
from Items.boots import Boots
from Items.gloves import Gloves
from Items.helmet import Helmet
from Items.weapon import Weapon
from constants import *
import plotter, math
from data_handler import DataHandler
from methods.mutations import MutationLib
from methods.implementations import replacement
# Impl

# file_list = [('TP2/allitems/armas-short.tsv', Weapon), ('TP2/allitems/botas-short.tsv', Boots), ('TP2/allitems/cascos-short.tsv', Helmet), ('TP2/allitems/guantes-short.tsv', Gloves), ('TP2/allitems/pecheras-short.tsv', Armor)]

data = None

def avg_fitness(characters):
    return sum(list(map(lambda character: character.fitness,characters))) / len(characters)



with open('TP2/config.json', 'r') as json_file:
    data = json.load(json_file)
    data_handler = DataHandler(data)
    # population_amount = data['population_amount']
    # character_class = data['class']
file_list = [(data_handler.dataset_weapons, Weapon), (data_handler.dataset_boots, Boots), (data_handler.dataset_helmets, Helmet), (data_handler.dataset_gloves, Gloves), (data_handler.dataset_armors, Armor)]
item_handler = ItemHandler(file_list) 
# Build Generation 0
characters = []
for i in range(data_handler.population_amount):
    equipment = item_handler.getEquipment()
    char = None
    height = random.uniform(MIN_HEIGHT, MAX_HEIGHT)
    char = Character(i, height, equipment, data_handler.character_class)
    characters.append(char)
    # print(char)

runSimulation(data_handler, item_handler, characters)
