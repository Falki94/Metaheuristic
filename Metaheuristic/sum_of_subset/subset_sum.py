import argparse
import sys
import logging

import solvers as solver
import tools as tool




if __name__ == "__main__":
    '''
    Main method which allows us run program in many ways.
    For more specific info go to README
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--algorithm", required=False, choices=['b', 'c', 't', 's', 'g'],
                    default='b',
                    help="choose algorithm to use: b = bruteforce, c=climbing, t=tabu, s=simulated_annealing, g=genetic")
    ap.add_argument("-s", "--size", type=int, required=False,
                    help="Set size of input to generate random entry set")
    ap.add_argument("-d", "--debug", required=False, action='store_true', default=False,
                    help="enable debug mode")

    ap.add_argument("-i", "--info", required=False, action='store_true', default=False,
                    help="enable info mode")
    ap.add_argument("-l", "--limit", required=False, type=int, default=1000000,
                    help="Set limit of iterations in algorithm(tabu,climbing,sa);"
                         "default=1000 000")
    ap.add_argument('-ts', '--tabusize', required=False, type=int, default=1000,
                    help="Set size of tabu"
                         "default=1000")


    args = vars(ap.parse_args())
    algorithm = args['algorithm']
    input_data_size = args['size']
    logging_level_debug = args['debug']
    logging_level_info = args['info']
    limit_value = args['limit']
    tabu_size = args['tabusize']

    if logging_level_info:
        logging.basicConfig(stream=sys.stdout, format='%(message)s', level=logging.INFO, )
    elif logging_level_debug:
        logging.basicConfig(stream=sys.stdout, format='%(message)s', level=logging.DEBUG)

    if input_data_size != None:
        tool.generate_random_entry_set(input_data_size)
    else:
        entry_set = [int(x) for x in input().split()]
        T = int(input())
        if algorithm == 'b':
            print(solver.brute_force_solver(entry_set, T))
        elif algorithm == 'c':
            print(solver.climbing_solver(entry_set, T, limit_value))
        elif algorithm == 's':
            print(solver.simulated_annealing_solver(entry_set, T, limit_value))
        elif algorithm == 't':
            print(solver.tabu_solver(entry_set, T, limit_value, tabu_size))
        elif algorithm == 'g':
            limit_value = 990  # Max 995 in genetic case ( recursive )
            crossover_rate = 0.8
            mutation_rate = 0.15
            cloning_rate = 0.05

            s = solver.generate_initial_population(len(entry_set))

            s.sort(key=lambda k: solver.fitness_function(k, entry_set, T))
            print(solver.chromosomeToInts(entry_set, solver.genetic_solver(entry_set, s, s[0], len(entry_set), limit_value, crossover_rate, mutation_rate,
                                        cloning_rate, T)))