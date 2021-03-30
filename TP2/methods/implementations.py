from data_handler import selection
import math
from constants import *

def replacement(method, old_generation, children, individuals_amount, population_amount,replacement_a, replacement_b, replacement_prob,generation):
    if method == FILL_ALL_I:
        return fill_all(old_generation,children,individuals_amount,population_amount,replacement_a,replacement_b,replacement_prob,generation)
    elif method == FILL_PARENT_I:
        return fill_parent(old_generation,children,individuals_amount,population_amount,replacement_a,replacement_b,replacement_prob,generation)

def fill_all(old_generation,children,k,n,replacement_a,replacement_b,replacement_prob,generation):
    join = old_generation + children   # N de la actual + k hijos
    
    first = selection(replacement_a,join,math.floor(n*replacement_prob),len(join),generation)
    second = selection(replacement_b,join,math.ceil(n*(1-replacement_prob)),len(join),generation)

    return first + second


def fill_parent(old_generation,children,k,n,replacement_a,replacement_b,replacement_prob,generation):
    if k > n:
        selected_children1 = selection(replacement_a,children,math.floor(n*replacement_prob),len(children),generation)
        selected_children2 = selection(replacement_b,children,math.ceil(n*(1-replacement_prob)),len(children),generation)
        return selected_children1 + selected_children2
    elif k == n:
        return children
    selected_old1 = selection(replacement_a,old_generation,math.floor((n-k)*replacement_prob),len(old_generation),generation)
    selected_old2 = selection(replacement_b,old_generation,math.ceil((n-k)*(1-replacement_prob)),len(old_generation),generation)
    return children + selected_old1 + selected_old2
    