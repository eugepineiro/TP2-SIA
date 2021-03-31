import math
from constants import *

def replacement(data_handler, old_generation, children, generation):
    if data_handler.implementation == FILL_ALL_I:
        return fill_all(old_generation, children, data_handler, generation)
    elif data_handler.implementation == FILL_PARENT_I:
        return fill_parent(old_generation,children, data_handler, generation)

def fill_all(old_generation, children, data_handler, generation): # individuals_amount,population_amount,replacement_a,replacement_b,replacement_prob, threshold
    join = old_generation + children   # N de la actual + k hijos
    n = data_handler.population_amount
    replacement_a = data_handler.replacement_a
    replacement_b = data_handler.replacement_b
    replacement_prob = data_handler.replacement_prob

    
    first = data_handler.selection(replacement_a,join,math.floor(n*replacement_prob),len(join),generation)
    second = data_handler.selection(replacement_b,join,math.ceil(n*(1-replacement_prob)),len(join),generation)

    return first + second


def fill_parent(old_generation,children, data_handler, generation): # individuals_amount,population_amount,replacement_a,replacement_b,replacement_prob, threshold
    k = data_handler.individuals_amount
    n = data_handler.population_amount
    replacement_a = data_handler.replacement_a
    replacement_b = data_handler.replacement_b
    replacement_prob = data_handler.replacement_prob

    if k > n:
        selected_children1 = data_handler.selection(replacement_a,children,math.floor(n*replacement_prob),len(children),generation)
        selected_children2 = data_handler.selection(replacement_b,children,math.ceil(n*(1-replacement_prob)),len(children),generation)
        return selected_children1 + selected_children2
    elif k == n:
        return children
    selected_old1 = data_handler.selection(replacement_a,old_generation,math.floor((n-k)*replacement_prob),len(old_generation),generation)
    selected_old2 = data_handler.selection(replacement_b,old_generation,math.ceil((n-k)*(1-replacement_prob)),len(old_generation),generation)
    return children + selected_old1 + selected_old2
    