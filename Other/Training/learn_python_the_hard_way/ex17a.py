from sys import argv

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}") 

open(to_file, 'w').write(open(from_file).read())

print(f"Alright, all done.")




