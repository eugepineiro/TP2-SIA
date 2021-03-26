def roulette(characters, individuals_amount): 

    fitness_dict = {}

    acum_fitness = 0
    for character in characters: 
        acum_fitness = acum_fitness + character.fitness
        fitness_dict[acum_fitness, character]

    
