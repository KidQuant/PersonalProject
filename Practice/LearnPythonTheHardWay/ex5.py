name = 'Zed A. Shaw' #Not my name
age = 35 #Not my age
height = 74 #inches
weight = 180 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

total = age + height + weight
height_cm = height * 2.54
weight_kilo = weight / 2.205
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f'My height in centimeters is {height_cm}.')
print(f'My weight in kilograms is {round(weight_kilo, 2)}.')
