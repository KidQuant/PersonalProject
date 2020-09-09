
# imports the argv package from the sys module
from sys import argv

# unpackages argv into two variables: script and input_file 
script, input_file = argv

# defines a function named 'print_all' that reads a file
def print_all(f):
    print(f.read())

# defines a function named 'rewind' that starts the function from the first line
def rewind(f):
    f.seek(0)

# prints a function named 'print_a_line' that prints the line count and the contents of the line
def print_a_line(line_count, f):
    print(line_count, f.readline())
# opens the input_file name and assigns it to the variable 'current_file'
current_file = open(input_file)

# prints a comment
print("First let's print the whole file:\n")

# prints the name of the current file
print_all(current_file)

# prints a comment
print("New let's rewind, kind of like a tape.")

# starts the current file at the first line
rewind(current_file)

# prints a comment
print("Let's print three lines:")

# assigns a integer to the variable 'current_lie'
current_line = 1

# 'print_a_line' function prints the current line and the file name
print_a_line(current_line, current_file)

# incremends on the second line 
current_line += 1

# 'current_line' variable is passed through the 'print_a_line' function, which prints the new line the function reads.
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
