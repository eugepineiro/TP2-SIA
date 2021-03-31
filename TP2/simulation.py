from data_handler import DataHandler
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

def generationCut(data_handler, item_handler, characters, plotter, iteration_func): # cant_gens, data,
    cant_gens = data_handler.cutting_param
    for i in range(cant_gens):
        characters = iteration_func(data_handler, item_handler, characters, plotter, i)

def timeCut(data_handler, item_handler, characters, plotter, iteration_func): # max_time
    max_time = data_handler.cutting_param
    start = end = time.time()
    generation = 0
    while (end - start) <= max_time:
        characters = iteration_func(data_handler, item_handler, characters, plotter, generation)
        generation += 1
        end = time.time()

def contentCut(data_handler, item_handler, characters, plotter, iteration_func): # max_generation
    max_generation = data_handler.cutting_param
    generation = 0
    last_fitness = 0
    gen_counter = 0

    while gen_counter < max_generation:
        characters = iteration_func(data_handler, item_handler, characters, plotter, generation)

        best_fit = max_fitness(characters)

        if best_fit != last_fitness:
            last_fitness = best_fit
            gen_counter = 0
        else:
            gen_counter += 1

        generation += 1

def structureCut(data_handler, item_handler, characters, plotter, iteration_func): # max_diversity
    max_diversity = data_handler.cutting_param
    MAX_GENERATIONS = 20 
    generation = 0
    gen_counter = 0

    while gen_counter < MAX_GENERATIONS:
        characters = iteration_func(data_handler, item_handler, characters, plotter, generation)

        diversity = get_diversity(characters)

        if diversity >= max_diversity:
            gen_counter = 0
        else:
            gen_counter += 1

        generation += 1

def solutionCut(data_handler, item_handler, characters, graph, iteration_func): # min_fitness
    min_fitness = data_handler.cutting_param
    generation = 0

    while True: 
        characters = iteration_func(data_handler, item_handler, characters, plotter, generation)
        avg_fit = avg_fitness(characters)
        if avg_fit >= min_fitness:
            return

        generation += 1
    


def cutting(data_handler, item_handler, characters, iteration_func): # cutting_method, cutting_param, data,
    
    graph = plotter
    graph.init_plot(data_handler.character_class)
    graph.update_plots(0,min(map(lambda character: character.fitness,characters)),avg_fitness(characters),get_diversity(characters),max(map(lambda character: character.fitness,characters)))

    if data_handler.cutting_method == GENERATION_CUT:
        generationCut(data_handler, item_handler, characters, graph, iteration_func)
    elif data_handler.cutting_method == TIME_CUT:
        timeCut(data_handler, item_handler, characters, graph, iteration_func)
    elif data_handler.cutting_method == CONTENT_CUT:
        contentCut(data_handler, item_handler, characters, graph, iteration_func)
    elif data_handler.cutting_method == STRUCTURE_CUT:
        structureCut(data_handler, item_handler, characters, graph, iteration_func)
    elif data_handler.cutting_method == SOLUTION_CUT:
        solutionCut(data_handler, item_handler, characters, graph, iteration_func)
    else:
        return

    graph.show()

def runIteration(data_handler, item_handler, characters, plotter, generation):

    # population_amount = data['population_amount']
    # character_class = data['class']
    # individuals_amount = data['individuals_amount']
    # individual_mutation_probability = data['individual_mutation_probability']
    # selection_method_a = data["methods"]["selection_a"]
    # selection_method_b = data["methods"]["selection_b"]
    # mutation_method = data["methods"]["mutation"]
    # replacement_a = data["methods"]["replacement_a"]
    # replacement_b = data["methods"]["replacement_b"]
    # selection_prob = data["methods"]["selection_prob"]
    # replacement_prob = data["methods"]["replacement_prob"]
    # implementation = data["implementation"]
    # crossover_func = data["methods"]["crossover"] 
    # threshold = data["methods"]["selection_params"]["p_tournaments_threshold"] 

    # Parents Selection 
    print("-------------------- SELECTION ----------------------")
    first_cut = math.floor(data_handler.individuals_amount*data_handler.selection_prob)
    second_cut = math.ceil(data_handler.individuals_amount*(1-data_handler.selection_prob))
    parents1 = data_handler.selection(data_handler.selection_method_a, characters, first_cut, data_handler.population_amount, generation+1)
    parents2 = data_handler.selection(data_handler.selection_method_b, characters, second_cut, data_handler.population_amount, generation+1)
    parents = parents1 + parents2
    # print(parents)
    # print(len(parents))
    
    # Pair parent for crossover 
    parents1 = parents[0::2]
    parents2 = parents[1::2] 
    # Crossover --> get children  
    print("-------------------- CROSSOVER ----------------------")

    children = data_handler.crossover(parents1, parents2)
    # print(children)


    # Mutate children (para cada hijo chequeo --> si cumple con Pm --> lo muto, sino sigo)
    print("-------------------- MUTATION ----------------------")
    min_fitness = 20
    # for c in children :
        # if c.fitness < min_fitness :
            # min_fitness = c.fitness
    # print("MIN FITNESS BEFORE MUTATION: %d" %min_fitness)
        
    #print(children)
    for j,individual in enumerate(children):
        if data_handler.individual_mutation_probability > MutationLib.getMutationProbability():
            children[j] = data_handler.mutation(individual, item_handler)
    #print(children)
    min_fitness = 20
    # for c in children :
        # if c.fitness < min_fitness :
            # min_fitness = c.fitness
    # print("MIN FITNESS AFTER MUTATION: %d" %min_fitness)

    # Get new Generation
    print("-------------------- REPLACEMENT ----------------------")
    print(len(characters))

    characters = replacement(data_handler, characters, children, generation=generation+1)
    print(len(characters))
    plotter.update_plots(generation + 1,min(map(lambda character: character.fitness,characters)),avg_fitness(characters),get_diversity(characters),max(map(lambda character: character.fitness,characters)))

    return characters

def runSimulation(data_handler, item_handler, characters):
    cutting(data_handler, item_handler, characters, runIteration)

