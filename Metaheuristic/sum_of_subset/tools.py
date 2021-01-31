import random
import numpy as np


def generate_random_entry_set(input_data_size):
    '''
    Generating random numbers to create set of numbers for Sum of Subset Problem
    :param input_data_size: size of set
    :return: The set of random numbers
    '''
    x = random.sample(range(1, input_data_size*10), input_data_size)
    y = random.randint(1,np.sum(x))
    print(" ".join(str(i) for i in x))
    print(y)



