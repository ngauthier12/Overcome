from Environment import *
from SimpleGeneticData import *
from IndependentFitnessEvaluator import *


def create_genetic_data():
    genetic_data = SimpleGeneticData()
    genetic_data["a"] = 0.0
    genetic_data["b"] = 1.0
    genetic_data["c"] = 2.0
    return genetic_data


def evaluate_fitness(individual, population):
    a = individual["a"]
    b = individual["b"]
    c = individual["b"]
    return a + b - c


if __name__ == "__main__":
    initial_data = create_genetic_data()

    fitness_evaluator = IndependentFitnessEvaluator(
        evaluation_function=evaluate_fitness)

    environment = Environment(
        genetic_data=initial_data,
        fitness_evaluator=fitness_evaluator)

    population = environment.simulate(
        individual_count=1000,
        generation_count=1000,
        elimination_ratio=0.2,
        mutation_rate=0.01)

    print("best individual = " + str(population[0]))
