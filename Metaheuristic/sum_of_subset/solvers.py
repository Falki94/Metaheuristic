import itertools
import logging
import math
import random
import time

import numpy as np


def brute_force_solver(entry_set, target):
    '''
    The brute force algorithm checks all possibilities until he finds a solution.
    :param entry_set: Set of numbers to solve the problem
    :param target: Target value of sum of subset to solve the problem
    :return:
    '''
    start_time = time.time()
    attempt = 0
    for i in range(1, len(entry_set) + 1):
        for combination in itertools.combinations(entry_set, i):
            goal = goal_function(combination, target)
            attempt += 1
            logging.debug("Attempt = {}, Goal = {}, Execution time = {}".format(attempt, goal, (time.time() - start_time)))
            if is_optimal_solution(combination, target):
                if is_valid_solution(entry_set, combination):
                    logging.info("SOLUTION(~BruteForce)!!!!!->Size = {}, Attempt = {}, Goal = {}, Execution time = {} ".format(len(entry_set), attempt, goal, (time.time() - start_time)))
                    return list(combination)
    return None


def climbing_solver(entry_set, target, limit):
    '''
    Hill Climbing algorithm to solve Sum of Subset problem:
    General principle of operation: We start from a random point,
    Browse through its neighbours, choose the neighbour with the greatest value
    "we go up", repeat the activities until the local maxium is reached
    :param entry_set: Set of numbers to solve the problem
    :param target: Target value of sum of subset to solve the problem
    :param limit: Limit of iterations can be overridden
    :return:
    '''
    size = len(entry_set) // 2
    random_solution = generate_random_solution(entry_set, size)
    start_time = time.time()
    attempt = 0
    if is_optimal_solution(random_solution, target):
        if is_valid_solution(entry_set, random_solution):
            attempt += 1
            logging.info(
                "SOLUTION(~Climbing)!!!!!->Size = {}, Attempt = {}, Goal = {}, Execution time = {} ".format(len(entry_set), attempt, goal_function(random_solution, target), (
                            time.time() - start_time)))
            return random_solution
    for _ in range(1, limit):
        attempt += 1
        close_neighbour = find_close_neighbour(entry_set, random_solution)
        goal = goal_function(close_neighbour, target)
        logging.debug("Attempt = {}, Goal = {}, Execution time = {}".format(attempt, goal, (time.time() - start_time)))
        if is_optimal_solution(close_neighbour, target):
            if is_valid_solution(entry_set, close_neighbour):
                logging.info(
                    "SOLUTION(~Climbing)!!!!!->Size = {}, Attempt = {}, Goal = {}, Execution time = {} ".format(len(entry_set), attempt, goal,
                                                                                                         (
                                                                                                                 time.time() - start_time)))
                return close_neighbour
        if close_neighbour > random_solution:
            random_solution = close_neighbour

    logging.warning("Limit exceeded not found solution")
    return None


def simulated_annealing_solver(entry_set, target, limit):
    '''
    Simulated annealing algorithm is very similar to Hill climbing algorithm,
    but is extended through the characteristic feature of a control parameter called Temperature,
    which decreses during the execution of the algorithm
    :param entry_set: Set of numbers to solve the problem
    :param target: Target value of sum of subset to solve the problem
    :param limit: Limit of iterations can be overridden
    :return:
    '''
    def temperature(x):
        return 1 / x
    size = len(entry_set) // 2
    start_time = time.time()
    attempt = 0
    random_solution = generate_random_solution(entry_set, size)
    if is_optimal_solution(random_solution, target):
        if is_valid_solution(entry_set, random_solution):
            attempt += 1
            logging.info(
                "SOLUTION(~Simulated_annealing)!!!!!->Size = {}, Attempt = {}, Goal = {}, Execution time = {} ".format(len(entry_set), attempt, goal_function(random_solution, target), (
                            time.time() - start_time)))
            return random_solution
    for i in range(1, limit):
        attempt += 1
        close_neighbour = find_close_neighbour(entry_set, random_solution)
        goal = goal_function(close_neighbour, target)
        logging.debug("Attempt = {}, Goal = {}, Execution time = {}".format(attempt, goal, (time.time() - start_time)))
        if is_optimal_solution(close_neighbour, target):
            if is_valid_solution(entry_set, close_neighbour):
                logging.info(
                    "SOLUTION(~Simulated_annealing)!!!!!->Size = {}, Attempt = {}, Goal = {}, Execution time = {} ".format(len(entry_set), attempt, goal,
                                                                                                       (
                                                                                                               time.time() - start_time)))
                return close_neighbour
        if close_neighbour > random_solution:
            random_solution = close_neighbour
        else:
            random_number = random.random()
            sa_condition = math.exp(
                -(abs(np.sum(close_neighbour) - np.sum(random_solution)) / temperature(i))
            )
            if random_number < sa_condition:
                random_solution = close_neighbour
    return None


