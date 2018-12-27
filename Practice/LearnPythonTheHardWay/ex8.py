#assign four empty spaces to the variable 'formatter'
formatter = '{} {} {} {}'

#passing 1, 2, 3, 4 into the formatter string and print the string
print(formatter.format(1,2,3,4))
#passing one, two, three, four into the formatter string and print the string
print(formatter.format('one','two','three','four'))
#passing bool arguments into the formatter string and print the string
print(True, False, False, True)

print(formatter.format(
    'Try your',
    'Own text here',
    'Maybe a poem',
    'Or a song about fear'
))
