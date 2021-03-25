# crear un personaje --> conseguir el array de items que le tiene que pasar --> abre los tsv y elige uno de cada PONELE QUE DE FORMA RANDOM
# el mejor personaje --> genes: h, equipent
# poblacion: n personajes --> QUIERO EL FITNESS --> elegir algun alg genetico y aplicar crossover y mutation 
#--------
# GEN1: Height  
# GEN2: Helmet 
# GEN3: Armor 
# GEN4: Boots 
# GEN5: Weapon 
# GEN6: Gloves 

# 1. SELECCION DE PADRES 
# 2. SE APAREAN LOS PADRES 
# 3. SE HACE CROSSOVER 
# 4. SE HACE MUTACION DE ALGUNOS HIJOS DE LA NUEVA GENERACION 
# 5. CONDICION DE CORTE

import json, csv, random
from Characters.warrior import Warrior
from Characters.archer import Archer
from Characters.defender import Defender
from Characters.spy import Spy
from item_handler import ItemHandler

from Items.armor import Armor
from Items.boots import Boots
from Items.gloves import Gloves
from Items.helmet import Helmet
from Items.weapon import Weapon

from methods.selections.elite import elite

file_list = [('TP2/allitems/armas.tsv', Weapon), ('TP2/allitems/botas.tsv', Boots), ('TP2/allitems/cascos.tsv', Helmet), ('TP2/allitems/guantes.tsv', Gloves), ('TP2/allitems/pecheras.tsv', Armor)]
item_handler = ItemHandler(file_list) 
data = None

with open('TP2/config.json','r') as json_file:
    data = json.load(json_file)

    character_class = data['class']
    population_amount = data['population_amount']
    individuals_amount = data['individuals_amount']
    selection_method = data["selection_method"]

   
    characters = []

    for i in range(population_amount):
        equipment = item_handler.getEquipment()
        char = None
        height = random.uniform(1.3, 2)
        if character_class == 'warrior':
            char = Warrior(i,height, equipment)

        characters.append(char)

    
    parents = elite(characters, individuals_amount, population_amount)

print(parents) 



    
    