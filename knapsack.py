import random


# generate a random population
def generate_population(size):
    pop = []
    for _ in range(size):
        genes = [0, 1]
        individual = []
        for _ in range(len(items)):
            individual.append(random.choice(genes))
        pop.append(individual)
    print("A random population with size ", size, " is generated")
    return pop


def calculate_fitness(individual):
    total_weight = 0
    total_value = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            total_weight += items[i][0]
            total_value += items[i][1]
    if total_weight > max_weight:
        return 0
    else:
        return total_value


# function to select two individuals for crossover
def select_individuals(pop):
    fitness_values = []
    for individual in pop:
        fitness_values.append(calculate_fitness(individual))

    fitness_values = [float(i) / sum(fitness_values) for i in fitness_values]

    parent1 = random.choices(pop, weights=fitness_values, k=1)[0]
    parent2 = random.choices(pop, weights=fitness_values, k=1)[0]

    return parent1, parent2


# function to perform crossover between two individuals
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(items) - 1)
    child1 = parent1[0:crossover_point] + parent2[crossover_point:]
    child2 = parent2[0:crossover_point] + parent1[crossover_point:]

    print("Performed crossover between two individuals")
    return child1, child2


# function to perform mutation on a individual
def mutate(individual):
    mutation_point = random.randint(0, len(items) - 1)
    if individual[mutation_point] == 0:
        individual[mutation_point] = 1
    else:
        individual[mutation_point] = 0
    print("Performed mutation on a individual")
    return individual


# function to get the best individual from the population
def get_best(population):
    fitness_values = []
    for individual in population:
        fitness_values.append(calculate_fitness(individual))

    max_value = max(fitness_values)
    max_index = fitness_values.index(max_value)
    return population[max_index]


# items that can be put in the knapsack
items = [
    [5, 2],
    [2, 5],
    [3, 3],
    [8, 5],
    [8, 5],
    [5, 7],
    [9, 2]
]

# print available items
print("Available items:\n", items)

# parameters for genetic algorithm
max_weight = 10
population_size = 20
mutation_probability = 0.4
generations = 100

print("\nGenetic algorithm parameters:")
print("Max weight:", max_weight)
print("Population:", population_size)
print("Mutation probability:", mutation_probability)
print("Generations:", generations, "\n")
print("Performing genetic evolution:")

# generate a random population
population = generate_population(population_size)

# evolve the population for specified number of generations
for _ in range(generations):
    # select two individuals for crossover
    parent1, parent2 = select_individuals(population)

    # perform crossover to generate two new individuals
    child1, child2 = crossover(parent1, parent2)

    # perform mutation on the two new individuals
    if random.uniform(0, 1) < mutation_probability:
        child1 = mutate(child1)
    if random.uniform(0, 1) < mutation_probability:
        child2 = mutate(child2)

    # replace the old population with the new population
    population = [child1, child2] + population[2:]

# get the best individual from the population
best = get_best(population)

# get the weight and value of the best solution
total_weight = 0
total_value = 0
for i in range(len(best)):
    if best[i] == 1:
        total_weight += items[i][0]
        total_value += items[i][1]

# print the best solution
print("\nThe best solution:")
print("Weight:", total_weight)
print("Value:", total_value)