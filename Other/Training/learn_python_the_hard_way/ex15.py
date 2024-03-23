
# imports the package argv from the module sys
from sys import argv

# unpackages argv and request two variables: script and filename
script, filename = argv

# the filename argument is assigned to the variable 'txt
txt = open(filename)

# prints the file name and the contents of the file.
print(f"Here's your file {filename}:")
print(txt.read())

# request the user to type in the file name again using the input command
print("Type the filename again:")
file_again = input("> ")

# assigns the file input to a variable 'txt_again'
txt_again = open(file_again)

# prints the contents of the file again
print(txt_again.read())
