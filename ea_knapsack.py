import numpy as np
import random
import matplotlib.pyplot as plt
import math
from dataclasses import dataclass, field

GENERATION = 500
POPULATION = 40
NUM_OF_ITEM = 50
MAX_WEIGHT = int(np.round(math.fsum(range(1, NUM_OF_ITEM + 1)) * 0.75))
# the fitness individual gets mutation every 25 years of their life
MUTATION_AGE = int(np.round(GENERATION * 0.05))


@dataclass
class Individual:
    value: np.ndarray = field(init=False,
                              default_factory=lambda: np.array([],
                                                               dtype=int))
    weight: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=int))
    present: np.ndarray = field(init=False,
                                default_factory=lambda: np.array([],
                                                                 dtype=int))
    score_v: int = field(init=False, default=0)
    score_w: int = field(init=False, default=0)
    age: int = field(init=True, default=0)

    def aging(self):
        self.age += 1

    ##Get relative fitness per individual
    def fitness(self):
        self.score_v = 0
        self.score_w = 0
        for i in range(0, NUM_OF_ITEM):
            if self.present[i] == 1:
                self.score_v = self.score_v + self.value[i]
                self.score_w = self.score_w + self.weight[i]


def main():
    ##Initialization
    gen = 0
    value = np.array([])
    weight = np.array([])
    best_array = np.array([])
    gen_array = np.array([])
    mean_array = np.array([])
    std_array = np.array([])
    trail_array = np.array([])
    for i in range(0, NUM_OF_ITEM):
        value = np.append(value, np.random.randint(1, 10))
        weight = np.append(weight, i + 1)
    dyn = dynamic(value)

    for work in range(0, 1000):
        print(work)
        population = new_individuals(value, weight, POPULATION)
        start = population[fittest(population)].score_v
        ##Actual EA
        while gen < GENERATION:
            population = recombination(population)
            population = mutation(population)
            population = selection(population)
            population = aged(population)
            gen = gen + 1

            best = population[fittest(population)]
            best_array = np.append(best_array, best.score_v)
            gen_array = np.append(gen_array, gen)
            mean, std = get_stat(population)
            mean_array = np.append(mean_array, mean)
            std_array = np.append(std_array, std)
        trail_array = np.append(trail_array, dyn - best.score_v)
        del population

    print(dyn)
    print(start)
    print(best.score_v)
    print(best.age)
    print(mean)
    print(std)
    plot(gen_array, best_array, 'Highest Value Over Time',
         'graph1-2.png', 'Generation', 'Value of sack', 'red', 'value')
    plot(gen_array, mean_array, 'Average Value Over Time',
         'graph2-2.png', 'Generation', 'Value of sack', 'blue', 'value')
    plot(gen_array, std_array, 'std Value Over Time',
         'graph3-2.png', 'Generation', 'Value of sack', 'green', 'value')
    plot(range(0, 1000), trail_array, 'Differnce between dynamic and EA',
         'graph4-2.png', 'Trails', 'Value of sack', 'black', 'value')