def tabu_solver(entry_set, target, limit, tabu_size):
    '''
    Tabu search is a meta-heuristic optimization technique, which owes its name to its memory structures,
    used to store recently evaluated candidate solutions.
    The candidates stored in these structures are not eligible for generation of further candidates
    and are thereby considered “Tabu” by the algorithm.
    :param entry_set: Set of numbers to solve the problem
    :param target: Target value of sum of subset to solve the problem
    :param limit: Limit of iterations can be overridden
    :param tabu_size:
    :return:
    '''
    tabu_count = 100
    size = len(entry_set) // 2
    current_tabu_count = 0
    start_time = time.time()
    attempt = 0
    random_solution = generate_random_solution(entry_set, size)
    tabu_list = []
    if is_optimal_solution(random_solution, target):
        if is_valid_solution(entry_set, random_solution):
            attempt += 1
            logging.info(
                "SOLUTION(~Tabu)!!!!!->Size = {}, Attempt = {}, Goal = {}, Execution time = {} ".format(len(entry_set),
                                                                                                         attempt,
                                                                                                   goal_function(
                                                                                                       random_solution,
                                                                                                       target), (
                                                                                                           time.time() - start_time)))
            return random_solution
    for _ in range(1, limit):
        attempt += 1
        if tabu_list and current_tabu_count == tabu_count:
            tabu_list.pop()
            current_tabu_count = 0
        if len(tabu_list) == tabu_size:
            tabu_list.pop()
        current_tabu_count += 1
        close_neighbour = find_close_neighbour(entry_set, random_solution)
        goal = goal_function(close_neighbour, target)
        logging.debug("Attempt = {}, Goal = {}, Execution time = {}".format(attempt, goal, (time.time() - start_time)))
        if is_optimal_solution(close_neighbour, target):
            if is_valid_solution(entry_set, close_neighbour):
                logging.info(
                    "SOLUTION(~Tabu)!!!!!->Size = {}, Attempt = {}, Goal = {}, Execution time = {} ".format(len(entry_set), attempt, goal,
                                                                                                       (
                                                                                                               time.time() - start_time)))
                return close_neighbour
        if close_neighbour > random_solution and close_neighbour not in tabu_list:
            tabu_list.append(random_solution)
            random_solution = close_neighbour
    return None



