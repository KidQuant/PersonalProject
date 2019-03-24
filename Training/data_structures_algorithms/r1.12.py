import random

def choice(data):
    return data[random.randrange(0, len(data))]

print(choice([2,4,6,8]))