def plot(xarray, yarray, title, file, xlabel, ylabel, color, label):
    plt.plot(xarray, yarray, color=color, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.savefig(file)
    plt.clf()


##Get the mean and standard deviation of the fitness of population
def get_stat(population):
    mean = std = 0
    for i in range(0, len(population)):
        population[i].fitness()
        mean += population[i].score_v
    mean = mean / len(population)
    for i in range(0, len(population)):
        tmp = population[i].score_v - mean
        tmp = math.pow(tmp, 2)
        std += tmp
    std = std / len(population)
    std = math.sqrt(std)
    return  mean, std


##Find the fittest individual in the population
def fittest(population):
    population[0].fitness()
    n = 0
    best = population[0]
    for i in range(1, len(population)):
        population[i].fitness()
        if population[i].score_v > best.score_v:
            best = population[i]
            n = i
    return n


##Update everyone's age in the population
def aged(population):
    for i in range(0, len(population)):
        population[i].aging()
    return population


##Either add new individuals to the population, or initialize it
def new_individuals(value, weight, size):
    population = np.array([])
    for i in range(0, size):
        individual = Individual()
        individual.value = np.append(individual.value, value)
        individual.weight = np.append(individual.weight, weight)
        binary = np.random.randint(0, 2, NUM_OF_ITEM)
        individual.present = np.append(individual.present, binary)
        individual.fitness()
        while individual.score_w > MAX_WEIGHT:
            binary = np.random.randint(0, 2, NUM_OF_ITEM)
            spot = range(0, NUM_OF_ITEM)
            np.put(individual.present, [spot], binary)
            individual.fitness()
        population = np.append(population, individual)
    return population


def mutation(population):
    index = np.array([], int)
    mean, std = get_stat(population)
    cut_off = mean - std
    spot = range(0, NUM_OF_ITEM)
    binary = np.random.randint(0, 1, NUM_OF_ITEM)

    for i in range(0, len(population)):
        time = population[i].age % MUTATION_AGE
        if population[i].score_v < cut_off or time == 0:
            index = np.append(index, i)

    for j in index:
        point = np.random.randint(0, NUM_OF_ITEM)
        if population[j].present[point] == 0:
            population[j].present[point] = 1
        else:
            population[j].present[point] = 0
    ##Remove individuals who break the weight limit
    size = len(population)
    k = 0
    while k < size:
        population[k].fitness()
        if population[k].score_w > MAX_WEIGHT:
            size = size - 1
            population = np.delete(population, k)
        else:
            k = k + 1
    return population


def recombination(population):
    new = 0
    best = fittest(population)
    new_population = np.array([population[best]])
    old_gen = len(population)

    while new < POPULATION:
        mom = dad = -1
        while mom == dad:
            mom = np.random.randint(0, old_gen)
            dad = np.random.randint(0 , old_gen)
        new_individual = Individual()
        new_individual.value = np.append(new_individual.value,
                                         population[0].value)
        new_individual.weight = np.append(new_individual.weight,
                                          population[0].weight)
        crossover_point = random.randint(1, NUM_OF_ITEM - 1)

        mom_genes = population[mom].present[0:crossover_point]
        new_individual.present = np.append(new_individual.present,
                                           mom_genes)

        dad_genes = population[dad].present[crossover_point:NUM_OF_ITEM]
        new_individual.present = np.append(new_individual.present,
                                           dad_genes)
        new_individual.fitness()
        if new_individual.score_w > MAX_WEIGHT:
            del new_individual
        else:
            new_population = np.append(new_population, new_individual)
            new += 1
    return new_population


def selection(population):
    total_fitness_v = 0
    new_population = np.array([])
    roulette = np.array([])
    mean, std = get_stat(population)
    cut_off = mean + std

    for i in range(0, len(population)):
        if population[i].score_v >= cut_off:
            new_population = np.append(new_population, population[i])
        else:
            total_fitness_v += population[i].score_v
            roulette = np.append(roulette, population[i])
    ##Roulette selection, from Individuals who fall under the cut off
    stop = int(np.round(len(roulette) / 10))
    for j in range(0, stop):
        sum_v = 0
        prob = random.random()
        n = 0
        sum_v = (roulette[n].score_v / total_fitness_v)
        while sum_v < prob:
            n += 1
            sum_v += roulette[n].score_v / total_fitness_v
        new_population = np.append(new_population, roulette[n])
    return new_population


##Jason's code he let me use to check the EA
def dynamic(values):
    memo = []
    for item in range(0, len(values)):
        temp = []
        for weight in range(0, MAX_WEIGHT):
            temp.append(0)
        memo.append(temp)
    for item in range(0, len(values)):
        for weight in range(0, MAX_WEIGHT):
            # check if biggest item can fit in sub-problem bag
            if item + 1 <= weight + 1:
                memo[item][weight] = values[item]
            # check if there was a better solution already
            if item > 0 and memo[item - 1][weight] > memo[item][weight]:
                memo[item][weight] = memo[item - 1][weight]
            # check if more items can be added on top of biggest item
            check = values[item] + memo[item - 1][weight - item - 1]
            if weight - item > 0 and \
                    item > 0 and \
                    check > memo[item][weight]:
                memo[item][weight] = values[item] + \
                    memo[item - 1][weight - item - 1]
    return memo.pop().pop()


if __name__ == "__main__":
    main()