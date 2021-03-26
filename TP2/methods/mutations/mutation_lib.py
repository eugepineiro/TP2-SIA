# Tengo que definir una probabilidad de mutación Pm --> debería depende de alguna forma de la cantidad de generaciones que tengo me parece porque la idea es explorar mucho al principio y a medida que van pasando las generaciones o el tiempo disminuir la exploracion y aumentar la explotacion
import random
from Characters.character import Character
from constants import *


class MutationLib:

    def getMutationProbability():
        return random.uniform(0, 1)

    def getNewGen(gen_class, item_handler):

        print(gen_class)
        if gen_class == HEIGHT_CLASS:
            new_gen = random.uniform(MIN_HEIGHT, MAX_HEIGHT)
        else:
            new_gen = item_handler.getRandomItem(gen_class)

        return new_gen
