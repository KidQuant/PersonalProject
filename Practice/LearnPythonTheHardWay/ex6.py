
#Assigns 10 to the value 'types_of_people'
types_of_people = 10

#Strings together a sentence and assigns it to the variable x
x = f'There are {types_of_people} types of people'

#assigns the string binary to the variable binary
binary = 'binary'
#assigns the string 'don't' to the variable 'do_not'
do_not = 'don\'t'

#Strings together the variable 'binary' and 'do_not' in a sentence and assigns to variable y
y = f'Those who know {binary} and those who {do_not}'

#prints the variable x and y
print(x)
print(y)

#Strings together x and y in a sentence and prints the sentence
print(f'I said: {x}')
print(f"I also said: '{y}'")

#Assigns a bool value in the variable 'hilarious'
hilarious = False

#Assigns a string to the variable 'joke_evaluation'
joke_evaluation = 'Isn\'t that joke so funny?! {}'

#prints the joke evaluation string with the formatted hilarious bool
print(joke_evaluation.format(hilarious))

#Assigns a string to the variable w and e
w = 'This is the left side of...'
e = 'a string with a right side.'

#prints both strings together.
print(w + e)
