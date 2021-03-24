# crear un personaje --> conseguir el array de items que le tiene que pasar --> abre los tsv y elige uno de cada PONELE QUE DE FORMA RANDOM
# el mejor personaje --> genes: h, equipent
# poblacion: n personajes --> QUIERO EL FITNESS --> elegir algun alg genetico y aplicar mutacion o cruce 


# GEN1: Height 
# GEN2: Equipment 

#--------
# GEN1: Height 2 --> 10 
# GEN2: Helmet 
# GEN3: Armor 
# GEN4: Boots 
# GEN5: Weapon 
# GEN6: Gloves 

import json, csv
from Characters.warrior import Warrior
from Characters.archer import Archer
from Characters.defender import Defender
from Characters.spy import Spy
from item_handler import ItemHandler
from Items.constants import ItemConstants

file_list = [ (ItemConstants.WEAPON,'allitems/armas.tsv'), (ItemConstants.BOOTS,'allitems/botas.tsv'), (ItemConstants.HELMET,'allitems/cascos.tsv'), (ItemConstants.GLOVES,'allitems/guantes.tsv'), (ItemConstants.ARMOR,'allitems/pecheras.tsv')]
item_handler = ItemHandler(file_list) 

equipment = item_handler.getEquipment()
warrior = Warrior(1.5, equipment)

print(equipment)
print(warrior)



    
    