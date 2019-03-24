# r1.5

n = 241

def sum_of_squares(n):
    x = [n*n for n in range(n-1, 0, -1)]
    return sum(x)

print(sum_of_squares(n))