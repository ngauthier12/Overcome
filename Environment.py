import copy

from IGeneticData import *
from IFitnessEvaluator import *


class Environment:

    def __init__(self, genetic_data, fitness_evaluator):
        assert genetic_data is not None, "Expecting not None genetic_data"
        assert isinstance(genetic_data, IGeneticData), "Expecting genetic_data to be an IGeneticData"

        assert fitness_evaluator is not None, "Expecting not None fitness_evaluator"
        assert isinstance(fitness_evaluator, IFitnessEvaluator), "Expecting fitness_evaluator to be an IFitnessEvaluator"

        self.genetic_data = genetic_data
        self.fitness_evaluator = fitness_evaluator

    def simulate(self, individual_count, generation_count):
        # Create population
        population = []
        for i in range(individual_count):
            population.append(copy.deepcopy(self.genetic_data))
