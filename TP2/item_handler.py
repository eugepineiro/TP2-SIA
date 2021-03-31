import pandas as pd
import random
from Items.boots import Boots
from constants import *

class ItemHandler: 
    
    def __init__(self, file_list): # file_list: lista de tuplas=(item_constant, 'path_tsv')
        self.file_map = {}
        for file_tuple in file_list:
            try:
                df = pd.read_csv(file_tuple[0],delimiter = "\t",skiprows = 1, names=["id","Fu","Ag","Ex","Re","Vi"], index_col="id")
                # aux = file_tuple[1](0,0,0,0,0,0)
                self.file_map[file_tuple[1].__str__(None)] = (df, file_tuple[1])
            except:
                print("cannot open %s" % file_tuple[0])
                continue

    
    def getEquipment(self):
        equipment = {}

        for class_name, tup in self.file_map.items():
            df, item_class = tup

            random_int = self.getRandomNumber(len(df.index))
            row = df.loc[random_int]
            
            force = row.Fu
            agility = row.Ag
            expertise = row.Ex
            resistance = row.Re
            life = row.Vi

            item = item_class(random_int, force, agility, expertise, resistance, life)
            equipment[class_name] = item

        return equipment

    def getRandomNumber(self,max_id):
        return random.randint(0,max_id)

    def getRandomItem(self, class_name):
        df, item_class = self.file_map[class_name]

        random_int = self.getRandomNumber(len(df.index)-1)
        row = df.loc[random_int]

        return item_class(random_int, row.Fu, row.Ag, row.Ex, row.Re, row.Vi)

    
    def getRandomBoots(self):
        return self.getRandomItem(BOOTS_CLASS)

    def getRandomWeapon(self):
        return self.getRandomItem(WEAPON_CLASS)
    
    def getRandomArmor(self):
        return self.getRandomItem(ARMOR_CLASS)

    def getRandomGloves(self):
        return self.getRandomItem(GLOVES_CLASS)
    
    def getRandomHelmet(self):
        return self.getRandomItem(HELMET_CLASS)