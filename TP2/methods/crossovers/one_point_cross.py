import random
from Characters.character import Character

def onePointCross(parents1, parents2, char_class):
    i = 0
    genes_cant = len(parents1[0].equipment) + 1
    children = []
    for p1, p2 in zip(parents1, parents2):
        genes1 = [p1.height]+p1.equipment
        genes2 = [p2.height]+p2.equipment
        lotus = random.randint(1, genes_cant)
        desc_genes1 = genes1[:lotus] + genes2[lotus:]
        desc_genes2 = genes2[:lotus] + genes1[lotus:]
        
        child1 = Character(i, desc_genes1[0], desc_genes1[1:], char_class)
        child2 = Character(i+1, desc_genes2[0], desc_genes2[1:], char_class)
        i += 2
        children += [child1, child2]
    return children
