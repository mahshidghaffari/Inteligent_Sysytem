from random import random
from random import choice


def pop_generator(size):
    pop = []
    for i in range(size):
        genes = [0, 1]
        individual = []
        for j in range(len(items)):
            individual.append(choice(genes))
            pop.append(individual)
            print("population is generated with random size :", size)

    return pop


def fit_calculator(individual):
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


def indv_selector(pop):
    fitness_values = []
    for ind in pop:
        fitness_values.append(fit_calculator(ind))

    # normalize the fittness value
    fitness_values = [float(i) / sum(fitness_values) for i in fitness_values]

    parent1 = choice(pop, weights=fitness_values, k=1)[0]
    parent2 = choice(pop, weights=fitness_values, k=1)[0]

    print("Selected two individusl for crossover")
    return parent1, parent2


def crossover(parent_1, parent_2):
    cross_point = random.randint(0, len(items) - 1)
    child_1 = parent_1[0:cross_point] + parent_2[cross_point:]
    child_2 = parent_2[0:cross_point] + parent_1[cross_point:]

    print("Performed crossover")
    return child_1, child_2


# function to perform mutation on a chromosome
def mutate(individual):
    mutation_point = random.randint(0, len(items) - 1)
    if individual[mutation_point] == 0:
        individual[mutation_point] = 1
    else:
        individual[mutation_point] = 0
    print("Performed mutation on a individual")
    return individual


def get_best(pop):
    fitness_values = []
    for ind in pop:
        fitness_values.append(fit_calculator(ind))
    max_index = fitness_values.index(max(fitness_values))
    print("get best individual")
    return pop[max_index]


if __name__ == "__main__":
    items = [[4, 7], [8, 6], [8, 5], [2, 9], [6, 8], [0, 5]]
    # print available items
    print("Available items:\n", items)

    max_weight = 10
    population_size = 10
    mutation_probability = 0.2
    generations = 10
    print("\nGenetic algorithm parameters:")
    print("Max weight:", max_weight)
    print("Population:", population_size)
    print("Mutation probability:", mutation_probability)
    print("Generations:", generations, "\n")
    print("Performing genetic evolution:")
    # generate a random population
    population = pop_generator(population_size)

    # evolve the population for specified number of generations
    for i in range(generations):
        # select two chromosomes for crossover
        parent1, parent2 = indv_selector(population)

        # perform crossover to generate two new chromosomes
        child1, child2 = crossover(parent1, parent2)

        # perform mutation on the two new chromosomes
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

