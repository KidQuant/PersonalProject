
#Creates a function called 'cheese_and_crackers' and accepts two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #prints the number of cheese
    print(f"You have {cheese_count} cheese!")
    #prints the boxes of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #prints more comments
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#executes the function with the numbers directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#executes the function with the numbers assigned to a variable instead of directly
print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#executes the function with math inside the variable
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_ofcheese + 100, amount_of_crackers + 1000)

#New function

def practice_function(*args):
    arg1, arg2 = args
    sum_args = arg1 + arg2
    print(sum_args)

practice_function(12,34)
