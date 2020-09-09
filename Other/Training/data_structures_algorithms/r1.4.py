# r1.4

n = 241

def sum_of_squares(n):
    sum = 0
    for n in range(n-1, 0, -1):
        sum += n *n
    return sum

print(sum_of_squares(n))