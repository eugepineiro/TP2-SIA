from methods.selections import elite
import math
methods = {
    'elite': elite
}

def fill_all(old_generation,children,k,n,replacement_a,replacement_b,B):
    join = old_generation + children
    first = methods[replacement_a](join, k, n)
    second = methods[replacement_b](join, k, n)
    first_cut = math.ceil(len(first)*B)
    second_cut = math.floor(len(second)*B)
    final_join = first[:first_cut] + second[:second_cut]
    return final_join


    