from data_handler import mutation, selection, crossover
from Characters.character_class import CharacterClass
from methods.mutations import MutationLib
from methods.implementations.fill_all import fill_all
from constants import *
import math, plotter
import time

def avg_fitness(characters):
    return sum(list(map(lambda character: character.fitness,characters))) / len(characters)

def get_diversity(characters):
    return sum(list(map(lambda character: character.fitness,characters))) / len(characters)

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

def cutting(method, parameter, data, item_handler, characters, iteration_func):
    graph = plotter
    if method == GENERATION_CUT:
        generationCut(parameter, data, item_handler, characters, graph, iteration_func)
    elif method == TIME_CUT:
        timeCut(parameter, data, item_handler, characters, graph, iteration_func)
    elif method == CONTENT_CUT:
        contentCut(parameter, data, item_handler, characters, graph, iteration_func)
    else:
        return

    graph.show()

def runIteration(data, item_handler, characters, plotter, generation):

    character_class = data['class']
    population_amount = data['population_amount']
    individuals_amount = data['individuals_amount']
    individual_mutation_probability = data['individual_mutation_probability']
    selection_method_a = data["methods"]["selection_a"]
    selection_method_b = data["methods"]["selection_b"]
    crossover_method = data["methods"]["crossover"]
    mutation_method = data["methods"]["mutation"]
    replacement_a = data["methods"]["replacement_a"]
    replacement_b = data["methods"]["replacement_b"]
    selection_prob = data["methods"]["selection_prob"]
    replacement_prob = data["methods"]["replacement_prob"]

    # Parents Selection 
    print("-------------------- SELECTION ----------------------")
    #parents = elite(characters, individuals_amount, population_amount)
    first_cut = math.ceil(individuals_amount*selection_prob)
    second_cut = math.floor(individuals_amount*(1-selection_prob))
    parents1 = selection(selection_method_a, characters, first_cut,population_amount, generation)
    parents2 = selection(selection_method_b, characters, second_cut,population_amount, generation)
    parents = parents1 + parents2
    print(parents)
    print(len(parents))
    
    # Pair parent for crossover 
    parents1 = parents[0::2]
    parents2 = parents[1::2] 
    # Crossover --> get children  
    print("-------------------- CROSSOVER ----------------------")

    children = crossover(crossover_method, parents1, parents2, CharacterClass[character_class.upper()])
    # print(children)


    # Mutate children (para cada hijo chequeo --> si cumple con Pm --> lo muto, sino sigo)
    print("-------------------- MUTATION ----------------------")

    print(children)
    for j,individual in enumerate(children):
        if individual_mutation_probability > MutationLib.getMutationProbability():
            children[j] = mutation(mutation_method, individual, item_handler, individual_mutation_probability)
    print(children)


    # Get new Generation
    print("-------------------- REPLACEMENT ----------------------")
    characters = fill_all(characters,children,individuals_amount, population_amount,replacement_a,replacement_b,replacement_prob)
    # print(characters)
    # print(len(characters))
    plotter.update_plots(generation, min(map(lambda character: character.fitness,characters)), avg_fitness(characters), get_diversity(characters))

    return characters

def runSimulation(data, item_handler, characters):
    cutting_method = data["cutting_condition"]["method"]
    cutting_param = data["cutting_condition"]["parameter"]
    cutting(cutting_method, cutting_param, data, item_handler, characters, runIteration)

