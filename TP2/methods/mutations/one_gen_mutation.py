# genes[h, weapon, boots, armor, gloves, helmet]
# Qué es mutar un gen? --> Elijo un gen y lo intercambio por otro del tsv (en caso de ser item), si es height getUniform(1.3 ; 2)
#                      --> o aplico un delta
# Tengo que definir una probabilidad de mutación Pm --> si se cumple esa Pm para mi individuo --> agarro un gen al azar y lo muto, sino no (puede pasar que no mute ningun individuo, no pasa nada)
import random

def oneGenMutation(genes):
    
    gen_to_mutate = random.choice(genes) 
    print(gen_to_mutate.__class__.__name__)
    
    
    #Deberia tener guardados en el item_handler.py todas las botas, todos los helmets y asi para ahora agarrar uno random dependiendo de lo que sea el gen_to_mutate
    
    return individual