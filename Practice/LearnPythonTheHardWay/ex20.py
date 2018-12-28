#Imports the argv features from the package sys

from sys import argv

#unpackage the argv feature and assigns it to script and input_file

script, input_file = argv

#creates a funtion that reads and prints a file.

def print_all(f):
    print(f.read())

#starts from a certain point in the file

def rewind(f):
    f.seek(0)

#prints the line count of the file and the reads the line

def print_a_line(line_count, f):
    print(line_count, f.readline())

#opens an input file and assigns it to the variable 'current_file'

current_file = open(input_file)

print("First let's print the whole file:\n")

#opens a current file and reads the file

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#Starts the current file from the first line

rewind(current_file)

#Reads the current file and prints the first line of it

current_line = 1
print_a_line(current_line, current_file)

#Reads the current file and prints the second line of it

current_line = current_line + 1
print_a_line(current_line, current_file)

#Reads the current file and prints the third line of it

current_line = current_line + 1
print_a_line(current_line, current_file)
