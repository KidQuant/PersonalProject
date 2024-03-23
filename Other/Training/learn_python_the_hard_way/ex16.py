
# imports the argv package from the sys module
from sys import argv

# unpackages the argv package into two arguments: script and filename
script, filename = argv

# prints a comment regarding the file name entered
print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

# input command accepts any input
input("?")

# prints a comment and assigns the file into the variable 'target' with the intention to write
print("Opening the file...")
target = open(filename, 'w')

# prints another comment
print("Now I'm going to ask you for three lines.")

# asks for inputs for three lines and assigns them into three seperate variables
line1 = input("line 1: ") 
line2 = input("line 2: ")
line3 = input("line 3: ")

#prints a comment
print("I'm going to write these to the file.")

#writes the lines into the file that is assigned to the variable 'target'
#also writes the new text onto the new line.

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

#prints a comment and then closes the file
print("And finally, we close it.")
target.close()
