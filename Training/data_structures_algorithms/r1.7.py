# r.17

n = 241

def sum_odd_squares(n):
    x = [n*n for n in range(n-1, 0,-1) if n % 2 == 1]
    return sum(x)

print(sum_odd_squares(n))