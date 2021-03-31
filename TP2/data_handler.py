from constants import *
from methods.mutations import oneGenMutation, completeMutation, limitedMultigenMutation, uniformMultigenMutation
from methods.selections import elite, roulette, universal, ranking, boltzmann, d_tournaments, p_tournaments
from methods.crossovers import onePointCross, twoPointsCross, annularCross, uniformCross
from Characters.character_class import CharacterClass

class DataHandler:

    def __init__(self, data):
        self.population_amount = data['population_amount']
        self.character_class = CharacterClass[data['class'].upper()]
        self.individuals_amount = data['individuals_amount']
        self.individual_mutation_probability = data['individual_mutation_probability']
        self.selection_method_a = data["methods"]["selection_a"]
        self.selection_method_b = data["methods"]["selection_b"]
        self.mutation_method = data["methods"]["mutation"]
        self.replacement_a = data["methods"]["replacement_a"]
        self.replacement_b = data["methods"]["replacement_b"]
        self.selection_prob = data["methods"]["selection_prob"]
        self.replacement_prob = data["methods"]["replacement_prob"]
        self.implementation = data["implementation"]
        self.crossover_func = data["methods"]["crossover"] 
        self.threshold = data["methods"]["selection_params"]["p_tournaments_threshold"] 
        self.cutting_method = data["cutting_condition"]["method"]
        self.cutting_param = data["cutting_condition"]["parameter"]

    def selection(self, method, characters, ind_amount, pop_amount, generation):

        if method == ELITE_S :
            return elite(characters, ind_amount, pop_amount)
        elif method == ROULETTE_S:
            return roulette(characters, ind_amount)
        elif method == UNIVERSAL_S: 
            return universal(characters, ind_amount)
        elif method == RANKING_S: 
            return ranking(characters,ind_amount,pop_amount)
        elif method == BOLTZMANN: 
            return boltzmann(characters, ind_amount, pop_amount, generation)
        elif method == D_TOURNAMENTS_S:
            #TODO: CHANGE 
            m_value = 10 
            return d_tournaments(characters, ind_amount, pop_amount, m_value)
        elif method == P_TOURNAMENTS_S: 
            return p_tournaments(characters,ind_amount, pop_amount, self.threshold)
        


    def mutation(self, individual, item_handler):

        if self.mutation_method == ONE_GEN_M:
            return oneGenMutation(individual, item_handler)
        elif self.mutation_method == COMPLETE_M: 
            return completeMutation(individual, item_handler)
        elif self.mutation_method == LIMITED_MULTIGEN_M:
            return limitedMultigenMutation(individual, item_handler)
        elif self.mutation_method == UNIFORM_MULTIGEN_M: 
            return uniformMultigenMutation(individual, item_handler, self.individual_mutation_probability)

    def crossover(self, parents1, parents2):
        if self.crossover_func == ONE_POINT_C:
            return onePointCross(parents1, parents2, self.character_class)
        elif self.crossover_func == TWO_POINTS_C:
            return twoPointsCross(parents1, parents2, self.character_class)
        elif self.crossover_func == ANNULAR_C:
            return annularCross(parents1, parents2, self.character_class)
        elif self.crossover_func == UNIFORM_C:
            return uniformCross(parents1, parents2, self.character_class)
