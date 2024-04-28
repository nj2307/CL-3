import random
from deap import base, creator, tools, algorithms

# Define the evaluation function
def evaluate(individual):
    # Evaluation function calculates the fitness of an individual
    # In this case, it returns the sum of binary values in the individual
    return sum(individual),

# Create the types for individuals and fitness
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Initialize the DEAP toolbox
toolbox = base.Toolbox()

# Register the functions to create attributes, individuals, and populations
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register the genetic operators
toolbox.register("mate", tools.cxTwoPoint)  # Crossover operator
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)  # Mutation operator
toolbox.register("select", tools.selTournament, tournsize=3)  # Selection operator
toolbox.register("evaluate", evaluate)  # Fitness evaluation function

# Define parameters
population_size = 100
num_generations = 50

# Create initial population
population = toolbox.population(n=population_size)

# Evaluate the entire population
fitnesses = list(map(toolbox.evaluate, population))
for ind, fit in zip(population, fitnesses):
    ind.fitness.values = fit

# Evolutionary loop
for generation in range(num_generations):
    # Select the next generation individuals
    offspring = toolbox.select(population, len(population))

    # Clone the selected individuals
    offspring = list(map(toolbox.clone, offspring))

    # Apply crossover and mutation on the offspring
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < 0.5:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < 0.2:
            toolbox.mutate(mutant)
            del mutant.fitness.values

# Evaluate individuals with invalid fitness
invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
fitnesses = map(toolbox.evaluate, invalid_ind)
for ind, fit in zip(invalid_ind, fitnesses):
    ind.fitness.values = fit

# Replace the current population with the offspring
population[:] = offspring

# Print the best individual found
best_individual = tools.selBest(population, 1)[0]
print("Best individual:", best_individual)
print("Fitness:", best_individual.fitness.values[0])
