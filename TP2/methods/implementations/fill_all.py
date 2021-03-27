from methods.selections import elite

def fill_all(old_generation,children,k,n):
    join = old_generation + children
    return elite(join, k, n)


    