import copy
import random

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

    def simulate(self, individual_count, generation_count, elimination_ratio, mutation_rate):
        assert isinstance(individual_count, int), "Expecting individual_count to be an int"
        assert individual_count > 1, "Expecting individual_count > 1"

        assert isinstance(generation_count, int), "Expecting generation_count to be an int"
        assert generation_count > 1, "Expecting generation_count > 1"

        assert isinstance(elimination_ratio, float), "Expecting elimination_ratio to be a float"
        assert 0 <= elimination_ratio < 1, "Expecting elimination_ratio to be within [0, 1["

        assert isinstance(mutation_rate, float), "Expecting mutation_rate to be a float"
        assert mutation_rate >= 0, "Expecting mutation_rate to be >= 0"

        # Create population
        population = []
        for individual_index in range(individual_count):
            population.append(copy.deepcopy(self.genetic_data))

        # Iterate
        for generation_index in range(generation_count):
            # Evaluate score
            for individual in population:
                individual.score = self.fitness_evaluator.evaluate(individual, population)

            # Sort by highest score
            population.sort(key= lambda x : x.score, reverse=True)

            # Replace losers by combination of winners
            number_losers = int(round(individual_count * elimination_ratio))
            number_winners = individual_count - number_losers

            winners = population[:number_winners]
            losers = population[-number_losers:]

            for loser in losers:
                # Regen each loser from 2 random parents
                random_winner1 = random.choice(winners)
                random_winner2 = random.choice(winners)
                loser.regen_from_parents(random_winner1, random_winner2)

                # Apply mutation
                mutation_counter = mutation_rate
                while mutation_counter >= 1:
                    loser.mutate_once()
                    mutation_counter -= 1

                if random.uniform(0, 1) < mutation_counter:
                    loser.mutate_once()

        return population
