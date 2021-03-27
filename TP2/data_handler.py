from constants import *
from methods.mutations.one_gen_mutation import oneGenMutation
from methods.mutations.complete_mutation import completeMutation
from methods.mutations.limited_multigen_mutation import limitedMultigenMutation
from methods.mutations.uniform_multigen_mutation import uniformMultigenMutation

def mutation(method, individual, item_handler, individual_mutation_probability):

    if method == ONE_GEN_M:
        return oneGenMutation(individual, item_handler)
    elif method == COMPLETE_M: 
        return completeMutation(individual, item_handler)
    elif method == LIMITED_MULTIGEN_M:
        return limitedMultigenMutation(individual, item_handler)
    elif method == UNIFORM_MULTIGEN_M: 
        return uniformMultigenMutation(individual, item_handler, individual_mutation_probability)

