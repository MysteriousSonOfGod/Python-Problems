#import Math

number = float(input("Enter a number>>  "))

if number == 0:
    print("zero")
    
elif number < 0:
    print("Number is negative")
    if abs(number) < 1:
        print("Small")
    
elif number > 0:
    print("Positive ")
    if abs(number) > 1000000:
        print("Large ")

else:
    print()