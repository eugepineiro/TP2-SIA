from constants import *
from methods.mutations import oneGenMutation, completeMutation, limitedMultigenMutation, uniformMultigenMutation
from methods.selections import elite, rouletteOrUniversal

def selection(method, characters, individuals_amount, population_amount):

    if method == ELITE_S :
        return elite(characters, individuals_amount, population_amount)
    elif method == ROULETTE_S or UNIVERSAL_S: 
        return rouletteOrUniversal(method,characters, individuals_amount)
    elif method == RANKING_S: 
        return 
    elif method == BOLTZMANN: 
        return 
    elif method == D_TOURNAMENTS_S: 
        return 
    elif method == P_TOURNAMENTS_S: 
        return


def mutation(method, individual, item_handler, individual_mutation_probability):

    if method == ONE_GEN_M:
        return oneGenMutation(individual, item_handler)
    elif method == COMPLETE_M: 
        return completeMutation(individual, item_handler)
    elif method == LIMITED_MULTIGEN_M:
        return limitedMultigenMutation(individual, item_handler)
    elif method == UNIFORM_MULTIGEN_M: 
        return uniformMultigenMutation(individual, item_handler, individual_mutation_probability)



