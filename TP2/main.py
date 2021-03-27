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

import json, csv, random
# Population
from Characters.character import Character
from Characters.character_class import CharacterClass
from item_handler import ItemHandler
from Items.armor import Armor
from Items.boots import Boots
from Items.gloves import Gloves
from Items.helmet import Helmet
from Items.weapon import Weapon
from constants import *
# Selection
from methods.selections import elite, roulette
# Crossover
from methods.crossovers import onePointCross, twoPointsCross, annularCross, uniformCross
# Mutation
from data_handler import mutation, selection
from methods.mutations import MutationLib
# Impl
from methods.implementations.fill_all import fill_all
from methods.implementations.fill_parent import fill_parent

import plotter

file_list = [('TP2/allitems/armas-short.tsv', Weapon), ('TP2/allitems/botas-short.tsv', Boots), ('TP2/allitems/cascos-short.tsv', Helmet), ('TP2/allitems/guantes-short.tsv', Gloves), ('TP2/allitems/pecheras-short.tsv', Armor)]
item_handler = ItemHandler(file_list) 
data = None

with open('TP2/config.json', 'r') as json_file:
    data = json.load(json_file)

    character_class = data['class']
    population_amount = data['population_amount']
    individuals_amount = data['individuals_amount']
    individual_mutation_probability = data['individual_mutation_probability']
    selection_method_a = data["methods"]["selection_a"]
    selection_method_b = data["methods"]["selection_b"]
    mutation_method = data["methods"]["mutation"]
    replacement_a = data["methods"]["replacement_a"]
    replacement_b = data["methods"]["replacement_b"]
    A = float(data["A"]) 
    B = float(data["B"])

# Build Generation 0
characters = []

for i in range(population_amount):
    equipment = item_handler.getEquipment()
    char = None
    height = random.uniform(MIN_HEIGHT, MAX_HEIGHT)
    char = Character(i, height, equipment, CharacterClass[character_class.upper()])
    characters.append(char)
    # print(char)

# plotter.init_plot()

for i in range(10):

    # Parents Selection 
    print("-------------------- SELECTION ----------------------")
    #parents = elite(characters, individuals_amount, population_amount)
    parents = selection(selection_method_a, characters, individuals_amount,population_amount)
    print(parents)
    
    # Pair parent for crossover 
    parents1 = parents[0::2]
    parents2 = parents[1::2] 
    # Crossover --> get children  
    print("-------------------- CROSSOVER ----------------------")

    children = twoPointsCross(parents1, parents2, CharacterClass[character_class.upper()])
    # print(children)


    # Mutate children (para cada hijo chequeo --> si cumple con Pm --> lo muto, sino sigo)
    print("-------------------- MUTATION ----------------------")
    individual = parents[0]  # CHILDREN !
    print(individual)
    print("---------------------------")
    if individual_mutation_probability < MutationLib.getMutationProbability():
        individual = mutation(mutation_method, individual, item_handler, individual_mutation_probability)
    print(individual)


    # Get new Generation
    print("-------------------- REPLACEMENT ----------------------")
    characters = fill_parent(characters,children,individuals_amount, population_amount,replacement_a,replacement_b,B)
    print(characters)
    
    plotter.update_plots(i,min(map(lambda character: character.fitness,characters)),0,0)

    # a = random.randint(1,60)
    # b = random.randint(1,60)
    # c = random.randint(1,60)
    
    # plotter.update_plots(i,a,b,c)
    
plotter.show()
