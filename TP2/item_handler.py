import pandas as pd
import random

class ItemHandler: 
    
    def __init__(self, file_list): # file_list: lista de tuplas=(item_constant, 'path_tsv')
        self.file_map = {}
        for file_tuple in file_list:
            try:
                df = pd.read_csv(file_tuple[0],delimiter = "\t",skiprows = 1, names=["id","Fu","Ag","Ex","Re","Vi"], index_col="id")
                self.file_map[file_tuple[0]] = (df, file_tuple[1])
            except:
                print("cannot open %s" % file_tuple[0])
                continue

        # self.rd = self.open(filename)
        # df = pd.read_csv("./allitems/"+filename+".tsv",delimiter = "\t",skiprows = 1, names=["id","Fu","Ag","Ex","Re","Vi"], index_col="id")
        # self.row = df.loc[4]
    
    def getEquipment(self):
        equipment = []

        for item_constant, tup in self.file_map.items():
            df = tup[0]
            item_class = tup[1]

            random_int = self.getRandomNumber(len(df.index))
            row = df.loc[random_int]
            
            force = row.Fu
            agility = row.Ag
            expertise = row.Ex
            resistence = row.Re
            life = row.Vi

            item = item_class(random_int, force, agility, expertise, resistence, life)
            equipment.append(item)

        return equipment

    def getRandomNumber(self,max_id):
        return random.randint(0,max_id)