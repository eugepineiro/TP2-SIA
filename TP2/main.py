# crear un personaje --> conseguir el array de items que le tiene que pasar --> abre los tsv y elige uno de cada PONELE QUE DE FORMA RANDOM
# el mejor personaje --> genes: h, equipent
# poblacion: n personajes --> QUIERO EL FITNESS --> elegir algun alg genetico y aplicar mutacion o cruce 

import json
from Characters.warrior import Warrior
from Characters.archer import Archer
from Characters.defender import Defender
from Characters.spy import Spy
from Items.armor import Armor
from Items.boots import Boots
from Items.gloves import Gloves
from Items.helmet import Helmet
from Items.weapon import Weapon

equipment = [Weapon(0,0,0,0,0,0), Boots(0,0,0,0,0,0), Helmet(0,0,0,0,0,0), Gloves(0,0,0,0,0,0), Armor(0,0,0,0,0,0)]
warrior = Warrior(1.5, equipment)

print(warrior)