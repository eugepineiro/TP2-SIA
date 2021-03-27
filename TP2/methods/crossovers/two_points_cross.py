import random
from Characters.character import Character

def twoPointsCross(parents1, parents2, char_class):
    i = 0
    genes_cant = len(parents1[0].getEquipment()) + 1
    children = []

    for p1, p2 in zip(parents1, parents2):
        genes1 = [p1.height]+p1.getEquipment()
        genes2 = [p2.height]+p2.getEquipment()
        l1 = random.randint(0, genes_cant)
        l2 = random.randint(l1, genes_cant)
        desc_genes1 = genes1[:l1] + genes2[l1:l2] + genes1[l2:]
        desc_genes2 = genes2[:l1] + genes1[l1:l2] + genes2[l2:]

        equip1_list = desc_genes1[1:]
        equip1 = {e.__str__(): e for e in equip1_list}

        equip2_list = desc_genes2[1:]
        equip2 = {e.__str__(): e for e in equip2_list}

        child1 = Character(i, desc_genes1[0], equip1, char_class)
        child2 = Character(i+1, desc_genes2[0], equip2, char_class)
        i += 2
        children += [child1, child2]
        
    return children