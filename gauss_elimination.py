import numpy as np


a_matrix = np.random.randint(-8, 0, size=(3,4))
a_matrix

np.delete(a_matrix, np.s_[-1:], axis=1)

np.vsplit(a_matrix, 1)
a_matrix[:][-1]
b_matrix = [ele[3:] for ele in a_matrix]
print(b_matrix)
np.array([[-8], [-1], [-5]]) == b_matrix