def genetic_solver(entry_set, s, s_best, population_size, iterations_number, crossover_rate, mutation_rate,
                   cloning_rate, fitness_target, iteration=1):
    '''
    The genetic algorithm tries to obtain the best solutions by selecting the best features of solutions from a specific pool.
    There are crossover, mutation, and selection operations defined.
    We assume that with each successive generation the solutions present in the population will be better and better.
    :param entry_set: Set of numbers to solve the problem
    :param s: Randomly Initialized set
    :param s_best: The best chromosome
    :param population_size: Size of the population which is actually correlated with entry_set
    :param iterations_number: Value of the iterations (There can be maximum 995 iterations set to avoid stack over flow)
    :param crossover_rate: Value of the crossover rate
    :param mutation_rate: Value of the mutation rate
    :param cloning_rate: Value of the cloning rate
    :param fitness_target: The target value of the sum of the subset to solve the problem
    :return:
    '''
    start_time = time.time()
    # global iteration
    if fitness_function(s_best, entry_set, fitness_target) == 0:
        logging.info("SOLUTION(~Genetic)!!!!!->Size = {}, Attempt = {}, Target = {}, Execution time = {} ".format(
                    len(entry_set), iteration, fitness_target, (time.time() - start_time)))
        return s_best
    if iteration == iterations_number:
        logging.warning("Out of Attempts: {}".format(iteration))

    logging.debug("Attempt = {}, Target = {}, Execution time = {}".format(iteration, fitness_target, (time.time() - start_time)))
    s.sort(key=lambda k: fitness_function(k, entry_set, fitness_target))

    s_best = s[0]
    s_worst = s[population_size - 1]

    new_s = []
    while len(new_s) < population_size * crossover_rate:
        s_current = []
        s_current.append(None)
        s_current.append(None)

        i = 0
        while i < 2:
            s_current[i] = s[int(random.uniform(0, population_size - 1))]
            P_s_current = get_choice_probability(0.9, s_best, s_worst, s_current[i], entry_set, fitness_target)
            if select_solution(P_s_current):
                i += 1
        s_1, s_2 = crossover(s_current[0], s_current[1], len(entry_set))

        new_s.append(s_1)
        new_s.append(s_2)
    while len(new_s) < population_size * (crossover_rate + mutation_rate):
        s_current = s[int(random.uniform(0, population_size - 1))]
        s_mutated = mutation(s_current, len(entry_set))
        new_s.append(s_mutated)

    while len(new_s) < population_size * (crossover_rate + mutation_rate + cloning_rate):
        clones = clone_N_individuals(s, int(population_size * cloning_rate))
        new_s.extend(clones)

    new_s.sort(key=lambda k: fitness_function(k, entry_set, fitness_target))

    if fitness_function(new_s[0], entry_set, fitness_target) < fitness_function(s_best, entry_set, fitness_target):
        s_best = new_s[0]

    return genetic_solver(entry_set, new_s, s_best, population_size, iterations_number, crossover_rate, mutation_rate,
                          cloning_rate, fitness_target, iteration+1)


def is_valid_solution(set_of_problem, subset_solution):
    return set(subset_solution).issubset(set(set_of_problem))


def goal_function(solution_subset, target):
    return abs(np.sum(solution_subset) - target)


def is_optimal_solution(solution_subset, target):
    return goal_function(solution_subset, target) == 0


def generate_random_solution(entry_set, size_of_subset):
    return random.sample(entry_set, size_of_subset)


def find_close_neighbour(entry_set, solution):
    new_subset = solution
    first, second = random.choices(entry_set, k=2)
    if first in solution:
        new_subset.remove(first)
    else:
        new_subset.append(first)
    if second in solution and second in new_subset:
        if random.randint(1, 2) == 1:
            new_subset.remove(second)
    else:
        if random.randint(1, 2) == 1:
            new_subset.append(second)
    return new_subset



#Genetics methods

def generate_initial_population(array_length):
    population = []
    for _ in range(0, array_length):
        population.append(''.join(random.choice(["0", "1"]) for _ in range(array_length)))
    return population


def fitness_function(solution, array, fitness_target):
    sum = 0
    for index, entry in enumerate(solution):
        if entry == "1":
            sum += array[index]
    return abs(sum - fitness_target)


def get_choice_probability(P_s_best, s_best, s_worst, s_current, array, fitness_target):
    step = P_s_best / float(fitness_function(s_worst, array, fitness_target) - fitness_function(s_best, array, fitness_target) + 1)
    return P_s_best - (fitness_function(s_current, array, fitness_target) - fitness_function(s_best, array, fitness_target)) * step


def select_solution(P_s_current):
    rand = random.uniform(0, 1)
    return rand <= P_s_current


def crossover(s_1, s_2, length):
    crossover_point = int(random.uniform(0, length - 1))
    new_individual_1 = s_1[:crossover_point] + s_2[crossover_point:]
    new_individual_2 = s_2[:crossover_point] + s_1[crossover_point:]
    return new_individual_1, new_individual_2


def mutation(s_current, length):
    gene_index = int(random.uniform(0, length - 1))
    s_list = list(s_current)
    if s_list[gene_index] == "0":
        s_list[gene_index] = "1"
    else:
        s_list[gene_index] = "0"
    return "".join(s_list)


def clone_N_individuals(sorted_s, N):
    return sorted_s[:N]


def chromosomeToInts(array, s_final):
    result = list(map(int, s_final))
    result = [i ^ 1 for i in result]
    result = list(np.ma.masked_array(array, result))
    result = list(filter(lambda x: (x != 'masked'), result))
    return result

