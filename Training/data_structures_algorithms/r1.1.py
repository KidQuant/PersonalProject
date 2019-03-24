
# R-1.1

n = 1120
m = 3

def is_multiple(n, m):
    if n % m == 0:
        print("True")
    else:
        print("False")

is_multiple(n,m)

# R-1.2
k = 100

def is_even(k):
    if divmod(k,2)[1] == 0 :
        print("True")
    else:
        print("False")

