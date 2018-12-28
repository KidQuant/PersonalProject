#Imports the subpackage argv from the package sys

from sys import argv

#Unpackages the argv function and assigns it to script and filename

script, filename = argv

# uses the open function and assigns it to the value txt

txt = open(filename)

#prints the name of the filename and the contents of the file

print(f'Here\'s your file {filename}:')
print(txt.read())

#asks for the file name again

print('Type the filename again:')
file_again = input('> ')

#opens the file name again and assigns it to the variable txt_again

txt_again = open(file_again)

#prints the contents of the filename

print(txt_again.read())
...
