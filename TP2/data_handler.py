from constants import *
from methods.mutations import oneGenMutation, completeMutation, limitedMultigenMutation, uniformMultigenMutation
from methods.selections import elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments

def selection(method, characters, individuals_amount, population_amount,generation):

    if method == ELITE_S :
        return elite(characters, individuals_amount, population_amount)
    elif method == ROULETTE_S:
        return roulette(characters, individuals_amount)
    elif method == UNIVERSAL_S: 
        return universal(characters, individuals_amount)
    elif method == RANKING_S: 
        return ranking(characters,individuals_amount,population_amount)
    elif method == BOLTZMANN: 
        return boltzmann(characters, individuals_amount, population_amount,generation)
    elif method == D_TOURNAMENTS_S:
        #TODO: CHANGE 
        m_value = 10 
        return d_tournaments(characters, individuals_amount, population_amount, m_value)
    elif method == P_TOURNAMENTS_S: 
        return p_tournaments(characters,individuals_amount,population_amount)
    


def mutation(method, individual, item_handler, individual_mutation_probability):

    if method == ONE_GEN_M:
        return oneGenMutation(individual, item_handler)
    elif method == COMPLETE_M: 
        return completeMutation(individual, item_handler)
    elif method == LIMITED_MULTIGEN_M:
        return limitedMultigenMutation(individual, item_handler)
    elif method == UNIFORM_MULTIGEN_M: 
        return uniformMultigenMutation(individual, item_handler, individual_mutation_probability)
