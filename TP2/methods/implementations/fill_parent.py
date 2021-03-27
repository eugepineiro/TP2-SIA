from methods.selections.elite import elite
import math

methods = {
    'elite': elite
}

def fill_parent(old_generation,children,k,n,replacement_a,replacement_b,B):
    if k > n:
        selected_children1 = methods[replacement_a](children, k, n)
        selected_children2 = methods[replacement_b](children, k, n)
        return selected_children1[:math.ceil(n*B)] + selected_children2[:math.floor(n*B)]
    elif k == n:
        return children
    selected_old1 = methods[replacement_a](children, k, n)
    selected_old2 = methods[replacement_b](children, k, n)
    return children + selected_old1[:math.ceil((n-k)*B)] + selected_old2[:math.floor((n-k)*B)]

    
