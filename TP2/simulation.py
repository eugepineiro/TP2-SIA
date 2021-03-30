from data_handler import mutation, selection, crossover
from Characters.character_class import CharacterClass
from methods.mutations import MutationLib
from methods.implementations import fill_all
from constants import *
import math, plotter
import time
from methods.implementations import replacement
ERROR = 0.01
equipment_types = ["Weapon", "Boots", "Helmet", "Gloves", "Armor"]

def avg_fitness(characters):
    return sum(list(map(lambda character: character.fitness,characters))) / len(characters)

def compare_height(h1,h2):
    return abs(h1-h2) < ERROR

def compare_equipment(e1,e2):
    for item in equipment_types:
        i1 = e1[item]
        i2 = e2[item]
        if not abs(i1.force - i2.force) < ERROR or not abs(i1.agility - i2.agility) < ERROR or not abs(i1.expertise - i2.expertise) < ERROR or not abs(i1.resistance - i2.resistance) < ERROR or not abs(i1.life - i2.life) < ERROR: 
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
    size = len(characters)
    return (diff / ((size-1)*size)/2) * 100

#def get_diversity_by_stats(characters): #dos individuos son iguales si tienen la misma fuerza y la misma pericia y agilidad etc con un delta
    
    
#def get_diversity_by_fitness(characters): #dos individuos son iguales si tienen el mismo fitness con un delta
    
    
    

def max_fitness(characters):
    return max(list(map(lambda character: character.fitness, characters)))

def generationCut(cant_gens, data, item_handler, characters, plotter, iteration_func):
    for i in range(cant_gens):
        characters = iteration_func(data, item_handler, characters, plotter, i)

def timeCut(max_time, data, item_handler, characters, plotter, iteration_func):
    start = end = time.time()
    generation = 0
    while (end - start) <= max_time:
        characters = iteration_func(data, item_handler, characters, plotter, generation)
        generation += 1
        end = time.time()

def contentCut(max_generation, data, item_handler, characters, plotter, iteration_func):
    generation = 0
    last_fitness = 0
    gen_counter = 0

    while gen_counter < max_generation:
        characters = iteration_func(data, item_handler, characters, plotter, generation)

        best_fit = max_fitness(characters)

        if best_fit != last_fitness:
            last_fitness = best_fit
            gen_counter = 0
        else:
            gen_counter += 1

        generation += 1

def structureCut(max_diversity, data, item_handler, characters, plotter, iteration_func):
    MAX_GENERATIONS = 20
    generation = 0
    gen_counter = 0

    while gen_counter < MAX_GENERATIONS:
        characters = iteration_func(data, item_handler, characters, plotter, generation)

        diversity = get_diversity(characters)

        if diversity >= max_diversity:
            gen_counter = 0
        else:
            gen_counter += 1

        generation += 1

def solutionCut(min_fitness, data, item_handler, characters, graph, iteration_func): 
    
    generation = 0

    while True: 
        characters = iteration_func(data, item_handler, characters, plotter, generation)
        avg_fit = avg_fitness(characters)
        if avg_fit >= min_fitness:
            return

        generation += 1
    


def cutting(method, parameter, data, item_handler, characters, iteration_func):
    graph = plotter
    graph.update_plots(0,min(map(lambda character: character.fitness,characters)),avg_fitness(characters),get_diversity(characters),max(map(lambda character: character.fitness,characters)))

    if method == GENERATION_CUT:
        generationCut(parameter, data, item_handler, characters, graph, iteration_func)
    elif method == TIME_CUT:
        timeCut(parameter, data, item_handler, characters, graph, iteration_func)
    elif method == CONTENT_CUT:
        contentCut(parameter, data, item_handler, characters, graph, iteration_func)
    elif method == STRUCTURE_CUT:
        structureCut(parameter, data, item_handler, characters, graph, iteration_func)
    elif method == SOLUTION_CUT:
        solutionCut(parameter, data, item_handler, characters, graph, iteration_func)
    else:
        return

    graph.show()

def runIteration(data, item_handler, characters, plotter, generation):

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

    # Parents Selection 
    print("-------------------- SELECTION ----------------------")
    #parents = elite(characters, individuals_amount, population_amount)
    first_cut = math.ceil(individuals_amount*selection_prob)
    second_cut = math.floor(individuals_amount*(1-selection_prob))
    parents1 = selection(selection_method_a, characters, first_cut,population_amount, generation+1)
    parents2 = selection(selection_method_b, characters, second_cut,population_amount, generation+1)
    parents = parents1 + parents2
    print(parents)
    print(len(parents))
    
    # Pair parent for crossover 
    parents1 = parents[0::2]
    parents2 = parents[1::2] 
    # Crossover --> get children  
    print("-------------------- CROSSOVER ----------------------")

    children = crossover(crossover_func, parents1, parents2, CharacterClass[character_class.upper()])
    # print(children)


    # Mutate children (para cada hijo chequeo --> si cumple con Pm --> lo muto, sino sigo)
    print("-------------------- MUTATION ----------------------")
    min_fitness = 20
    for c in children :
        if c.fitness < min_fitness :
            min_fitness = c.fitness
    print("MIN FITNESS BEFORE MUTATION: %d" %min_fitness)
        
    #print(children)
    for j,individual in enumerate(children):
        if individual_mutation_probability > MutationLib.getMutationProbability():
            children[j] = mutation(mutation_method, individual, item_handler, individual_mutation_probability)
    #print(children)
    min_fitness = 20
    for c in children :
        if c.fitness < min_fitness :
            min_fitness = c.fitness
    print("MIN FITNESS AFTER MUTATION: %d" %min_fitness)

    # Get new Generation
    print("-------------------- REPLACEMENT ----------------------")
    characters = replacement(implementation,characters,children,individuals_amount, population_amount,replacement_a,replacement_b,replacement_prob,generation=generation+1)
    # print(characters)
    # print(len(characters))
    plotter.update_plots(generation + 1,min(map(lambda character: character.fitness,characters)),avg_fitness(characters),get_diversity(characters),max(map(lambda character: character.fitness,characters)))

    return characters

def runSimulation(data, item_handler, characters):
    cutting_method = data["cutting_condition"]["method"]
    cutting_param = data["cutting_condition"]["parameter"]
    cutting(cutting_method, cutting_param, data, item_handler, characters, runIteration)

