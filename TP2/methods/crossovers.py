import random, math
from Characters.character import Character

# genes_selector(genes1, genes2, genes_cant) => return desc_genes1, desc_genes2

def internal_crossover(parents1, parents2, char_class, genes_selector):
    i = 0
    genes_cant = len(parents1[0].getEquipment()) + 1
    children = []
     
    
    if(len(parents1)%2 == 1):  
        parents2.append(parents2[0])
    elif(len(parents2)%2 == 1):
        parents1.append(parents1[0])
    
    for p1, p2 in zip(parents1, parents2):
        genes1 = [p1.height]+p1.getEquipment()
        genes2 = [p2.height]+p2.getEquipment()

        desc_genes1, desc_genes2 = genes_selector(genes1, genes2, genes_cant)

        equip1_list = desc_genes1[1:]
        equip1 = {e.__str__(): e for e in equip1_list}

        equip2_list = desc_genes2[1:]
        equip2 = {e.__str__(): e for e in equip2_list}
        
        child1 = Character(i, desc_genes1[0], equip1, char_class)
        child2 = Character(i+1, desc_genes2[0], equip2, char_class)
        i += 2
        children += [child1, child2]
    return children

def onePointCross(parents1, parents2, char_class):
    
    def internal_one_point(genes1, genes2, genes_cant):
        locus = random.randint(0, genes_cant)
        desc_genes1 = genes1[:locus] + genes2[locus:]
        desc_genes2 = genes2[:locus] + genes1[locus:]
        return desc_genes1, desc_genes2

    return internal_crossover(parents1, parents2, char_class, internal_one_point)


def twoPointsCross(parents1, parents2, char_class):
    
    def internal_two_points(genes1, genes2, genes_cant):
        l1 = random.randint(0, genes_cant)
        l2 = random.randint(l1, genes_cant)
        desc_genes1 = genes1[:l1] + genes2[l1:l2] + genes1[l2:]
        desc_genes2 = genes2[:l1] + genes1[l1:l2] + genes2[l2:]
        return desc_genes1, desc_genes2

    return internal_crossover(parents1, parents2, char_class, internal_two_points)

def annularCross(parents1, parents2, char_class):

    def internal_annular(genes1, genes2, genes_cant):
        locus = random.randint(0, genes_cant)
        length = random.randint(0, math.ceil(genes_cant/2))

        desc_genes1 = genes1.copy()
        desc_genes2 = genes2.copy()

        idx = locus
        k = 0
        while k < length:
            desc_genes1[idx % genes_cant] = genes2[idx % genes_cant]
            desc_genes2[idx % genes_cant] = genes1[idx % genes_cant]
            idx += 1
            k += 1

        return desc_genes1, desc_genes2

    return internal_crossover(parents1, parents2, char_class, internal_annular)

def uniformCross(parents1, parents2, char_class):

    def internal_uniform(genes1, genes2, genes_cant):
        desc_genes1 = [None] * genes_cant # lista vacía de tamaño genes_cant
        desc_genes2 = [None] * genes_cant

        idx = 0
        while idx < genes_cant:
            p = random.uniform(0,1)

            if p >= 0.5:
                desc_genes1[idx] = genes1[idx]
                desc_genes2[idx] = genes2[idx]
            else:
                desc_genes1[idx] = genes2[idx]
                desc_genes2[idx] = genes1[idx]

            idx += 1

        return desc_genes1, desc_genes2

    return internal_crossover(parents1, parents2, char_class, internal_uniform)
