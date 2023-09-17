import numpy as np


a_matrix = np.random.randint(-8, 8, size=(4,5))
a_matrix

def guass_elimination(matrix):

    rows = matrix.shape[0]
    columns = matrix.shape[1]

    if rows + 1 != columns:
        print('ERROR: Square matrix not given!')
        return

    else:

        n = len(np.delete(matrix, np.s_[:-1], axis=1))
        m = n - 1
        i = 0
        j = i - 1
        x = np.zeros(n)

        while i < n:

            if matrix[i][i] == 0.0:
                print("Divide by zero error!")

            for j in range(i + 1, n):
                # print(i, j)
                scalingFactor = matrix[j][i] / matrix[i][i]
                matrix[j] = matrix[j] - (scalingFactor * matrix[i])
                # print(matrix)
                # print('')

            i += 1

        x[m] = matrix[m][n] / matrix[m][m]

        for k in range(n-2, -1, -1):
            x[k] = matrix[k][n]

            for j in range(k+1, n):
                x[k] = x[k] - matrix[k][j] * x[j]
                print(k, x[k])

            x[k] = x[k] / matrix[k][k]

        for an in range(n):

            print(f'x{an + 1} = {x[an]}')


guass_elimination(a_matrix)
