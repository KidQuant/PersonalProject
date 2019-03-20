name = 'Zed A. Shaw'
age = 35
height = 74 #inches
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}" )
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy"  )
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right.
total = age + height + weight

print(f"if I add {age}, {height}, and {weight} I get {total}")

def inches_to_cm(height):
    cm = height / 0.393710
    return cm

inches_to_cm(74)

def pounds_to_kilo(weight):
    kilo = weight / 2.2046
    return kilo
