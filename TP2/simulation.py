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
    return get_diversity_by_genes(characters)


def get_diversity_by_genes(characters): 
    diff = 0
    # Iterate through all but last characters
    for i,char1 in enumerate(characters[:-1]):
        # Iterate throught all characters with higher index than char1
        for char2 in characters[i+1:]:
            if not compare_height(char1.height,char2.height) or not compare_equipment(char1.equipment,char2.equipment):
                diff += 1
    size = len(characters) 
    total = ((size-1)*size)/2.0
    return (diff / int(total)) * 100

def get_diversity_by_fitness(characters): 
    diff = 0
    for char1 in characters: 
        for char2 in characters: 
            if abs(char1.fitness - char2.fitness) >= ERROR : 
                diff += 1
    
    size = len(characters)
    return (diff / pow(size-1, size )) * 100
                

def max_fitness(characters):
    return max(list(map(lambda character: character.fitness, characters)))

def generationCut(data_handler, item_handler, characters, plotter, iteration_func): # cant_gens, data,
    cant_gens = data_handler.cutting_param
    for i in range(cant_gens):
        characters = iteration_func(data_handler, item_handler, characters, plotter, i)
    return characters

def timeCut(data_handler, item_handler, characters, plotter, iteration_func): # max_time
    max_time = data_handler.cutting_param
    start = end = time.time()
    generation = 0
    while (end - start) <= max_time:
        characters = iteration_func(data_handler, item_handler, characters, plotter, generation)
        generation += 1
        end = time.time()
    return characters

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
    return characters

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
    return characters

def solutionCut(data_handler, item_handler, characters, graph, iteration_func): # min_fitness
    min_fitness = data_handler.cutting_param
    generation = 0

    while True: 
        characters = iteration_func(data_handler, item_handler, characters, plotter, generation)
        avg_fit = avg_fitness(characters)
        if avg_fit >= min_fitness:
            return characters

        generation += 1
        
    


def cutting(data_handler, item_handler, characters, iteration_func): # cutting_method, cutting_param, data,
    
    graph = plotter
    graph.init_plot(data_handler.character_class)
    graph.update_plots(0,min(map(lambda character: character.fitness,characters)),avg_fitness(characters),get_diversity(characters),max(map(lambda character: character.fitness,characters)))
    final_characters = None
    if data_handler.cutting_method == GENERATION_CUT:
        final_characters= generationCut(data_handler, item_handler, characters, graph, iteration_func)
    elif data_handler.cutting_method == TIME_CUT:
        final_characters = timeCut(data_handler, item_handler, characters, graph, iteration_func)
    elif data_handler.cutting_method == CONTENT_CUT:
        final_characters = contentCut(data_handler, item_handler, characters, graph, iteration_func)
    elif data_handler.cutting_method == STRUCTURE_CUT:
        final_characters = structureCut(data_handler, item_handler, characters, graph, iteration_func)
    elif data_handler.cutting_method == SOLUTION_CUT:
        final_characters = solutionCut(data_handler, item_handler, characters, graph, iteration_func)
    else:
        return
    best = final_characters[0]
    for character in final_characters[1:]:
        if character.fitness > best.fitness:
            best = character
    print("Best character is")
    print(best)
    print("'Height': %g" %best.height)
    for item in best.equipment.items():
        print(item)
    graph.show()

def runIteration(data_handler, item_handler, characters, plotter, generation):
    aux_chars = characters.copy()
    # Parents Selection 
    first_cut = math.floor(data_handler.individuals_amount*data_handler.selection_prob)
    second_cut = math.ceil(data_handler.individuals_amount*(1-data_handler.selection_prob))
    parents1 = data_handler.selection(data_handler.selection_method_a, characters, first_cut, data_handler.population_amount, generation+1)
    parents2 = data_handler.selection(data_handler.selection_method_b, characters, second_cut, data_handler.population_amount, generation+1)
    parents = parents1 + parents2
    
    # Pair parent for crossover 
    parents1 = parents[0::2]
    parents2 = parents[1::2] 
    
    # Crossover --> get children  
    children = data_handler.crossover(parents1, parents2)
   
    # Mutate children (para cada hijo chequeo --> si cumple con Pm --> lo muto, sino sigo)
    for j,individual in enumerate(children):
        if data_handler.individual_mutation_probability > MutationLib.getMutationProbability(): 
            children[j] = data_handler.mutation(individual, item_handler) 
 
    # Get new Generation
    characters = replacement(data_handler, characters, children, generation=generation+1)
    plotter.update_plots(generation + 1,min(map(lambda character: character.fitness,characters)),avg_fitness(characters),get_diversity(characters),max(map(lambda character: character.fitness,characters)))
   # print("DIVERSITY %d" %generation)
    #if(get_diversity(aux_chars) < get_diversity(characters)): 
     #   print(aux_chars)
      #  print(characters)
    
    return characters

def runSimulation(data_handler, item_handler, characters):
    cutting(data_handler, item_handler, characters, runIteration)

