import numpy as np


a_matrix = np.random.randint(-8, 0, size=(3,5))


def matrix_check(matrix):
    i = matrix.shape[0]
    j = matrix.shape[1]

    if i + 1 == j:
        b_matrix = np.delete(a_matrix, np.s_[:-1], axis=1)
        #  b_matrix = [ele[3:] for ele in a_matrix]
        return a_matrix, b_matrix

    else:
        print('ERROR: Square matrix not given!')
        return
    

matrix_check(a_matrix)