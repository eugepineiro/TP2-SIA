from methods.selections import elite, roulette, d_tournaments
import math
methods = {
    'elite': elite
}

def fill_all(old_generation,children,k,n,replacement_a,replacement_b,replacement_prob):
    join = old_generation + children   # N de la actual + k hijos
    first_cut = math.ceil(n*replacement_prob)
    second_cut = math.floor(n*(1-replacement_prob))
    first = methods[replacement_a](join, first_cut, n)
    second = d_tournaments(join, k,n,10)
    # second = methods[replacement_b](join, k, n)
    
    final_join = first + second
    return final_join


    