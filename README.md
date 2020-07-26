# Overcome
`Overcome` is a minimalist evolutive algorithm (EA) framework. It's designed to have an API as simple as possible, yet allow beginners to try their hand at solving problems with EA.

# Sample
```
from Environment import *
from SimpleGeneticData import *
from IndependentFitnessEvaluator import *


def create_genetic_data():
    genetic_data = SimpleGeneticData()
    genetic_data["x"] = 10.
    genetic_data["y"] = -10.
    return genetic_data


def evaluate_fitness(individual, population):
    x = individual["x"]
    y = individual["y"]
    return -(x * x) - (y * y)


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
```
