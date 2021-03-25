import pandas as pd
from Items.constants import ItemConstants
import random
from Items.armor import Armor
from Items.boots import Boots
from Items.gloves import Gloves
from Items.helmet import Helmet
from Items.weapon import Weapon

class ItemHandler: 
    
    def __init__(self, file_list): # file_list: lista de tuplas=(item_constant, 'path_tsv')
        self.file_map = {}
        for file_tuple in file_list:
            try:
                df = pd.read_csv(file_tuple[1],delimiter = "\t",skiprows = 1, names=["id","Fu","Ag","Ex","Re","Vi"], index_col="id")
                self.file_map[file_tuple[0]] = df
            except:
                print("cannot open %s" % file_tuple[1])
                continue

        # self.rd = self.open(filename)
        # df = pd.read_csv("./allitems/"+filename+".tsv",delimiter = "\t",skiprows = 1, names=["id","Fu","Ag","Ex","Re","Vi"], index_col="id")
        # self.row = df.loc[4]
    
    def getEquipment(self):
        equipment = []

        for item_constant, df in self.file_map.items():
            
            random_int = self.getRandomNumber(10) # df.axes[0]
            row = df.loc[random_int]
            
            force = row.Fu
            agility = row.Ag
            expertise = row.Ex
            resistence = row.Re
            life = row.Vi

            if item_constant == ItemConstants.BOOTS:
                equipment.append(Boots(random_int, force, agility, expertise, resistence, life))
            elif item_constant == ItemConstants.ARMOR:
                equipment.append(Armor(random_int, force, agility, expertise, resistence, life))
            elif item_constant == ItemConstants.HELMET:
                equipment.append(Helmet(random_int, force, agility, expertise, resistence, life))
            elif item_constant == ItemConstants.WEAPON:
                equipment.append(Weapon(random_int, force, agility, expertise, resistence, life))
            elif item_constant == ItemConstants.GLOVES:
                equipment.append(Gloves(random_int, force, agility, expertise, resistence, life))
            else:
                print("item not recognized")
                continue

        return equipment

    def getRandomNumber(self,max_id):
        return random.randint(0,max_id)