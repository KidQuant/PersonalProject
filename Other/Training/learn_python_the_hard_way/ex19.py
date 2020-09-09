
# Defines a function named 'cheese_and_crackers' with two arguments:
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #takes the number from the first argument and prints
    print(f"You have {cheese_count} cheeses!")
    #takes the number from the second argument and prints
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #prints two comments
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Uses the function with the numbers directly
print(f"We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#Assigns two numbers to two variables
print("Or, we can use variables from our scripts")
amount_of_cheese = 10
amount_of_crackers = 50

# Uses the function with the assigned variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#Uses math insides of the two variables
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#Uses math and assigned variables inside of the function
print("And we can combine the two, variables and math!")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+ 1000)
