def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

print("Adding two ages together:")
age = add(float(input()), float(input()))

print("subtracting two heights from one another:")
height = subtract(float(input()), float(input()))

print("Multiplying two weights together:")
weight = multiply(float(input()), float(input()))

print("Dividing two IQs")
iq = divide(float(input()), float(input()))

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")
