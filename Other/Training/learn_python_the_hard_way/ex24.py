# prints a string
print("Let's practice everything.")

# prints a string with regular expressions 
print("You\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs.")

# assigns the poem to a variable called 'poem'
# creates a poem using regular expression.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehened passion from intuition
and requires an explaination
\n\t\ twhere there is none.
"""
#prints a border and the point
print("-" * 10)
print(poem)
print("-" * 10)

# assigns an expression that adds up to 5 in the variable 'five.'
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# Defines a variable called 'secret_formula'
def secret_formula(started):

    # multiplies 500 to a variable called 'started' and assigns to variable 'jelly_beans'
    jelly_beans = started * 500

    # divides the variable 'jelly_beans' by 1000 and assigns to variable 'jars'
    jars = jelly_beans / 1000

    # divides the variable 'jars' by 100 and assigns to variable 'crates'
    crates = jars / 100

    #returns the variables 'jelly_beans', 'jars', and 'crates.'
    return jelly_beans, jars, crates


# assigns the int 10000 to the variable start_point
start_point = 10000

# runs the function 'secret_formula' with the variable 'start_point' inside and
# unpacks into three variables
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of : {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans}, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
