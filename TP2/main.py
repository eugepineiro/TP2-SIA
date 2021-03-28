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
from Characters.character_class import CharacterClass
from simulation import runSimulation
from item_handler import ItemHandler
from Items.armor import Armor
from Items.boots import Boots
from Items.gloves import Gloves
from Items.helmet import Helmet
from Items.weapon import Weapon
from constants import *
import plotter, math
from data_handler import mutation, selection, crossover
from methods.mutations import MutationLib
from methods.implementations import replacement
# Impl

# file_list = [('TP2/allitems/armas-short.tsv', Weapon), ('TP2/allitems/botas-short.tsv', Boots), ('TP2/allitems/cascos-short.tsv', Helmet), ('TP2/allitems/guantes-short.tsv', Gloves), ('TP2/allitems/pecheras-short.tsv', Armor)]
file_list = [('TP2/allitems/armas.tsv', Weapon), ('TP2/allitems/botas.tsv', Boots), ('TP2/allitems/cascos.tsv', Helmet), ('TP2/allitems/guantes.tsv', Gloves), ('TP2/allitems/pecheras.tsv', Armor)]
item_handler = ItemHandler(file_list) 
data = None
ERROR = 0.001

def avg_fitness(characters):
    return sum(list(map(lambda character: character.fitness,characters))) / len(characters)

def compare_height(h1,h2):
    return abs(h1-h2) < ERROR

def compare_equipment(e1,e2):
    items = list(map(lambda elem: elem[1].__str__(None) ,file_list))
    for item_type in items:
        if not e1[item_type] == e2[item_type]:
            return False
    return True

def get_diversity(characters):
    diff = 0
    # Iterate through all but last characters
    for i,char1 in enumerate(characters[:-1]):
        # Iterate throught all characters with higher index than char1
        for char2 in characters[i+1:]:
            if not compare_height(char1.height,char2.height) or not compare_equipment(char1.equipment,char2.equipment):
                diff += 1
    return diff

with open('TP2/config.json', 'r') as json_file:
    data = json.load(json_file)
    population_amount = data['population_amount']
    character_class = data['class']
    individuals_amount = data['individuals_amount']
    individual_mutation_probability = data['individual_mutation_probability']
    selection_method_a = data["methods"]["selection_a"]
    selection_method_b = data["methods"]["selection_b"]
    mutation_method = data["methods"]["mutation"]
    replacement_a = data["methods"]["replacement_a"]
    replacement_b = data["methods"]["replacement_b"]
    selection_prob = data["methods"]["selection_prob"]
    replacement_prob = data["methods"]["replacement_prob"]
    implementation = data["implementation"]
    crossover_func = data["methods"]["crossover"]

# Build Generation 0
characters = []
for i in range(population_amount):
    equipment = item_handler.getEquipment()
    char = None
    height = random.uniform(MIN_HEIGHT, MAX_HEIGHT)
    char = Character(i, height, equipment, CharacterClass[character_class.upper()])
    characters.append(char)
    # print(char)
plotter.update_plots(0,min(map(lambda character: character.fitness,characters)),avg_fitness(characters),get_diversity(characters))

for i in range(50):
    print("-------------------- GENERATION {i} ----------------------".format(i=i))
    # Parents Selection 
    print("-------------------- SELECTION ----------------------")
    #parents = elite(characters, individuals_amount, population_amount)
    first_cut = math.ceil(individuals_amount*selection_prob)
    second_cut = math.floor(individuals_amount*(1-selection_prob))
    parents1 = selection(selection_method_a, characters, first_cut,population_amount,generation=i+1)
    parents2 = selection(selection_method_b, characters, second_cut,population_amount,generation=i+1)
    parents = parents1 + parents2
    # print(parents)
    # print(len(parents))
    
    # Pair parent for crossover 
    parents1 = parents[0::2]
    parents2 = parents[1::2] 
    # Crossover --> get children  
    print("-------------------- CROSSOVER ----------------------")
    children = crossover(crossover_func, parents1, parents2, CharacterClass[character_class.upper()])

    # print(children)


    # Mutate children (para cada hijo chequeo --> si cumple con Pm --> lo muto, sino sigo)
    print("-------------------- MUTATION ----------------------")

    # print(children)
    for j,individual in enumerate(children):
        if individual_mutation_probability > MutationLib.getMutationProbability():
            children[j] = mutation(mutation_method, individual, item_handler, individual_mutation_probability)
    # print(children)


    # Get new Generation
    print("-------------------- REPLACEMENT ----------------------")
    characters = replacement(implementation,characters,children,individuals_amount, population_amount,replacement_a,replacement_b,replacement_prob,generation=i+1)
    # print(characters)
    # print(len(characters))
    plotter.update_plots(i+1,min(map(lambda character: character.fitness,characters)),avg_fitness(characters),get_diversity(characters))

plotter.show()

# runSimulation(data, item_handler, characters)
