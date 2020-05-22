#Exercise 37: Name that Shape

numbers = range(5,11)

list_of_numbers = []

for x in numbers:
    list_of_numbers.append(x)
    
    
shape_size = int(input("Enter sides: "))

if shape_size == 3:
    print("The shape is a Triangle")

#If sides = 4
#nested loop to figure out
#square or rectangle
elif shape_size == 4:
    sides = input("Are the sides equeal Y/N: ")
    if sides.upper() == 'Y':
        print("The shape is a square")
    elif sides.upper() == 'N':
        print("The shape is a rectangle")
    else:
        print("The side is either a Square or Rectangle")
        
elif shape_size in list_of_numbers:
    print("The shape is a polygon")
    
else:
    print("Invalid shape")